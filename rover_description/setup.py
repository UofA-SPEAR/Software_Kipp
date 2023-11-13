from setuptools import find_packages, setup

package_name = 'rover_description'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/URDF/Components', ['URDF/Components/wheel.xacro.urdf']),
        ('share/' + package_name + '/URDF/Components', ['URDF/Components/rocker.xacro.urdf']),
        ('share/' + package_name + '/URDF/Components', ['URDF/Components/bogie.xacro.urdf']),
        ('share/' + package_name, ['launch/visualize.launch.py'])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Induwara',
    maintainer_email='kandapah@ualberta.ca',
    description='Rover Description file, including URDF XACRO Files and full assembly of various configurations',
    license='',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
