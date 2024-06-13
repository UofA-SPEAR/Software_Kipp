
import rclpy
import random
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix
from sensor_msgs.msg import NavSatStatus
from std_msgs.msg import Header

class GpsNode(Node):

    def __init__(self):
        super().__init__('gps_node')
        self.publisher_ = self.create_publisher(NavSatFix, 'gps/fix', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = NavSatFix()
        msg.header = Header()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = "gps"

        msg.status.status = NavSatStatus.STATUS_FIX
        msg.status.service = NavSatStatus.SERVICE_GPS

        # Generate random latitude and longitude within a realistic range
        msg.latitude = random.uniform(-90.0, 90.0)
        msg.longitude = random.uniform(-180.0, 180.0)

        # Random altitude between -500 meters and 5000 meters
        msg.altitude = random.uniform(-500.0, 5000.0)

        msg.position_covariance[0] = 0
        msg.position_covariance[4] = 0
        msg.position_covariance[8] = 0
        msg.position_covariance_type = NavSatFix.COVARIANCE_TYPE_DIAGONAL_KNOWN

        self.publisher_.publish(msg)
    # def call_gps_service(self, )
        
def main(args=None):
    rclpy.init(args=args)

    gps_node = GpsNode()

    rclpy.spin(gps_node)

    # Destroy the node explicitly
    gps_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()