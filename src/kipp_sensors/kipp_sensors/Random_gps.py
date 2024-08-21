import rclpy
import random
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix
from sensor_msgs.msg import NavSatStatus
from std_msgs.msg import Header, Float64

class GpsNode(Node):

    def __init__(self):
        super().__init__('gps_node')
        self.gps_publisher_ = self.create_publisher(NavSatFix, 'gps/fix', 10)
        self.heading_publisher_ = self.create_publisher(Float64, 'gps/heading', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        # Generate and publish GPS fix data
        gps_msg = NavSatFix()
        gps_msg.header = Header()
        gps_msg.header.stamp = self.get_clock().now().to_msg()
        gps_msg.header.frame_id = "gps"

        gps_msg.status.status = NavSatStatus.STATUS_FIX
        gps_msg.status.service = NavSatStatus.SERVICE_GPS

        # Generate random latitude and longitude within a realistic range
        # Limiting the range to a region around 53.5561, -113.4938
        gps_msg.latitude = random.uniform(53.0, 54.0)
        gps_msg.longitude = random.uniform(-114.0, -113.0)

        # Random altitude between -500 meters and 5000 meters
        gps_msg.altitude = random.uniform(-500.0, 5000.0)

        gps_msg.position_covariance[0] = 0
        gps_msg.position_covariance[4] = 0
        gps_msg.position_covariance[8] = 0
        gps_msg.position_covariance_type = NavSatFix.COVARIANCE_TYPE_DIAGONAL_KNOWN

        self.gps_publisher_.publish(gps_msg)

        # Generate and publish heading data
        heading_msg = Float64()
        heading_msg.data = random.uniform(0.0, 360.0)
        self.heading_publisher_.publish(heading_msg)

def main(args=None):
    rclpy.init(args=args)

    gps_node = GpsNode()

    rclpy.spin(gps_node)

    # Destroy the node explicitly
    gps_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
