#!/usr/bin/env python
# encoding: utf-8
# Copyright (C) 2019 John Törnblom
'''
Publish a goal to a drone
'''
import math
import optparse
import sys

import rospy as ros
import geometry_msgs.msg
import mav_planning_msgs.msg
import mav_planning_msgs.srv
import std_srvs.srv

from tf.transformations import quaternion_from_euler


class DroneAgent:
    pose_sub = None
    plan_proxy = None
    path_proxy = None
    pose = None
    
    def __init__(self, ns='firefly'):
        self.plan_proxy = ros.ServiceProxy('/%s/voxblox_rrt_planner/plan' % ns,
                                           mav_planning_msgs.srv.PlannerService)

        self.path_proxy = ros.ServiceProxy('/%s/voxblox_rrt_planner/publish_path' % ns,
                                           std_srvs.srv.Empty)

        self.pose_sub = ros.Subscriber('/%s/ground_truth/pose' % ns,
                                       geometry_msgs.msg.Pose, self.on_current_pose)
        
    def on_current_pose(self, pose):
        self.pose_sub.unregister()
        self.pose_sub = None
        self.pose = pose
    
    def plan_and_publish(self, x, y, z, w):
        while self.pose is None:
            ros.sleep(1)
            if ros.is_shutdown():
                return False

        start = geometry_msgs.msg.PoseStamped()
        goal = geometry_msgs.msg.PoseStamped()

        start.pose = self.pose
        
        goal.pose.position.x = x
        goal.pose.position.y = y
        goal.pose.position.z = z

        x, y, z, w = quaternion_from_euler(0, 0, z*math.pi/180)
        goal.pose.orientation.x = x
        goal.pose.orientation.y = y
        goal.pose.orientation.z = z
        goal.pose.orientation.w = w
        
        res = self.plan_proxy(start_pose=start, goal_pose=goal)
        if res.success:
            self.path_proxy()

        return res.success

        
def main(args):
    parser = optparse.OptionParser(usage="%prog [options] x y z yaw")
    
    parser.set_description(__doc__.strip())

    parser.add_option('-n', dest='namespace', action='store',
                      metavar='STRING', help='set namespace to STRING (default to firefly)',
                      default='firefly')

    (opts, args) = parser.parse_args(args)
    if len(args) < 4:
        parser.print_help()
        sys.exit(1)

    args = [float(value) for value in args]
     
    ros.init_node('goal_publisher', anonymous=True)

    try:
        agent = DroneAgent()
        agent.plan_and_publish(*args)
    except Exception as e:
        print e
        
    ros.sleep(1)


if __name__ == '__main__':
    main(sys.argv[1:])
