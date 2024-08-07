import launch
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode


def generate_launch_description():
    """Launch the H.264 Decoder Node."""
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

    return (launch.LaunchDescription([container]))