import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix
from std_msgs.msg import Float64
from geopy.distance import geodesic
import matplotlib.pyplot as plt
import numpy as np

class GPSDisplayNode(Node):
    def __init__(self):
        super().__init__('gps_display_node')
        self.current_lat = None
        self.current_lon = None
        self.orientation = None
        
# -----------------------------------------------------------------------
        self.dest_lat = 53.556 # Edit for task
        self.dest_lon = -113.4938 # Edit for Task
# -----------------------------------------------------------------------

        self.create_subscription(NavSatFix, 'gps/fix', self.pose_callback, 10)
        self.create_subscription(Float64, 'gps/heading', self.orientation_callback, 10)
        
        self.arrow_needed = None
        self.arrow_current = None
        self.init_plot()

    def pose_callback(self, msg):
        self.current_lat = msg.latitude
        self.current_lon = msg.longitude
        self.update_plot()

    def orientation_callback(self, msg):
        self.orientation = msg.data
        self.update_plot()

    def calculate_bearing(self, lat1, lon1, lat2, lon2):
        diff_lon = np.radians(lon2 - lon1)
        lat1 = np.radians(lat1)
        lat2 = np.radians(lat2)
        x = np.sin(diff_lon) * np.cos(lat2)
        y = np.cos(lat1) * np.sin(lat2) - (np.sin(lat1) * np.cos(lat2) * np.cos(diff_lon))
        initial_bearing = np.degrees(np.arctan2(x, y))
        compass_bearing = (initial_bearing + 360) % 360
        return compass_bearing

    def init_plot(self):
        plt.ion()
        self.fig, self.ax = plt.subplots()
        self.text = self.ax.text(0.5, 0.8, '', transform=self.ax.transAxes, ha='center', va='center', fontsize=12)
        self.ax.axis('off')

        # Adding legend
        self.red_arrow = plt.Line2D([0], [0], color='red', lw=2, label='Needed Orientation')
        self.blue_arrow = plt.Line2D([0], [0], color='blue', lw=2, label='Current Orientation')
        self.ax.legend(handles=[self.red_arrow, self.blue_arrow], loc='upper right')

        plt.show()

    def update_plot(self):
        if self.current_lat is not None and self.current_lon is not None:
            distance = geodesic((self.current_lat, self.current_lon), (self.dest_lat, self.dest_lon)).meters
            needed_orientation = self.calculate_bearing(self.current_lat, self.current_lon, self.dest_lat, self.dest_lon)
            text_content = f"Distance: {distance:.2f} meters\nNeeded Orientation: {needed_orientation:.2f}°"
        else:
            text_content = "Distance: Calculating...\nNeeded Orientation: Calculating..."
        
        if self.orientation is not None:
            text_content += f"\nCurrent Orientation: {self.orientation:.2f}°"
        else:
            text_content += "\nCurrent Orientation: Calculating..."

        # Remove old arrows if they exist
        if self.arrow_needed:
            self.arrow_needed.remove()
        if self.arrow_current:
            self.arrow_current.remove()
        
        if self.current_lat is not None and self.current_lon is not None:
            needed_orientation = self.calculate_bearing(self.current_lat, self.current_lon, self.dest_lat, self.dest_lon)
            needed_dx = 0.1 * np.cos(np.radians(needed_orientation))
            needed_dy = 0.1 * np.sin(np.radians(needed_orientation))
            self.arrow_needed = self.ax.arrow(0.5, 0.5, needed_dx, needed_dy, head_width=0.05, head_length=0.1, fc='red', ec='red', transform=self.ax.transAxes)

        if self.orientation is not None:
            current_dx = 0.1 * np.cos(np.radians(self.orientation))
            current_dy = 0.1 * np.sin(np.radians(self.orientation))
            self.arrow_current = self.ax.arrow(0.5, 0.5, current_dx, current_dy, head_width=0.05, head_length=0.1, fc='blue', ec='blue', transform=self.ax.transAxes)

        self.text.set_text(text_content)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

def main(args=None):
    rclpy.init(args=args)
    gps_display_node = GPSDisplayNode()
    try:
        rclpy.spin(gps_display_node)
    except KeyboardInterrupt:
        pass
    finally:
        gps_display_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()


