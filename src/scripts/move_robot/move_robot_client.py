import rospy
import actionlib

from actions.msg import move_robotAction
from actions.msg import move_robotGoal

class client:
    def __init__(self):
        pass

if __name__ == '__main__':
    rospy.init_node('move_robot_client', anonymous = True)