## Getting started
Install one of the Ubuntu 18.04 desktop distribution (e.g. [xubuntu][xubuntu]).

Install ros-melodic-desktop-full:
```console
john@localhost:~$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
john@localhost:~$ sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' \
                                   --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
john@localhost:~$ sudo apt update
john@localhost:~$ sudo apt install ros-melodic-desktop-full
```
Setup ROS environment:
```console
john@localhost:~$ echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
john@localhost:~$ source /opt/ros/melodic/setup.bash
```
Install precompiled dependencies:
```console
john@localhost:~$ sudo apt-get install python-wstool python-catkin-tools protobuf-compiler \
                               libgoogle-glog-dev liblapacke-dev ros-melodic-octomap-ros \
                               ros-melodic-ompl ros-melodic-mavros ros-melodic-joy \
                               ros-melodic-mavlink ros-melodic-vrx-gazebo ros-melodic-mav-msgs
```
Fetch and compile source-based dependencies:
```console
john@localhost:~$ mkdir -p ws/src
john@localhost:~$ wget https://raw.githubusercontent.com/wara-ps/rotors_granso_scenarios/master/rosinstall.yaml -O ws/src/.rosinstall
john@localhost:~$ wstool update -t ws/src
john@localhost:~$ catkin build --workspace ws rotors_granso_scenarios
```
Launch Simulation:
```console
john@localhost:~$ source ws/devel/setup.bash
john@localhost:~$ roslaunch rotors_granso_scenarios mav_above_boat.launch
```
Wait for about 30 seconds before the drone starts to move arround.

![Preview of sample][preview]
![Download sample video][sample].

## Known Issues
- Compilation may sometimes fail due to insufficient amount of memory (8GB or more is recommended). Restarting the compilation often solves the problem.
- Visuals in Gazebo appears dark when running on PCs with Intel or AMD GPUs.
- Sometimes, simulation simply does not start and Gazebo is just black. Restarting simulation often solves the problem.

## Reporting Bugs
If you encounter problems with rotors_granso_scenarios, please [file a github issue](issues).
If you plan on sending pull requests which affect more than a few lines of code,
please file an issue before you start to work on you changes. This will allow us
to discuss the solution properly before you commit time and effort.

## License
Source code contained within this project is published under the [Apache 2.0 license][apl2].

[xubuntu]: http://ftp.lysator.liu.se/ubuntu-dvd/xubuntu/releases/18.04.4/release/xubuntu-18.04.4-desktop-amd64.iso
[apl2]: https://www.apache.org/licenses/LICENSE-2.0
[sample]: https://github.com/wara-ps/rotors_granso_scenarios/raw/master/videos/mav_above_boat.mp4
[preview]: https://github.com/wara-ps/rotors_granso_scenarios/raw/master/videos/mav_above_boat.png