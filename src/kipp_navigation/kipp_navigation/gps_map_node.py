import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix
from std_msgs.msg import Float64
import math

class GPSDistanceCalculator(Node):
    def __init__(self):
        super().__init__('gps_distance_calculator')
        
        self.create_subscription(NavSatFix, '/gps/fix', self.gps_callback, 10)
        self.create_subscription(Float64, '/gps/heading', self.heading_callback, 10)
        
        # Input destination GPS coordinates
        self.dest_lat = None
        self.dest_lon = None
        
        self.current_heading = 0.0
        
        self.get_logger().info("Enter destination GPS coordinates in the format: lat lon")
        
        self.get_user_input()
    
    def get_user_input(self):
        try:
            # User input for destination
            input_str = input("Enter destination GPS coordinates (latitude longitude): ")
            lat_str, lon_str = input_str.split()
            self.dest_lat = float(lat_str)
            self.dest_lon = float(lon_str)
            self.get_logger().info(f"Destination set to lat: {self.dest_lat}, lon: {self.dest_lon}")
        except ValueError:
            self.get_logger().error("Invalid input. Please enter valid latitude and longitude.")
            return
    
    def gps_callback(self, msg):
        if self.dest_lat is not None and self.dest_lon is not None:
            current_lat = msg.latitude
            current_lon = msg.longitude
            
            distance = self.calculate_distance(current_lat, current_lon, self.dest_lat, self.dest_lon)
            heading_change = self.calculate_heading_change(current_lat, current_lon, self.dest_lat, self.dest_lon)
            
            self.get_logger().info(f"Distance to destination: {distance:.2f} meters | Adjust heading by: {heading_change:.2f} degrees")

    def heading_callback(self, msg):
        self.current_heading = msg.data
    
    def calculate_distance(self, lat1, lon1, lat2, lon2):
        # Convert latitude and longitude from degrees to radians
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
        
        # Haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        r = 6371000  # Radius of Earth in meters
        distance = r * c
        return distance

    def calculate_heading_change(self, lat1, lon1, lat2, lon2):
        # Calculate the initial heading from (lat1, lon1) to (lat2, lon2)
        dlon = lon2 - lon1
        y = math.sin(dlon) * math.cos(lat2)
        x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(dlon)
        initial_heading = math.atan2(y, x)
        
        # Convert from radians to degrees
        initial_heading = math.degrees(initial_heading)
        
        # Normalize the heading to be in the range [0, 360)
        initial_heading = (initial_heading + 360) % 360
        
        # Calculate the required change in heading
        heading_change = initial_heading - self.current_heading
        if heading_change > 180:
            heading_change -= 360
        elif heading_change < -180:
            heading_change += 360
        
        return heading_change

def main(args=None):
    rclpy.init(args=args)
    gps_distance_calculator_node = GPSDistanceCalculator()
    rclpy.spin(gps_distance_calculator_node)
    
    gps_distance_calculator_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
