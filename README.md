## Getting started
Install one of the Ubuntu 18.04 desktop distribution (e.g. [xubuntu][xubuntu]).

Install ros-melodic-desktop-full:
```console
    $ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
    $ sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' \
                       --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
    $ sudo apt update
    $ sudo apt install ros-melodic-desktop-full
```
Setup ROS environment:
```console
    $ sudo rosdep init
    $ rosdep update
    $ echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
    $ source /opt/ros/melodic/setup.bash
```
Install precompiled dependencies:
```console
    $ sudo apt-get install python-wstool python-catkin-tools protobuf-compiler \
                           libgoogle-glog-dev liblapacke-dev ros-melodic-octomap-ros \
                           ros-melodic-ompl ros-melodic-mavros ros-melodic-joy \
                           ros-melodic-mavlink
```
Fetch and compile source-based dependencies:
```console
    $ mkdir -p ws/src
    $ wget https://git.io/Jerwk -O ws/src/.rosinstall
    $ wstool update -t ws/src
    $ catkin build --workspace ws
```
Launch Simulation:
```console
    $ source ws/devel/setup.bash
    $ roslaunch rotors_granso_scenarios hovering.launch
```

Set waypoint (in new terminal window):
```console
    $ source ws/devel/setup.bash
    $ python ws/src/rotors_granso_scenarios/scripts/set_waypoint.py -h
        Usage: set_waypoint.py [options] x y z yaw

        Publish a waypoint to a drone

        Options:
          -h, --help  show this help message and exit
          -n STRING   set namespace to STRING (default to firefly)
          -c          bypass planner and send waypoint directly to controller

    $ python ws/src/rotors_granso_scenarios/scripts/set_waypoint.py 55 55 5 310 -c
```


## Reporting Bugs
TBD

## License
TBD

[xubuntu]: http://ftp.lysator.liu.se/ubuntu-dvd/xubuntu/releases/18.04/release/xubuntu-18.04-desktop-amd64.iso