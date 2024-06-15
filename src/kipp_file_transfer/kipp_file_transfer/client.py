#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import socket

def send_file(server_ip, port, file_path):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, port))
        print(f"Connected to {server_ip}:{port}")

        with open(file_path, 'rb') as file:
            while True:
                data = file.read(1024)
                if not data:
                    break
                client_socket.sendall(data)

        print(f"File {file_path} sent successfully.")
        client_socket.close()
        return True  # Return True to indicate successful file transfer
    except Exception as e:
        print(f"Failed to send file: {e}")
        return False  # Return False if file transfer fails

class FileTransferNode(Node):
    def __init__(self):
        super().__init__('file_transfer_node')

        self.declare_parameter('file_path', '/home/ayden/Software_Kipp/src/kipp_sensors/kipp_sensors/gps_coordinates.txt')
        self.declare_parameter('server_ip', '127.0.0.1')
        self.declare_parameter('port', 12345)

        self.file_path = self.get_parameter('file_path').get_parameter_value().string_value
        self.server_ip = self.get_parameter('server_ip').get_parameter_value().string_value
        self.port = self.get_parameter('port').get_parameter_value().integer_value
        self.timer_period = 5.0  # seconds
        self.timer = self.create_timer(self.timer_period, self.timer_callback)
        self.get_logger().info('File Transfer Node has been started.')
        self.file_sent = False  # Track if file has been sent

    def timer_callback(self):
        if not self.file_sent:
            self.get_logger().info(f'Sending file: {self.file_path} to {self.server_ip}:{self.port}')
            if send_file(self.server_ip, self.port, self.file_path):
                self.file_sent = True
                self.get_logger().info('File transfer complete. Terminating node.')
                raise SystemExit

def main(args=None):
    rclpy.init(args=args)
    node = FileTransferNode()
    try:
        rclpy.spin(node)
    except SystemExit:
        rclpy.logging.get_logger("Quitting").info('Done')
    
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
