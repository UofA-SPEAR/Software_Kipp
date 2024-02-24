import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix
import serial
import pynmea2
from pyudev import Context, Devices

class GPSNode(Node):
    def __init__(self):
        super().__init__('gps_node')
        self.publisher_ = self.create_publisher(NavSatFix, 'gps/fix', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.serial_port = self.find_device_port(vendor_id='1546', product_id='01a9')
        if self.serial_port:
            self.ser = serial.Serial(self.serial_port, baudrate=38400, timeout=2)
        else:
            self.get_logger().error('GPS device not found. Please check the device connection.')
            rclpy.shutdown()

    def find_device_port(self, vendor_id, product_id):
        context = Context()
        for device in context.list_devices(subsystem='tty'):
            if 'ID_VENDOR_ID' in device.properties and 'ID_MODEL_ID' in device.properties:
                if device.properties['ID_VENDOR_ID'] == vendor_id and device.properties['ID_MODEL_ID'] == product_id:
                    return device.device_node
        return None

    def timer_callback(self):
        if self.ser:
            line = self.ser.readline().decode('ascii', errors='ignore')
            if line.startswith('$GNGGA') or line.startswith('$GPGGA'):  # GGA sentences contain position data
                try:
                    msg = pynmea2.parse(line)
                    navsatfix_msg = NavSatFix()
                    navsatfix_msg.header.stamp = self.get_clock().now().to_msg()
                    navsatfix_msg.header.frame_id = 'gps_frame'
                    navsatfix_msg.latitude = msg.latitude
                    navsatfix_msg.longitude = msg.longitude
                    navsatfix_msg.altitude = msg.altitude
                    navsatfix_msg.position_covariance_type = NavSatFix.COVARIANCE_TYPE_UNKNOWN  # Update accordingly
                    self.publisher_.publish(navsatfix_msg)
                except pynmea2.ParseError as e:
                    self.get_logger().warn('Failed to parse NMEA sentence: ' + str(e))
        else:
            self.get_logger().warn('Serial port not initialized.')

def main(args=None):
    rclpy.init(args=args)
    gps_node = GPSNode()
    if gps_node.ser:
        rclpy.spin(gps_node)
    gps_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
