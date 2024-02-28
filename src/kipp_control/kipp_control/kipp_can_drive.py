# Drive Motors
# Front Left: 0x10
# Front Right: 0x11
# Middle Left: 0x12
# Middle Right: 0x13
# Back Left: 0x14
# Back Right: 0x15
# Steering Motors
# Front Left: 0x20
# Front Right: 0x21
# Back Left: 0x22
# Back Right: 0x23

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix, NavSatStatus
from std_msgs.msg import Float64
import can
import struct
from can.message import Message
from geometry_msgs.msg import Twist
import math

class Kipp_Can_Drive(Node):
    def __init__(self):

        super().__init__('kipp_can_drive')
        
        self.cmd_vel_sub = self.create_subscription(Twist, 'cmd_vel', self.cmd_vel_callback, 10)
        
        self.bus = can.interface.Bus(channel='can0', bustype='socketcan')

        self.W = 1.0  # Width of the rover (meters)
        self.L = 1.5  # Length of the rover (meters)


    def cmd_vel_callback(self, msg):
        v = msg.linear.x  # Linear velocity (m/s)
        omega = msg.angular.z  # Angular velocity (rad/s)

        steering_angles = self.calculate_steering_angles(v, omega)

        wheel_velocities = self.calculate_wheel_velocities(v, omega)

        for actuator_id, angle in steering_angles.items():
            # Convert actuator ID from your custom mapping to actual CAN ID
            can_id = self.steering_actuator_id_to_can_id(actuator_id)
            message = self.create_steering_command(can_id, angle)
            self.bus.send(message)
    
        # Send drive commands to wheel actuators
        for actuator_id, velocity in wheel_velocities.items():
            # Convert actuator ID from your custom mapping to actual CAN ID
            can_id = self.drive_actuator_id_to_can_id(actuator_id)
            message = self.create_drive_command(can_id, velocity)
            self.bus.send(message)
        
    def steering_actuator_id_to_can_id(self, actuator_id):
        # Map your actuator_id to its corresponding CAN ID for steering motors
        mapping = {
            "front_left": 0x20,
            "front_right": 0x21,
            "back_left": 0x22,
            "back_right": 0x23,
        }
        return mapping.get(actuator_id, None)

    def drive_actuator_id_to_can_id(self, actuator_id):
        # Map your actuator_id to its corresponding CAN ID for drive motors
        mapping = {
            "fl": 0x10,
            "fr": 0x11,
            "ml": 0x12,
            "mr": 0x13,
            "bl": 0x14,
            "br": 0x15,
        }
        return mapping.get(actuator_id, None)

    def calculate_steering_angles(self, v, omega):
        """
        Calculate wheel velocities for a 6-wheel rover with differential speeds.
        
        Parameters:
        v (float): Linear velocity of the rover (m/s)
        omega (float): Angular velocity of the rover (rad/s)
        
        Returns:
        dict: Wheel velocities (m/s) for each wheel (fl, fr, ml, mr, bl, br)
        """
        
        if omega == 0:
            return {"front_left": 0, "front_right": 0, "back_left": 0, "back_right": 0}
    
    # Radius of the turn
        R = v / omega
        
        # Calculate the steering angle
        # Using the bicycle model approximation for simplicity
        angle = math.atan(self.L / R)
        
        # Convert to degrees
        angle_deg = math.degrees(angle)
        
        # Assuming symmetric steering angles for simplicity
        angles = {
            "front_left": angle_deg, "front_right": angle_deg,
            "back_left": -angle_deg, "back_right": -angle_deg  # Negative for back wheels if they steer opposite to front
        }
    
        return angles

    def calculate_wheel_velocities(self, v, omega):
        """
        Calculate wheel velocities for a 6-wheel rover with differential speeds.
        
        Parameters:
        v (float): Linear velocity of the rover (m/s)
        omega (float): Angular velocity of the rover (rad/s)
        
        Returns:
        dict: Wheel velocities (m/s) for each wheel (fl, fr, ml, mr, bl, br)
        """
        # Velocity of the center of the rover
        v_center = v
        
        # Assuming the center of rotation is at the center of the rover
        # Calculate the velocity for each wheel
        vr = v_center + (omega * self.W / 2)  # Velocity of right wheels
        vl = v_center - (omega * self.W / 2)  # Velocity of left wheels
        
        # Assuming same velocity for front, middle, and back wheels on each side
        velocities = {
            "fl": vl, "fr": vr,
            "ml": vl, "mr": vr,
            "bl": vl, "br": vr
        }
        
        return velocities
    
    def create_drive_command(actuator_id, velocity, priority=0, command_id=0x03, receiver_node_id=1, sender_node_id=1):
        # Construct arbitration ID
        arbitration_id = priority << 24 | command_id << 16 | receiver_node_id << 8 | sender_node_id
        
        # Pack data (velocity)
        data = struct.pack("f", velocity)  # 'f' for float32
        
        # Create CAN message
        message = can.Message(arbitration_id=arbitration_id, data=data, is_extended_id=True)
        
        return message

    def create_steering_command(actuator_id, angle, priority=0, command_id=0x02, receiver_node_id=1, sender_node_id=1):
        # Construct arbitration ID
        arbitration_id = priority << 24 | command_id << 16 | receiver_node_id << 8 | sender_node_id
        
        # Pack data (angle)
        data = struct.pack("f", angle)  # 'f' for float32
        
        # Create CAN message
        message = can.Message(arbitration_id=arbitration_id, data=data, is_extended_id=True)
        
        return message
    

def main(args=None):

    rclpy.init(args=args)

    gps_node = GPSNode()

    rclpy.spin(gps_node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    gps_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()


