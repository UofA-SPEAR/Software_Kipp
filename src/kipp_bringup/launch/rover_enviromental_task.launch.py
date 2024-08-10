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
            name='gps_node_rover',
            output='screen',
            emulate_tty=True,
        )
    #------------------Camera----------------------------------

    kipp_photgraph = Node(
            package='kipp_camera',
            executable='photographer_node',
            name='photo_node',
            output='screen',
            emulate_tty=True,
    )

    #--------------Arm Node------------------------

    kipp_arm_can = Node(
            package='kipp_arm_encoder',
            executable='kipp_arm_can',
            name='kipp_arm_can',
            output='screen',
            emulate_tty=True,
    )

    kipp_arm_can = Node(
            package='kipp_arm_encoder',
            executable='kipp_arm_gripper',
            name='kipp_arm_can',
            output='screen',
            emulate_tty=True,
    )

    return launch.LaunchDescription([
        SetEnvironmentVariable(name='RCUTILS_COLORIZED_OUTPUT', value='1'),
        kipp_can_node,
        kipp_arm_can,
        xbox_contol_node,
        gps_node,
        #kipp_photgraph
    ])

if __name__ == '__main__':
    generate_launch_description()