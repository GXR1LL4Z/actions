import rospy
import actionlib

from actions.msg import count_2_0Action
from actions.msg import count_2_0Feedback
from actions.msg import count_2_0Result

class count_server:
    def __init__(self):
        #stworzyc serwer
        self.server = actionlib.SimpleActionServer('count_2_0',
        count_2_0Action,
        self.on_goal,
        auto_start=False)
        self.server.start()


    def on_goal(self, goal):
        pass
if __name__ == '__main__':
    rospy.init_node('count_server',anonymous=True)
    server = count_server()
    rospy.spin()