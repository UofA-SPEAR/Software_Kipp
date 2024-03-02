from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Node(
        #     package='joy',
        #     executable='joy_node',
        #     name='joy_node',
        #     output='screen',
        #     emulate_tty=True,
        #     parameters=[{'autorepeat_rate': 20.0}, {'deadzone': 0.1}],
        #     namespace='manual',
        # ),
        Node(
            package='kipp_control',
            executable='xbox_node',
            name='xbox_node',
            namespace='manual',
            output='screen',
            emulate_tty=True,
        ),
        Node(
            package='kipp_control',
            executable='can_node',
            namespace='manual',
            name='can_node',
            output='screen',
            emulate_tty=True,
        ),
    ])
