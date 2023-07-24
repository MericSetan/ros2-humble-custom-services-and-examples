from setuptools import setup

package_name = 'custom_service_examples'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mrc_stn',
    maintainer_email='setan.meric@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        "my_server = custom_service_examples.custom_service_server:main",
        "my_client = custom_service_examples.custom_service_client:main"
        ],
    },
)
