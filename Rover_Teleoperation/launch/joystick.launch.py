import launch
import launch_ros.actions

import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    return launch.LaunchDescription([
        launch_ros.actions.Node(
            package='joy',
            executable='joy_node',
            name='joy_node',
            parameters=[{
                'device_id': 0,
                'deadzone': 0.05,
                'autorepeat_rate': 20.0,
            }]
        ),

        launch_ros.actions.Node(
            package='teleop_twist_joy',
            executable='teleop_node',
            name='teleop_node',
            parameters=[
                {'axis_linear.x':1}, # left thumb stick vertical
                {'scale_linear.x':0.5},
                {'scale_linear_turbo.x':1.0},
                {'axis_angular.yaw':0}, # left thumb stick horizontal
                {'scale_angular.yaw':0.5},
                {'scale_angular_turbo.yaw':1.0},
                {'require_enable_button':False},
                {'enable_button':6}, # left shoulder button
                {'enable_turbo_button':7} # right shoulder button
            ]
        )
    ])