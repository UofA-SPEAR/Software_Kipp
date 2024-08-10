import os

from ament_index_python.packages import get_package_share_directory
import launch
from launch.actions import SetEnvironmentVariable
from launch_ros.actions import Node, ComposableNodeContainer
from launch_ros.descriptions import ComposableNode

def generate_launch_description():
    
    #--------------------Drive Nodes ---------------------------

    kipp_can_node = Node(
            package='kipp_hardware',
            executable='can_node',
            name='kipp_can_drive',
            output='screen',
            emulate_tty=True,
        )
    
    xbox_contol_node = Node(
            package='kipp_hardware',
            executable='xbox_node',
            name='can_node',
            output='screen',
            emulate_tty=True,
        )
    
    #--------------------GPS Node------------------------------

    gps_node = Node(
            package='kipp_hardware',
            executable='gps_node',
            name='can_node',
            output='screen',
            emulate_tty=True,
        )


    return launch.LaunchDescription([
        SetEnvironmentVariable(name='RCUTILS_COLORIZED_OUTPUT', value='1'),
        #zedmain_node,
        xbox_contol_node,
        kipp_can_node,
        #gps_node
    ])

if __name__ == '__main__':
    generate_launch_description()