import os

from ament_index_python.packages import get_package_share_directory

import launch
from launch.actions import SetEnvironmentVariable
from launch_ros.actions import Node, ComposableNodeContainer
from launch_ros.descriptions import ComposableNode

def generate_launch_description():
    #---------------------CAMERA NODES ------------------------
    
    decoder_node = ComposableNode(
        name='decoder',
        package='isaac_ros_h264_decoder',
        plugin='nvidia::isaac_ros::h264_decoder::DecoderNode',
        remappings=[
            ('image_compressed', 'left/image_compressed')
        ])
    

    container = ComposableNodeContainer(
        name='decoder_container',
        namespace='',
        package='rclcpp_components',
        executable='component_container_mt',
        composable_node_descriptions=[decoder_node],
        output='screen',
        arguments=['--ros-args', '--log-level', 'info']
    )

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
    


    return launch.LaunchDescription([
        SetEnvironmentVariable(name='RCUTILS_COLORIZED_OUTPUT', value='1'),
        container,
        joy_node
        
    ])

if __name__ == '__main__':
    generate_launch_description()