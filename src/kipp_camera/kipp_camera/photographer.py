import rclpy
from rclpy.node import Node
from std_srvs.srv import Trigger
import cv2 as cv
import subprocess
import os

class ImageCaptureNode(Node):
    def __init__(self):
        super().__init__('image_capture_node')
        self.srv = self.create_service(Trigger, 'capture_image', self.capture_image_callback)
        self.get_logger().info('Ready to capture images. Call the "capture_image" service.')
        
        # Initialize image counter
        self.image_counter = 0

    def get_device_path_by_serial_or_bus(self, serial_number=None, bus_info=None):
        try:
            # Get the list of all /dev/video* devices
            output = subprocess.check_output("ls /dev/video*", shell=True, text=True)
            devices = output.strip().split("\n")
            
            for device in devices:
                if serial_number:
                    cmd = f"udevadm info --query=all --name={device} | grep '{serial_number}'"
                elif bus_info:
                    cmd = f"udevadm info --query=all --name={device} | grep '{bus_info}'"
                else:
                    continue
                
                try:
                    result = subprocess.check_output(cmd, shell=True, text=True)
                    if result:
                        return device
                except subprocess.CalledProcessError:
                    continue

            return None

        except subprocess.CalledProcessError:
            return None

    def capture_image_callback(self, request, response):
        self.get_logger().info('Service call received to capture image.')
        
        # Set up the camera
        serial_number = "66255C60"  # Or use bus_info = "usb-0000:00:14.0-3"
        device_path = self.get_device_path_by_serial_or_bus(serial_number=serial_number)

        if device_path:
            self.get_logger().info(f"Opening device at {device_path}")
            cap = cv.VideoCapture(device_path)

            if not cap.isOpened():
                response.success = False
                response.message = "Error: Could not open the camera."
                return response
            
            # Capture a single frame
            ret, frame = cap.read()
            if not ret:
                response.success = False
                response.message = "Error: Failed to capture image."
                cap.release()
                return response
            
            # Generate a unique file name
            self.image_counter += 1
            file_name = f'captured_image{self.image_counter}.png'
            cv.imwrite(file_name, frame)
            self.get_logger().info(f'Image saved as {file_name}.')
            
            # Release resources
            cap.release()
            
            response.success = True
            response.message = f'Image captured and saved as {file_name}.'
        else:
            response.success = False
            response.message = f"Error: Could not find the device with serial number {serial_number}."
        
        return response

def main(args=None):
    rclpy.init(args=args)
    image_capture_node = ImageCaptureNode()
    rclpy.spin(image_capture_node)
    image_capture_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
