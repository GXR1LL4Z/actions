import rospy
import actionlib
from actions.msg import CountUntilAction
from actions.msg import CountUntilGoal



class count_until_client:
    def __init__(self):
        self._action_client = actionlib.SimpleActionClient('/count_until', CountUntilAction)
        self._action_client.wait_for_server()
        rospy.loginfo("Action server is up lets gooo")
        
    def send_goal(self):
        #potrzeba CountUntilGoal
        goal = CountUntilGoal(max_numberf = 20, wait_duration = 0.5)
        
        self._action_client.send_goal(goal, done_cb = self.done_callback, feedback_cb = self.feedback_callback)
        rospy.loginfo("Goal has been sent")
        # self._action_client.wait_for_result()
        # rospy.loginfo(self._action_client.get_result())
    
    def done_callback(self, status, result):
        rospy.loginfo("status is: " + str(status))
        rospy.loginfo("Result is: " + str(result))

    def feedback_callback(self, feedback):
        rospy.loginfo(feedback)


if __name__ == '__main__':
    rospy.init_node('count_until_client', anonymous = True)
    client = count_until_client()
    client.send_goal()
    rospy.spin()