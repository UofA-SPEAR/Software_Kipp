import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix
from std_srvs.srv import SetBool

class SaveGpsNode(Node):

    def __init__(self):
        super().__init__('save_gps_node')
        self.srv = self.create_service(SetBool, 'trigger_action', self.trigger_action_callback)
        self.subscription = self.create_subscription(NavSatFix, 'gps/fix', self.gps_callback, 10)
        self.gps_data = None
        self.saved_positions = []
        self.saving_enabled = False
        self.timer = None
        self.get_logger().info('Service node has been started.')

    def gps_callback(self, msg):
        self.gps_data = msg
        self.get_logger().info(f'Received GPS data: lat={msg.latitude}, lon={msg.longitude}, alt={msg.altitude}')

    def save_gps_callback(self):
        if self.gps_data is not None:
            position = {
                'latitude': self.gps_data.latitude,
                'longitude': self.gps_data.longitude,
                'altitude': self.gps_data.altitude
            }
            self.saved_positions.append(position)
            self.get_logger().info(f'Saved GPS position: {position}')
        else:
            self.get_logger().warn('No GPS data available to save.')

    def trigger_action_callback(self, request, response):
        if request.data:
            if not self.saving_enabled:
                self.saving_enabled = True
                self.timer = self.create_timer(2.0, self.save_gps_callback)
                self.get_logger().info('GPS saving enabled.')
                response.success = True
                response.message = 'GPS position saving enabled.'
            else:
                self.get_logger().info('GPS saving already enabled.')
                response.success = True
                response.message = 'GPS position saving was already enabled.'
        else:
            if self.saving_enabled:
                self.saving_enabled = False
                if self.timer is not None:
                    self.timer.cancel()
                    self.timer = None
                self.get_logger().info('GPS saving disabled.')
                response.success = True
                response.message = 'GPS position saving disabled.'
            else:
                self.get_logger().info('GPS saving already disabled.')
                response.success = True
                response.message = 'GPS position saving was already disabled.'

        return response

def main(args=None):
    rclpy.init(args=args)
    save_gps_node = SaveGpsNode()
    rclpy.spin(save_gps_node)
    save_gps_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

