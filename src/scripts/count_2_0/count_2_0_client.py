from re import L
import rospy
import actionlib

from actions.msg import count_2_0Action
from actions.msg import count_2_0Goal

class count_client:
    def __init__(self):
        #stworzyc clienta 
        self.client = actionlib.SimpleActionClient('count_2_0', count_2_0Action)
        #zaczekac na serwer
        self.client.wait_for_server()
        rospy.loginfo("SERVER HAS BEEN DETECTED")
        
    def send_goal(self):
        #stworzyc zmeinna goal
        goal = count_2_0Goal(max_number = 20, wait_duration = 1)
        self.client.send_goal(goal, done_cb = self.done_callback, feedback_cb = self.feedback_callback)
        rospy.loginfo("GOAL HAS BEEN REQUESTED")        
    
    #funckcja obsugi feedbacku
    def feedback_callback(self, feedback):
        rospy.loginfo("RECEIVED FEEDBACK: "+ str(feedback.percentage*100)+"%")
    #funckja obsluigi rezultatu i statusu wykonaego dzialania
    def done_callback(self,status, result):
        rospy.loginfo("RECEIVED STATUS: "+ str(status))
        rospy.loginfo("RECEIVED: "+ str(result))

if __name__ == '__main__':
    rospy.init_node('count_client', anonymous=True)
    client = count_client()
    client.send_goal()
    rospy.spin()