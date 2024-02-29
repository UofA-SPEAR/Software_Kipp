from setuptools import find_packages, setup

package_name = 'kipp_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='smart',
    maintainer_email='kandapah@ualberta.ca',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'gps_node = kipp_control.kipp_gps:main',
            'dummy_gps = kipp_control.dummy_gps:main',
            'xbox_node = kipp_control.xbox_controller_node:main',
            'can_node = kipp_control.kipp_can_drive:main'
        ],
    },
)
