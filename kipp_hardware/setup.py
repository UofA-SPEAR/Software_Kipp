from setuptools import find_packages, setup
from glob import glob
from setup import setup
import os

package_name = 'kipp_hardware'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*.launch.py'))),
        (os.path.join('share', package_name, 'config'), glob(os.path.join('config', '*.yaml')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Induwara Kandapahala',
    maintainer_email='kandapah@ualberta.ca',
    description='Hardware Interface for our Rover. Currently includes both Zed Cameras, GPS Module and Can communication',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'can_node = kipp_hardware.kipp_can_drive:main'
            'xbox_node = kipp_hardware.xbox_controller_node:main'
        ],
    },
)
