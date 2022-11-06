import rospy
import actionlib

from actions.msg import CountUntilAction
from actions.msg import CountUntilFeedback
from actions.msg import CountUntilGoal
from actions.msg import CountUntilResult

class count_server:
    def __init__(self):
        #create a server
        self.action_server = actionlib.ActionServer('count_action', 
        CountUntilAction, 
        self.on_goal, 
        self.on_cancel,
        auto_start = False)
        self.action_server.start()
        rospy.loginfo("SERVER HAS BEEN STARTED")
        

    def process_goal(self, goal_handle):
        rospy.loginfo("PROCESSING THE GOAL")
        goal = goal_handle.get_goal()
        max_number = goal.max_number
        wait_duration = goal.wait_duration
        #Now goal is in the PENDING state, we need to accept or reject
        #the goal cannot be set_succeded fromthis state - NEVER

        #Validate the goal
        if wait_duration > 1000:
            goal_handle.set_rejected()
            return
        elif max_number >10000:
            goal_handle.set_rejected()
            return
        else:
            goal_handle.set_accepted
        
        #parameters
        counter = 0
        rate = rospy.Rate(1.0/wait_duration)

        #flags
        succes = False
        preempted = False

        #loop
        while not rospy.is_shutdown():
            counter += 1
            rospy.loginfo(counter)
            if counter >= max_number:
                succes = True
                break
            

    def on_goal(self, goal_handle):
        rospy.loginfo("RECEIVED A NEW GOAL: "+str(goal_handle))
        #wydrukowalo jakis syf tu nir ma tak łatwo



    def on_cancel(self, cancel_req):
        rospy.loginfo("RECEIVED CANCEL REQUEST")

if __name__ == '__main__':
    rospy.init_node('count_server', anonymous = True)
    server_ = count_server()
    rospy.spin()