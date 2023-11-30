import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
from sensor_msgs.msg import JointState
from sensor_msgs.msg import Joy
from rclpy.qos import QoSProfile
import time
import numpy as np
from rclpy.time import Time
import sys
import math

roverCommandTopic = "rover_controls"
steering_upper_limit = 0
steering_lower_limit = 0

baseLength = 30  # length between front and back wheels
baseWidth = 20  # width between wheels
maxSpeed = 15

class DriveControl(Node):

    def __init__(self):
            super().__init__('drive_control')

            rover_Command  = self.create_subscription(msg_type=RoverCommand, 
                                                        topic=roverCommandTopic, 
                                                        callback=self.rover_Command_Msg, 
                                                        qos_profile=qos_profile_sensor_data)
            
            # Initialize member variables
            self.throttle = 0
            self.steering = 0
            self.turn = 0
            # Additional variables for wheel speeds, etc.
            self.wheel_angles = [0] * 6  # Assuming 6 wheels
    
    def rover_Command_Msg(self,msg):
        self.throttle = msg.throttle 
        self.steering = self.steering_conversion(msg.steering)
        self.turn = msg.turn
    
    def steering_conversion(value):

        if value < -1 or value > 1:
            raise ValueError("Steering value must be between -1 and 1")
        
        # Linear interpolation between min and max radii
        return steering_lower_limit + (steering_upper_limit - steering_lower_limit) * (value + 1) / 2
    
    def calculateWheelAngle(self, steering):
        # ackerman geometry for individual wheel angles (assuming wheel_angles[0-2] = left, wheel_angles[3-5] = right
        
        for x in range(6):
            if (x < 3 and steering< 0) or (x >= 3 and steering > 0): # inner wheel
                self.wheel_angles[x] = math.atan(baseLength/(baseLength/math.tan(steering) - baseWidth/2))
            
            elif (x < 3 and steering > 0) or (x >= 3 and steering < 0): # outer wheel
                self.wheel_angles[x] = math.atan(baseLength/(baseLength/math.tan(steering) + baseWidth/2))
            
            else: # steering = 0
                self.wheel_angles[x] = 0

