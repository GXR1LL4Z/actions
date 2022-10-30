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
        #wystartowac serwe
        self.server.start()
        rospy.loginfo("SERWER HAS BEEN STARTED")
        
    def on_goal(self, goal):
        #wyswietlenie otzrymanego goala
        rospy.loginfo("GOAL HAS BEEN RECEIVED: " + str(goal))
        max_number = goal.max_number
        wait_duration = goal.wait_duration
        #czas spania
        rate = rospy.Rate(1/wait_duration)
        counter = 0
        #flagi
        succes = False
        preemted = False
        #feedback
        feedback  = count_2_0Feedback()
        while not rospy.is_shutdown:
            counter += counter
            if counter == max_number:
                succes = True
                break
            if self.server.is_preempt_requested():
                preemted = True
                break
            feedback = float(counter)/float(max_number)
            self.server.publish_feedback(feedback)
            rate.sleep()
        result = count_2_0Result()
        result = counter
        if succes:
            self.server.set_succeeded(result)
        elif preemted:
            self.server.set_preempted(result)
        else:
            self.server.set_aborted(result)

if __name__ == '__main__':
    rospy.init_node('count_server',anonymous=True)
    server = count_server()
    rospy.spin()