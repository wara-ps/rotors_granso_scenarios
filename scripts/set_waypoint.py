#!/usr/bin/env python
# encoding: utf-8
# Copyright (C) 2019 John Törnblom
'''
Publish a waypoint to a drone
'''

import optparse
import sys

import rospy as ros
import geometry_msgs.msg as msg


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
    
    ros.init_node('mission_publisher', anonymous=True)
    
    publisher = ros.Publisher('/%s/waypoint' % opts.namespace, msg.PoseStamped,
                              queue_size=5)

    message = msg.PoseStamped()

    message.header.seq = 1
    message.header.stamp = ros.Time.now()
    message.header.frame_id = 'world'

    message.pose.position.x = float(args[0])
    message.pose.position.y = float(args[1])
    message.pose.position.z = float(args[2])

    message.pose.orientation.x = 0.0
    message.pose.orientation.y = 0.0
    message.pose.orientation.z = 0.0
    message.pose.orientation.w = float(args[3])

    ros.sleep(1)
    publisher.publish(message)
    ros.sleep(1)

if __name__ == '__main__':
    main(sys.argv[1:])
