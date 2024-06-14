#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import socket

class FileReceiverNode(Node):
    def __init__(self):
        super().__init__('file_receiver_node')

        # Declare parameters for server IP, port, and output file
        self.declare_parameter('server_ip', '10.0.0.171')
        self.declare_parameter('port', 12345)
        self.declare_parameter('output_file', 'received_file.txt')

        # Get parameters
        self.server_ip = self.get_parameter('server_ip').get_parameter_value().string_value
        self.port = self.get_parameter('port').get_parameter_value().integer_value
        self.output_file = self.get_parameter('output_file').get_parameter_value().string_value

        # Start listening for file transfer
        self.receive_file()

    def receive_file(self):
        try:
            # Create a socket object
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Bind the socket to the IP and port
            server_socket.bind((self.server_ip, self.port))
            # Listen for incoming connections
            server_socket.listen(1)
            self.get_logger().info(f"Listening for connections on {self.server_ip}:{self.port}...")

            # Accept the incoming connection
            conn, addr = server_socket.accept()
            self.get_logger().info(f"Connection from {addr} has been established.")

            with open(self.output_file, 'wb') as file:
                while True:
                    # Receive data from the client
                    data = conn.recv(1024)
                    if not data:
                        break
                    # Write the data to the file
                    file.write(data)
            
            self.get_logger().info(f"File received and saved as {self.output_file}.")
            conn.close()
            server_socket.close()
        
        except Exception as e:
            self.get_logger().error(f"Error receiving file: {e}")

def main(args=None):
    rclpy.init(args=args)
    node = FileReceiverNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
