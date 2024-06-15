import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix
from std_srvs.srv import SetBool
import subprocess

class SaveGpsNode(Node):

    def __init__(self):
        super().__init__('save_gps_node')
        self.srv = self.create_service(SetBool, 'trigger_action', self.trigger_action_callback)
        self.subscription = self.create_subscription(NavSatFix, 'gps/fix', self.gps_callback, 10)
        self.gps_data = None
        self.saving_enabled = False
        self.timer = None
        self.file_path = 'src/kipp_sensors/kipp_sensors/gps_coordinates.txt'  # File to save GPS coordinates
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
            self.get_logger().info(f'Saved GPS position: {position}')
            self.write_to_file(position)
        else:
            self.get_logger().warn('No GPS data available to save.')

    def write_to_file(self, position):
        try:
            with open(self.file_path, 'a') as file:
                file.write(f"{position['latitude']}, {position['longitude']}, {position['altitude']}\n")
            self.get_logger().info('GPS position written to file.')
        except Exception as e:
            self.get_logger().error(f'Failed to write to file: {e}')

        file_path = "/home/ayden/Software_Kipp/src/kipp_sensors/kipp_sensors/gps_coordinates.txt" # change
        server_ip = "10.0.0.171" # change as needed
        port = 12345

        command = f"ros2 run kipp_file_transfer file_send --ros-args -p file_path:={file_path} -p server_ip:={server_ip} -p port:={port}"

        try:
            result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            print("Output:")
            print(result.stdout)
            if result.stderr:
                print("Errors:")
                print(result.stderr)
        except subprocess.CalledProcessError as e:
            print(f"Command '{command}' failed with return code {e.returncode}.")
            print("Error output:")
            print(e.stderr)


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
