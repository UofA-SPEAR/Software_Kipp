import subprocess
import cv2 as cv
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ArucoPublisher(Node):
    def __init__(self):
        super().__init__('aruco_publisher')
        self.publisher = self.create_publisher(String, 'aruco_marker_ids', 10)
    
    def publish_marker_ids(self, marker_ids):
        for marker_id in marker_ids:
            msg = String()
            msg.data = f'ID: {marker_id}'
            self.publisher.publish(msg)
            self.get_logger().info(f'Published marker ID: {marker_id}')

def get_device_path_by_serial_or_bus(serial_number=None, bus_info=None):
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

def main(args=None):
    rclpy.init(args=args)
    aruco_publisher = ArucoPublisher()

    # Example usage
    serial_number = "66255C60"  # Or use bus_info = "usb-0000:00:14.0-3"
    device_path = get_device_path_by_serial_or_bus(serial_number=serial_number)

    if device_path:
        print(f"Opening device at {device_path}")
        cap = cv.VideoCapture(device_path)

        if not cap.isOpened():
            print("Error: Could not open the camera feed.")
            return

        while rclpy.ok():
            # Load the ArUco dictionary
            dictionary = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_4X4_100)

            # Create parameters for the ArUco detector
            parameters = cv.aruco.DetectorParameters()

            # Create an ArUco detector object
            detector = cv.aruco.ArucoDetector(dictionary, parameters)

            # Read a frame from the webcam
            ret, frame = cap.read()
            if not ret:
                print("Failed to capture frame from webcam")
                break

            # Detect ArUco markers in the frame
            markerCorners, markerIds, rejectedCandidates = detector.detectMarkers(frame)

            # Publish detected marker IDs
            if markerIds is not None:
                marker_ids = markerIds.flatten().tolist()
                aruco_publisher.publish_marker_ids(marker_ids)

            # Check for 'q' key to quit
            if cv.waitKey(1) & 0xFF == ord('q'):
                break

        # Release resources
        cap.release()
        cv.destroyAllWindows()
    else:
        print(f"Error: Could not find the device with serial number {serial_number}.")

    # Clean up
    aruco_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
