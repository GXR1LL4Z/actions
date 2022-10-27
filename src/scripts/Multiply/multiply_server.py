from re import A
import rospy
import actionlib

from actions.msg import MultiplyAction
from actions.msg import MultiplyGoal
from actions.msg import MultiplyFeedback
from actions.msg import MultiplyResult

class multiply_server:
    def __init__(self):
        #stworzenie servera
        self.action_server = actionlib.SimpleActionServer('multiply',
        MultiplyAction,
        self.on_goal,
        auto_start = False)
        #rozpoczecie pracy serwera
        self.action_server.start()
        rospy.loginfo("Server has been started")

    def on_goal(self, goal):
        rospy.loginfo("Goal has been received!")
        rospy.loginfo(goal)
        #odczyt warosci przesłanych przez clienta
        value_1 = goal.a
        value_2 = goal.b
        wait_duration = goal.wait_duration
        #czas czekania
        rate = rospy.Rate(1/wait_duration)
        #obsługa informacji zwortnych
        succes = False
        preemted = False
        #zmienne uzywane w mnozeniu 
        self.counter_1 = 1
        self.counter_2 = 1
        #zmienna tyu feedback
        self.feedback = MultiplyFeedback()        
        #petla wykonawcza
        #chce aby jako feedback byly zwracane operacje posrednie a jako wynika mnozenia dwoch danych liczb
        while not rospy.is_shutdown():
            if self.counter_1 < value_1:
                result_1 = value_2 * self.counter_1
                self.feedback.feedback_1 = result_1
            if self.counter_2 < value_2:
                result_2 = value_1 * self.counter_2
                self.feedback.feedback_2 = result_2 
            if self.action_server.is_preempt_requested():
                preemted = True
                break

            #publikowanie feedbacku
            self.action_server.publish_feedback(self.feedback)
            rate.sleep()
        result = MultiplyResult()
        result.result = value_1 * value_2
        if succes:
            self.action_server.set_succeeded(result)
        else:
            self.action_server.set_aborted()
        if preemted:
            self.action_server.set_preempted()

if __name__ == '__main__':
    rospy.init_node('multiply_server', anonymous = True)
    server = multiply_server()
    rospy.spin()
