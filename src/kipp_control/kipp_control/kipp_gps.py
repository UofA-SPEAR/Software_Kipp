import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix, NavSatStatus
from std_msgs.msg import Float64
import serial
import pynmea2
from pyudev import Context, Devices

class GPSNode(Node):
    def __init__(self):
        super().__init__('gps_node')
        self.declare_parameter('vendor_id', '0x1546')  # Example VID
        self.declare_parameter('product_id', '0x01a9')  # Example PID
        self.declare_parameter('baud_rate', 38400)
        
        vendor_id = self.get_parameter('vendor_id').get_parameter_value().string_value
        product_id = self.get_parameter('product_id').get_parameter_value().string_value
        baud_rate = self.get_parameter('baud_rate').get_parameter_value().integer_value
        
        serial_port = self.find_serial_port(vendor_id, product_id)
        if serial_port:
            self.serial_connection = serial.Serial(serial_port, baud_rate, timeout=2)
        else:
            self.get_logger().error('GPS device not found')
            rclpy.shutdown()

        self.navsat_publisher = self.create_publisher(NavSatFix, '/gps/fix', 10)
        self.speed_publisher = self.create_publisher(Float64, '/gps/speed', 10)
        self.heading_publisher = self.create_publisher(Float64, '/gps/heading', 10)

        self.timer = self.create_timer(1.0, self.read_and_publish)
    
    def find_serial_port(self, vendor_id, product_id):
        context = Context()
        for device in context.list_devices(subsystem='tty'):
            if 'ID_VENDOR_ID' in device and 'ID_MODEL_ID' in device:
                if device['ID_VENDOR_ID'] == vendor_id and device['ID_MODEL_ID'] == product_id:
                    return device.device_node
        return None

    def read_and_publish(self):
        if not self.serial_connection:
            return
        line = self.serial_connection.readline().decode('ascii', errors='replace')
        # Parsing logic remains the same as previously described...

def main(args=None):
    rclpy.init(args=args)
    node = GPSNode()
    try:
        rclpy.spin(node)
    except Exception as e:
        node.get_logger().error(f'Unhandled exception: {e}')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
