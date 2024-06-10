import rclpy
from rclpy.node import Node
from rclpy.callback_groups import ReentrantCallbackGroup
from sensor_msgs.msg import NavSatFix
from std_srvs.srv import Trigger

class SaveGpsNode(Node):

    def __init__(self):
        super().__init__('save_gps_node')
        self.subscription = self.create_subscription(
            NavSatFix,
            'gps/fix',
            self.gps_callback,
            10)
        self.service = self.create_service(Trigger, 'save_gps', self.save_gps_callback)
        self.gps_data = None
        self.saved_positions = []
        self.callback_group = ReentrantCallbackGroup()
        self.get_logger().info('Save GPS Node has been started.')

    def gps_callback(self, msg):
        self.gps_data = msg
        self.get_logger().info(f'Received GPS data: lat={msg.latitude}, lon={msg.longitude}, alt={msg.altitude}')

    def save_gps_callback(self, request, response):
        if self.gps_data is not None:
            position = {
                'latitude': self.gps_data.latitude,
                'longitude': self.gps_data.longitude,
                'altitude': self.gps_data.altitude
            }
            self.saved_positions.append(position)
            self.get_logger().info(f'Saved GPS position: {position}')
            response.success = True
            response.message = 'GPS position saved.'
        else:
            response.success = False
            response.message = 'No GPS data available to save.'
        return response

def main(args=None):
    rclpy.init(args=args)

    save_gps_node = SaveGpsNode()

    rclpy.spin(save_gps_node)

    # Destroy the node explicitly
    save_gps_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
