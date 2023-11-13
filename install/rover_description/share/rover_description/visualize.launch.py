from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.substitutions import LaunchConfiguration, Command, PythonExpression
from ament_index_python.packages import get_package_share_directory
import os
import launch_ros
import launch

def print_debug_info(context):
    xacro_file_path = LaunchConfiguration('xacro_file_path').perform(context)
    print(f'Debug: xacro_file_path = {xacro_file_path}')
    
    generate_urdf_cmd = Command(['xacro ', xacro_file_path]).perform(context)
    print(f'Generated URDF:\n{generate_urdf_cmd}')


def generate_launch_description():
    # Package and XACRO file paths
    pkg_dir = get_package_share_directory('rover_description')
    xacro_file_path = os.path.join(pkg_dir, 'URDF', 'Components', 'wheel.xacro.urdf')
    
    # Declare launch arguments
    declare_xacro_file_path_cmd = DeclareLaunchArgument(
        'xacro_file_path',
        default_value=xacro_file_path,
        description='Path to wheel xacro file')
    declare_xacro_param_name_cmd = DeclareLaunchArgument(
        'name',
        default_value='wheel_name',
        description='Name parameter for the xacro file')

    # Convert XACRO to URDF with parameters
    robot_description = Command(
        ['xacro ', LaunchConfiguration('xacro_file_path')])

    # RViz Node
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        parameters=[{'robot_description': robot_description}]
    )

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description}]
    )
    joint_state_publisher_node = launch_ros.actions.Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        
    )
    return LaunchDescription([
        declare_xacro_file_path_cmd,
        OpaqueFunction(function=print_debug_info),
        joint_state_publisher_node,
        robot_state_publisher_node,
        rviz_node,
        
    ])
