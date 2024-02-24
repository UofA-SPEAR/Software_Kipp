import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix

class DummyGPSPublisher(Node):
    def __init__(self):
        super().__init__('dummy_gps_publisher')
        self.navsat_publisher = self.create_publisher(NavSatFix, '/gps/fix', 10)
        self.timer_period = 1.0  # seconds
        self.timer = self.create_timer(self.timer_period, self.publish_dummy_gps)

    def publish_dummy_gps(self):
        msg = NavSatFix()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = "dummy_gps"
        msg.latitude = 37.386052  # Example latitude
        msg.longitude = -122.083851  # Example longitude
        msg.altitude = 100.0  # Example altitude
        self.navsat_publisher.publish(msg)
        self.get_logger().info(f"Publishing Dummy GPS Data: {msg.latitude}, {msg.longitude}, {msg.altitude}")

def main(args=None):
    rclpy.init(args=args)
    dummy_gps_publisher = DummyGPSPublisher()
    rclpy.spin(dummy_gps_publisher)
    dummy_gps_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
