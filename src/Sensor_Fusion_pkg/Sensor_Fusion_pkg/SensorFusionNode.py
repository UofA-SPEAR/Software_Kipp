import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Quaternion, Twist, Pose, Point, Vector3
import random
import numpy as np


####Test run for if ekf outputs data
class FakeIMUPublisher(Node):
    def __init__(self):
        super().__init__('fake_imu_publisher')
        self.publisher_ = self.create_publisher(Odometry, 'odom/data', 10)
        self.timer = self.create_timer(1.0, self.publish_odom_data)

    def publish_odom_data(self):
        msg = Odometry()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = "odom"
        msg.child_frame_id = "base_link"

        # Fake pose
        msg.pose.pose.position = Point(x=random.uniform(-5, 5), 
                                       y=random.uniform(-5, 5), 
                                       z=0.0)
        yaw = random.uniform(-3.14, 3.14)
        msg.pose.pose.orientation = Quaternion(x=0.0, y=0.0, 
                                               z=np.sin(yaw/2), w=np.cos(yaw/2))
        msg.pose.covariance = np.diag([0.1]*3 + [0.1]*3).flatten().tolist()

        # Fake velocity
        msg.twist.twist.linear = Vector3(x=random.uniform(-1, 1), 
                                         y=random.uniform(-1, 1), 
                                         z=0.0)
        msg.twist.twist.angular = Vector3(x=0.0, y=0.0, 
                                          z=random.uniform(-1, 1))
        msg.twist.covariance = np.diag([0.1]*3 + [0.1]*3).flatten().tolist()

        self.publisher_.publish(msg)
        #self.get_logger().info('Publishing Odometry Data')

def main(args=None):
    rclpy.init(args=args)
    odom_publisher = FakeIMUPublisher()
    rclpy.spin(odom_publisher)
    odom_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
