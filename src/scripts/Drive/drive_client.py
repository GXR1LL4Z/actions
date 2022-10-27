import rospy
import actionlib

from actions.msg import DriveAction
from actions.msg import DriveGoal


class drive_client:
    def __init__(self):
        #stworzenie server
        self.action_client = actionlib.SimpleActionClient('drive', DriveAction)
        #zaczekaj na server
        self.action_client.wait_for_server()
        rospy.loginfo("serwer wstal, mozna dzialac")
    def send_goal(self):
        #stworzenie wiadomosci typu goal
        goal = DriveGoal(x_goal = 10, y_goal = 10)
        #wyslanie wiadomosci typu goal
        self.action_client.send_goal(goal, done_cb = self.done_callback, feedback_cb = self.feedback_callback)
        rospy.loginfo("GOAL HES BEEN SENT")
    def done_callback(self, status, result):
        rospy.loginfo("RECEIVED "+ str(result))
        rospy.loginfo("RECEIVED STATUS: "+ str(status))
    def feedback_callback(self, feedback):
        rospy.loginfo("RECEIVED "+str(feedback))



if __name__ == '__main__':
    rospy.init_node('drive_client', anonymous = True)
    client = drive_client()
    client.send_goal()
    rospy.spin()