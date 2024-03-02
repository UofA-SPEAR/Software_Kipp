from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='joy',
            executable='joy_node',
            name='joy_node',
            output='screen',
            emulate_tty=True,
            parameters=[{'autorepeat_rate': 20.0}, {'deadzone': 0.1}],
            namespace='manual',
        ),
    ])