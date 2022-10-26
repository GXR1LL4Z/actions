import rospy
import actionlib                            #dzieki temu mozna robic Sipleaction
from actions.msg import CountUntilAction
from actions.msg import CountUntilGoal      #zmienna typu goal


class count_until_client:
    def __init__(self):
        self._action_client = actionlib.SimpleActionClient('/count_until', CountUntilAction)            #inicjhalizacja klienta
        self._action_client.wait_for_server()                                                           #czeka az serwer bedzie dzialal
        rospy.loginfo("Action server is up lets gooo")
        
    def send_goal(self):
        #potrzeba CountUntilGoal
        goal = CountUntilGoal(max_number = 7, wait_duration = 0.5)            #z gory narzucamy jakie parametry zostana wyslane
        
        self._action_client.send_goal(goal, done_cb = self.done_callback, feedback_cb = self.feedback_callback)
        rospy.loginfo("Goal has been sent")
        # rospy.sleep(2)
        # self._action_client.cancel_goal(goal)
        #dzieki funckja callback nie zawieszamy klienta w trakcie wykonywania operacji przez serwer, klient odwola sie do funkcji result i feedback jedynie jak serwer wysle wynik
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
