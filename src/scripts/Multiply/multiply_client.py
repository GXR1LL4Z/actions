import rospy
import actionlib
from actions.msg import MultiplyAction
from actions.msg import MultiplyGoal
class multiply_client:
    def __init__(self):
        #stworzenie clienta
        self.action_client = actionlib.SimpleActionClient('multiply', MultiplyAction)
        #czekanie na serwer, client zadziala tylko wtedy jak serwer bedzie dzialal
        self.action_client.wait_for_server()
        rospy.loginfo("Server has been detected")

    #glowan funkcja odpowiedzialna za wysyłanie goal-a
    def send_goal(self):
        #stworzenie zmiennej typu goal kt zostanie wyslana do servera
        goal = MultiplyGoal(a = 10, b = 10, wait_duration = 0.25)

        #wyslanie zmiennej goal do serwera i USTAWIENNIE FUNNKCJI ODPOWIEDZIALNYCH ZA SPRZEZENIA ZWROTE Z SERWERA
        self.action_client.send_goal(goal, done_cb = self.done_callback, feedback_cb = self.feedback_callback)
        
        
    def done_callback(self, status, result):
        rospy.loginfo("RECEIVED RESULT: "+str(result))
        rospy.loginfo("RECEIVED STATUS: "+str(status))
        
    def feedback_callback(self, feedback):
        rospy.loginfo("RECEIVED FEEDBACK: "+ str(feedback))
        

if __name__ == '__main__':
    rospy.init_node('count_until_client', anonymous = True)
    client = multiply_client()
    client.send_goal()
    rospy.spin()
