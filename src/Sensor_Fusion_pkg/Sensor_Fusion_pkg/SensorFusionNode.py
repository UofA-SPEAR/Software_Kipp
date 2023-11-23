import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu , NavSatFix #for IMU and GPS messages
from nav_msgs.msg import Odometry

class SensorFusionNode(Node):
    def __init__(self):
        super().__init__('sensor_fusion_node')
        # Initialize subscribers for IMU, GPS, and wheel encoders
        # ...

def main(args=None):
    rclpy.init(args=args)
    node = SensorFusionNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
