import os

from ament_index_python.packages import get_package_share_directory
import launch
from launch.actions import SetEnvironmentVariable
from launch_ros.actions import Node, ComposableNodeContainer
from launch_ros.descriptions import ComposableNode

def generate_launch_description():
    
    #--------------------Drive Nodes ---------------------------

    joy_node = Node(
            package='joy',
            executable='joy_node',
            name='joy_node',
            output='screen',
            emulate_tty=True,
            parameters=[{'autorepeat_rate': 20.0}, {'deadzone': 0.1}],
            namespace='manual',
        )

    #--------------------GPS Node------------------------------

    gps_record = Node(
            package='kipp_gps',
            executable='gps_record',
            name='gps_record',
            output='screen',
            emulate_tty=True,
        )
    
    #--------------------ARM Node--------------------------------

    arm_node = Node(
        package='kipp_arm_encoder',
        executable='kipp_arm_calibrate',
        name='kipp_arm_calibrate',
        output='screen',
    )



    return launch.LaunchDescription([
        SetEnvironmentVariable(name='RCUTILS_COLORIZED_OUTPUT', value='1'),
        #gps_record,
        joy_node,
        # arm_node

    ])

if __name__ == '__main__':
    generate_launch_description()