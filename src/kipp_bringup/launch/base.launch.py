import os

from ament_index_python.packages import get_package_share_directory
import launch
from launch.actions import SetEnvironmentVariable
from launch_ros.actions import Node, ComposableNodeContainer
from launch_ros.descriptions import ComposableNode

def generate_launch_description():
    #---------------------CAMERA NODES ------------------------
    
    h264_msgs_packet_node = Node(
        name='h264_converter_node',
        package='isaac_ros_to_h264_msgs_packet',
        executable='ToH264MsgsPacket',
        remappings=[
            ('image_compressed', 'left/image_compressed'),
            ('image_raw/compressed', 'image_raw/h264')
        ],
        output='screen'
    )

    republish_node = Node(
        name='republish_node',
        package='image_transport', 
        executable='republish',  
        arguments=['h264',  'raw'], 
        remappings=[                
            ('in/h264', 'image_raw/h264'),
        ],
        output='screen'
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
        #h264_msgs_packet_node,
        #republish_node,
        joy_node
        
    ])

if __name__ == '__main__':
    generate_launch_description()