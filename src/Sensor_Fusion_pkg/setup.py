from setuptools import find_packages, setup

package_name = 'Sensor_Fusion_pkg'

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
    maintainer='floks',
    maintainer_email='gflokstr@ualberta.ca',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'fake_imu_publisher = Sensor_Fusion_pkg.SensorFusionNode:main' ######## Testing 
        ],
    },
)
