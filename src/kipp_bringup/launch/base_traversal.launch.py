import os

from ament_index_python.packages import get_package_share_directory
import launch
from launch.actions import SetEnvironmentVariable
from launch_ros.actions import Node, ComposableNodeContainer
from launch_ros.descriptions import ComposableNode

def generate_launch_description():


    joy_node = Node(
            package='joy',
            executable='joy_node',
            name='joy_node',
            output='screen',
            emulate_tty=True,
            parameters=[{'autorepeat_rate': 20.0}, {'deadzone': 0.1}],
            namespace='manual',
        )
    

    return launch.LaunchDescription([
        SetEnvironmentVariable(name='RCUTILS_COLORIZED_OUTPUT', value='1'),
        joy_node
    ])

if __name__ == '__main__':
    generate_launch_description()