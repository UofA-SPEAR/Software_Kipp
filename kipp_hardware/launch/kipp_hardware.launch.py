from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    config_path_main = os.path.join(
        get_package_share_directory('kipp_camera'),
        'config',
        'main_camera.yaml'
    )

    config_path_back = os.path.join(
        get_package_share_directory('kipp_camera'),
        'config',
        'back_camera.yaml'
    )

    return LaunchDescription([
       
        Node(
            package='kipp_hardware',
            executable='kipp_can_drive',
            name='kipp_can_drive',
            output='screen',
            emulate_tty=True,
        ),
        # Node(
        #     package='kipp_hardware',
        #     executable='gps_serial',
        #     name='gps',
        #     output='screen',
        #     emulate_tty=True,
        # ),

    #     Node(
    #     package='zed_wrapper',  # Replace with your package name if different
    #     executable='zed_wrapper',  # Replace with the correct executable name if different
    #     name='zed_node',  # You can rename your node if needed
    #     namespace='zed_main',  # Adjust the namespace as required
    #     parameters=[config_path_main],  # Path to your custom config file
    #     output='screen',
    #     #remappings=[('odom', 'kipp_camera_main_odom')]
    # ),

    #     Node(
    #     package='zed_wrapper',  # Replace with your package name if different
    #     executable='zed_wrapper',  # Replace with the correct executable name if different
    #     name='zed_node',  # You can rename your node if needed
    #     namespace='zed_back',  # Adjust the namespace as required
    #     parameters=[config_path_back],  # Path to your custom config file
    #     output='screen',
    #     remappings=[('odom', 'kipp_camera_map_odom')]
    # )
    ])