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
    $ wget https://gitlab.liu.se/johto84/rotors_granso_scenarios/raw/master/rosinstall.yaml \
           -O ws/src/.rosinstall
    $ wstool update -t ws/src
    $ catkin build --workspace ws rotors_simulator mav_voxblox_planning
```
Run Scenario:
```console
    $ source ws/devel/setup.bash
    $ roslaunch mav_local_planner firefly_sim.launch
```

## Reporting Bugs
TBD

## License
TBD

[xubuntu]: http://ftp.lysator.liu.se/ubuntu-dvd/xubuntu/releases/18.04/release/xubuntu-18.04-desktop-amd64.iso