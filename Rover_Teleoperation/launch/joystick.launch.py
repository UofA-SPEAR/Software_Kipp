from launch import LaunchDescription
from launch_ros.actions import Node

import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    joy_params = os.path.join(get_package_share_directory('Rover_Teleoperation'),'config','joystick.yaml') 
    # getting parameters for the joystick from the .yaml file, just easier this way since you dont have to retype every param

    joy_node = Node(
        package='joy',
        executable='joy_node',
        parameters=[joy_params],
    )

    teleop_node = Node(
        package='teleop_twist_joy',
        executable='teleop_node', 
        name='teleop_node',
        parameters=[joy_params],
        remappings=[('/cmd_vel', '/diff_cont/cmd_vel_unstamped')]
    )

    return LaunchDescription([
        joy_node,
        teleop_node
    ])  

    