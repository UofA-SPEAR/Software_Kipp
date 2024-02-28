# Copyright (c) 2018 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.conditions import IfCondition
from nav2_common.launch import RewrittenYaml


def generate_launch_description():
    # Get the launch directory
    rviz_dir = get_package_share_directory('kipp_description')
    camera_dir = get_package_share_directory('kipp_camera')
    nav_gps_dir = get_package_share_directory('nav2_gps_waypoint_follower_demo')
    rviz_launch_dir = os.path.join(rviz_dir, 'launch')
    camera_launch_dir = os.path.join(camera_dir, 'launch')
    nav_gps_launch_dir = os.path.join(nav_gps_dir, 'launch')


    
    # bringup_dir = get_package_share_directory('nav2_bringup')
    # gps_wpf_dir = get_package_share_directory(
    #     "nav2_gps_waypoint_follower_demo")
    # launch_dir = os.path.join(gps_wpf_dir, 'launch')
    # params_dir = os.path.join(gps_wpf_dir, "config")
    # nav2_params = os.path.join(params_dir, "nav2_no_map_params.yaml")
    # configured_params = RewrittenYaml(
    #     source_file=nav2_params, root_key="", param_rewrites="", convert_types=True
    # )
    rviz_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(rviz_launch_dir, 'display.launch.py'))
    )

    camera_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(camera_launch_dir, 'kipp_camera.launch.py'))
    )

    nav_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(nav_gps_launch_dir, 'gps_waypoint_follower.launch.py'))
    )

    # Create the launch description and populate
    ld = LaunchDescription()

    ld.add_action(rviz_cmd)
    ld.add_action(camera_cmd)
    ld.add_action(nav_cmd)

    return ld
