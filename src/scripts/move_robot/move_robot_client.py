import rospy
import actionlib

from actions.msg import move_robotAction
from actions.msg import move_robotGoal

class client:
    def __init__(self):
        self.client = actionlib.SimpleActionClient('move_robot', move_robotAction)
        self.client.wait_for_server()
        rospy.loginfo("SERVER HAS BEEN DETECTED")
    
    def send_goal(self):
        goal = move_robotGoal(velocity = 1, goal_position = 100)
        self.client.send_goal(goal, done_cb = self.done_callback, feedback_cb = self.feedback_callback)
        rospy.loginfo("GOAL HAS BEEN SENT")

    def done_callback(self, status, result):
        rospy.loginfo("RECEIVED STATUS: "+ str(status))
        rospy.loginfo("RECEIVED: "+ str(result))

    def feedback_callback(self, feedback):
        rospy.loginfo("RECEIVED CURRENT POSITION: "+ str(feedback))

if __name__ == '__main__':
    rospy.init_node('move_robot_client', anonymous = True)
    client_ = client()
    client_.send_goal()
    rospy.spin()
