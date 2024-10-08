import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # Define the path to your custom configuration file
    config_path = os.path.join(
        get_package_share_directory('kipp_sensors'),
        'config',
        'main_camera.yaml'
    )

    # Define the ZED wrapper node with your custom parameters
    zed_wrapper_node_main = Node(
        package='zed_wrapper',  # Replace with your package name if different
        executable='zed_wrapper',  # Replace with the correct executable name if different
        name='zed_node',  # You can rename your node if needed
        namespace='zed_main',  # Adjust the namespace as required
        parameters=[config_path],  # Path to your custom config file
        output='screen',
        #remappings=[('odom', 'kipp_camera_main_odom')]
    )

    zed_wrapper_node_back = Node(
        package='zed_wrapper',  # Replace with your package name if different
        executable='zed_wrapper',  # Replace with the correct executable name if different
        name='zed_node',  # You can rename your node if needed
        namespace='zed_back',  # Adjust the namespace as required
        parameters=[config_path],  # Path to your custom config file
        output='screen',
        remappings=[('odom', 'kipp_camera_map_odom')]
    )

    gps_node = Node(
            package='kipp_sensors',
            executable='gps_node',
            name='gps_node',
            output='screen',
        )
    
    save_gps_node = Node(
            package='kipp_sensors',
            executable='save_gps_node',
            name='save_gps_node',
            output='screen',
        )
    
    dummy_gps_node = Node(
            package='kipp_control',
            executable='dummy_gps',
            name='dummy_gps_node',
            output='screen',
        )


    # Return the LaunchDescription object
    return LaunchDescription([
        gps_node,
        save_gps_node,
        #dummy_gps_node,
        zed_wrapper_node_main
    ])