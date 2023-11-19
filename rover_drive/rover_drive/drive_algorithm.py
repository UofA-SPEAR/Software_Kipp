import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
from sensor_msgs.msg import JointState
from sensor_msgs.msg import Joy
from rclpy.qos import QoSProfile
from rclpy.qos import qos_profile_sensor_data
import time
import numpy as np
from rclpy.time import Time
import sys
from interfaces.msg import RoverCommand
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
        self.wheel_speeds = [0] * 6  # Assuming 6 wheels
                

    def rover_Command_Msg (self, msg):

        self.throttle = msg.throttle 
        self.steering = self.steering_conversion(msg.steering)
        self.turn = msg.turn
        
    def steering_conversion(value):

        if value < -1 or value > 1:
            raise ValueError("Steering value must be between -1 and 1")

    # Linear interpolation between min and max radii
        return steering_lower_limit + (steering_upper_limit - steering_lower_limit) * (value + 1) / 2
   

    #Calculate the wheel speed based on the throttle, steering data.
    #You can add additional functions to help build this function up.
    #Note create a global variable for the width of the base for now and any other value for deminsiosns 
    #float throttle. Value between 0-1 
    #float sterring. Value between the max wheel angle and min wheel angle. 
    def calculateWheelSpeed(self, throttle, steering):

       if throttle < 0 or throttle > 1:
            raise ValueError("Throttle value must be between 0 and 1")
        
        # Wheel speed using Ackerman Steering Geometry (assuming wheel_speeds[0-2] = left, wheel_speeds[3-6] = right)
        for x in range(6):

            if (x < 3 and steering < 0) or (x >= 3 and steering > 0): # inner wheel (based on turn direction)
                self.wheel_speeds[x] = (baseLength - baseWidth/2 * math.tan(steering)) * (throttle*maxSpeed) / baseLength
            
            elif (x < 3 and steering > 0) or (x >= 3 and steering < 0): # outer wheel
                self.wheel_speeds[x] = (baseLength + baseWidth/2 * math.tan(steering)) * (throttle*maxSpeed) / baseLength

            else: # steering = 0
                self.wheel_speeds[x] = throttle * maxSpeed
    
    #Function for rotating in place.
    #Ensure wheels have been fully rotated 
    def rotateInPlace(self,trigger):
        
        pass
    
    #Completed later on 
    def applyWheelSpeeds(self,wheelSpeeds, encoderWheels):
        
        pass
    
    #Completed later on 
    def checkSafety():
        
        pass
    
    #Completed later on 
    def emergencyStop(self):
        
        pass
    
    #Completed later on 
    def monitorWheelEncoder(self):
        
        pass
