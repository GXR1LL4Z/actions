from re import L
import rospy
import actionlib

from actions.msg import count_2_0Action
from actions.msg import count_2_0Goal

class count_client:
    def __init__(self):
        pass

    def send_goal(self):
        pass
if __name__ == '__main__':
    rospy.init_node('count_client', anonymous=True)
    client = count_client()
    client.send_goal()
    rospy.spin