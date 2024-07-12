#!/usr/bin/env python3
from pylimo import limo
import rospy
from ackermann_msgs.msg import AckermannDrive
import time
import numpy as np

class listener:
    def __init__(self):
        self.data = None

    def callback(self, data):
        self.data = data

    def listener(self):
        rospy.init_node("vs_listener", anonymous=True)
        rospy.Subscriber("vel_steer_limo780", AckermannDrive, self.callback)


if __name__ == '__main__':
    listener_ins = listener()
    limo= limo.LIMO()
    limo.EnableCommand()
    limo.SetMotionCommand(linear_vel=0, steering_angle=0)
    time.sleep(1)
    steering_angle = np.zeros(250)
    iter = 0 
    previous_steering = -6000 #arbitrary number
    while True:
        listener_ins.listener()
        if listener_ins.data is not None:
            if previous_steering == listener_ins.data.steering_angle:
                print("it is possible the mocap stopped updating, double check and run again")
                limo.SetMotionCommand(linear_vel=0, steering_angle=0)
                break
            listener_ins.data.speed
            limo.SetMotionCommand(linear_vel=listener_ins.data.speed, steering_angle=listener_ins.data.steering_angle)
            print("Velocity: ", listener_ins.data.speed, "Steering: ", listener_ins.data.steering_angle)
            iter += 1
            if iter > 5:
                previous_steering = listener_ins.data.steering_angle
                iter = 0
            time.sleep(0.1)
        else:
            print("[WARNING] Not receiving ROS messages")
            time.sleep(1)
            limo.SetMotionCommand(linear_vel=0, steering_angle=0)
            if iter>10:
                break