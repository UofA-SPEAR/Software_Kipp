import os

from ament_index_python.packages import get_package_share_directory

import launch
from launch.actions import SetEnvironmentVariable
from launch_ros.actions import Node, ComposableNodeContainer
from launch_ros.descriptions import ComposableNode

def generate_launch_description():
    # Path to the configuration file
    config_path_main = os.path.join(
        get_package_share_directory('kipp_hardware'),
        'config',
        'main_camera.yaml'
    )

    # Define the ZED main node
    zedmain_node = Node(
        package='zed_wrapper',  # Replace with your package name if different
        executable='zed_wrapper',  # Replace with the correct executable name if different
        name='zed_node',  # Node name
        namespace='zed_main',  # Namespace for the node
        parameters=[config_path_main],  # Path to your custom config file
        output='screen',
    )

    # Define the left format converter node
    zedmain_format_converter_node = ComposableNode(
        package='isaac_ros_image_proc',
        plugin='nvidia::isaac_ros::image_proc::ImageFormatConverterNode',
        name='image_format_node_left',
        parameters=[{
            'encoding_desired': 'rgb8',
        }],
        remappings=[
            ('image_raw', '/zed_main/zed_node/left/image_rect_color'),
            ('image', 'left/image_rect_raw')
        ]
    )

    # Define the encoder node
    zedmain_encoder_node = ComposableNode(
        package='isaac_ros_h264_encoder',
        plugin='nvidia::isaac_ros::h264_encoder::EncoderNode',
        name='left_encoder_node',
        parameters=[{
            'input_width': 1280,
            'input_height': 720,
        }],
        remappings=[
            ('image_raw', 'left/image_rect_raw'),
            ('image_compressed', 'left/image_compressed')
        ]
    )

    # Container to hold the composable nodes
    container = ComposableNodeContainer(
        name='encoder_container',
        namespace='encoder',
        package='rclcpp_components',
        executable='component_container_mt',
        composable_node_descriptions=[zedmain_format_converter_node, zedmain_encoder_node],
        output='screen'
    )

    return launch.LaunchDescription([
        SetEnvironmentVariable(name='RCUTILS_COLORIZED_OUTPUT', value='1'),
        zedmain_node,
        container
    ])

if __name__ == '__main__':
    generate_launch_description()
