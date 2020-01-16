#!/usr/bin/env python
# encoding: utf-8
# Copyright (C) 2019 John Törnblom
'''
Publish a pose to a MAV
'''
import math
import optparse
import sys

import rospy as ros
import geometry_msgs.msg as msg

from tf.transformations import quaternion_from_euler


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

    topic = '%s/command/pose' % opts.namespace
        
    ros.init_node('mav_pose_publisher', anonymous=True)
    
    publisher = ros.Publisher(topic, msg.PoseStamped, queue_size=5)

    message = msg.PoseStamped()

    message.header.seq = 1
    message.header.stamp = ros.Time.now()
    message.header.frame_id = 'world'

    message.pose.position.x = float(args[0])
    message.pose.position.y = float(args[1])
    message.pose.position.z = float(args[2])

    x, y, z, w = quaternion_from_euler(0, 0, float(args[3])*math.pi/180)
    message.pose.orientation.x = x
    message.pose.orientation.y = y
    message.pose.orientation.z = z
    message.pose.orientation.w = w

    ros.sleep(1)
    publisher.publish(message)
    ros.sleep(1)

if __name__ == '__main__':
    main(sys.argv[1:])
