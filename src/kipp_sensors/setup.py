from setuptools import find_packages, setup

package_name = 'kipp_sensors'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml'])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ayden',
    maintainer_email='aydenbravender@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'gps_node = kipp_sensors.gps_node:main',
            'save_gps_node = kipp_sensors.save_gps_node:main',
            'random_gps_node = kipp_sensors.Random_gps:main', # remove this line when interfacing actually gps
        ],
    },
)
