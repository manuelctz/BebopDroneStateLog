#!/usr/bin/pyhton
import rospy
from geometry_msgs.msg import PoseStamped
import math


class BebopState():

    def __init__(self):
        self.node = rospy.init_node("State_logger",anonymous=True)#initiate node
        self.pose_subscriber = rospy.Subscriber("vrpn_client_node/Drone1/pose", PoseStamped,self.get_pose)#sub to topic
        self.log_file = open("Drone_States.csv", "w") #create logger file
        self.rate = rospy.Rate(10)#10hz
        self.pos_x = None
        self.pos_y = None
        self.pos_z = None
        self.roll = None
        self.pitch = None
        self.yaw = None

    def get_pose(self, data):
        self.pos_x = self.truncate(data.pose.position.x, 3)
        self.pos_y = self.truncate(data.pose.position.z, 3) #switch y-z coordinates
        self.pos_z = self.truncate(data.pose.position.y, 3) #from OptiTrack system
        ori_x = data.pose.orientation.x
        ori_y = data.pose.orientation.y
        ori_z = data.pose.orientation.z
        ori_w = data.pose.orientation.w

        self.roll, self.pitch, self.yaw = self.quaternion_to_euler_angle(ori_w, ori_x, ori_y, ori_z)

        self.roll = self.truncate(self.roll, 3)
        self.pitch = self.truncate(self.pitch, 3)
        self.yaw = self.truncate(self.yaw, 3)

        str_val = '{}, {}, {}, {}, {}, {}\n'.format(self.pos_x, self.pos_y, self.pos_z, self.roll, self.pitch, self.yaw)
        self.log_file.write(str_val) #write the drone state into the log file



    def quaternion_to_euler_angle(self, w, x, y, z):
        ysqr = y * y

        t0 = +2.0 * (w * x + y * z)
        t1 = +1.0 - 2.0 * (x * x + ysqr)
        X = math.degrees(math.atan2(t0, t1))

        t2 = +2.0 * (w * y - z * x)
        t2 = +1.0 if t2 > +1.0 else t2
        t2 = -1.0 if t2 < -1.0 else t2
        Y = math.degrees(math.asin(t2))

        t3 = +2.0 * (w * z + x * y)
        t4 = +1.0 - 2.0 * (ysqr + z * z)
        Z = math.degrees(math.atan2(t3, t4))
        return X, Y, Z

    def truncate(self, number, digits):
        stepper = pow(10.0,digits)
        return math.trunc(stepper*number)/stepper

    def sample_data(self):
        for i in range(2):
            self.rate.sleep()
        return self.pos_x, self.pos_y, self.pos_z, self.roll, self.pitch, self.yaw


if __name__ == "__main__":
    test = BebopState()
    #x, y, z, r, p, w = test.sampleData() #get a drone state to close the control loop and get current state
    #print(x, y, z, r, p, w)
    rospy.spin()
    print("File executed directly")

else:
    # when module is called from another python script
    drone = BebopState()
    rospy.spin()
