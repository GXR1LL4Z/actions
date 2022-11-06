import rospy
import actionlib

from actions.msg import CountUntilAction
from actions.msg import CountUntilFeedback
from actions.msg import CountUntilGoal
from actions.msg import CountUntilResult

class count_client:
    def __init__(self):
        pass

if __name__ == '__main__':
    rospy.init_node('count_client', anonymous = True)
    client_ = count_client()