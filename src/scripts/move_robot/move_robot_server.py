import rospy
import actionlib

from actions.msg import move_robotAction
from actions.msg import move_robotFeedback
from actions.msg import move_robotResult


class Server:
    def __init__(self):
        self.server = actionlib.SimpleActionServer('move_robot', 
        move_robotAction, 
        self.on_goal, 
        auto_start=False)
        self.server.start()
        rospy.loginfo("SERVER HAS BEEN STARTED")

    def on_goal(self, goal):
        rospy.loginfo("RECEIVED: "+ str(goal))
        self.goal_position = goal.goal_position
        self.velocity = goal.velocity
        self.position = 0
        rate = rospy.Rate(self.velocity)

        #flagi
        succes = False
        preempted = False

        #zmienna typu feedback
        feedback = move_robotFeedback()

        while not rospy.is_shutdown():
            
            if self.server.is_preempt_requested:
                preempted = True
                break
            if self.position >= self.goal_position:
                succes = True
                break
            if self.position < self.goal_position: 
                self.position = self.position + 1
                feedback.current_position = self.position
                self.server.publish_feedback(feedback)
                rate.sleep()

            result = move_robotResult()
            result.reached_position = self.position
            if succes:
                result.message = "The goal has been achived"
                self.server.set_succeeded(result)
            elif preempted:
                result.message = "The procces has been preemted"
                self.server.set_preempted(result)
            else:
                result.message = "ERROR"
                self.server.set_aborted(result)

if __name__ == '__main__':
    rospy.init_node('move_robot_server', anonymous = True)
    server = Server()