from setuptools import setup

package_name = 'my_py_pkg'

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
    maintainer='jishnu',
    maintainer_email='jishnusurajila@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "my_node = my_py_pkg.my_first_node:main",
            "my_oops_node = my_py_pkg.py_node_oops:main",
<<<<<<< HEAD
            "robot_news_station = my_py_pkg.robot_news_station:main",
            "smartphone = my_py_pkg.smartphone:main"
=======
            "robot_news_station = my_py_pkg.robot_news_station:main"
>>>>>>> 874f3ef (setup: added executable to the robot news publisher)
        ],
    },
)
