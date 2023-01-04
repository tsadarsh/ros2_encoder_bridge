from setuptools import setup

package_name = 'ros2_encoder_bridge'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tsadarsh',
    maintainer_email='tsadarsh0707@gmail.com',
    description='Publishes encoder ticks form Arduino Nano using Serial Protocol',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'encoder_publisher = ros2_encoder_bridge.encoder_publisher:main',
        ],
    },
)
