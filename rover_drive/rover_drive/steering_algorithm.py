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

class DriveControl(Node):

# """
# Intialize
# Subscribers 
# 1.Throttle Value 
# 2.Steering Value 
# 3.Trigger value 
# 4.GUI E-Stop Commnad 
# 5.Encoder data 

# Publisher:
# Wheel speed Values   



# """
   
    def __init__(self):
        pass

    def drive_control_main(self):
        pass
   
    def getThrottle(self, joyData):
        pass
    
    def getSteering(self, joyData):
        pass
    
    def getTriggerValue(self, joyData):
        pass

    def calculateWheelSpeed(self, throttle, steering):
        pass

    def rotateInPlace(self,trigger):
        pass

    def applyWheelSpeeds(self,wheelSpeeds):
        pass

    def checkSafety():
        pass

    def applyWheelSpeeds(self,wheelSpeeds): 

        pass

    def checkSafety(self):

        pass

    def emergencyStop(self):

        pass

    def monitorWheelEncoder(self):
        
        pass





    
    

