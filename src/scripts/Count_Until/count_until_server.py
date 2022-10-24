import rospy
import actionlib
from actions.msg import CountUntilAction
from actions.msg import CountUntilGoal
from actions.msg import CountUntilResult
from actions.msg import CountUntilFeedback

class CountUntilServer:
    def __init__(self):
        self._action_server = actionlib.SimpleActionServer('/count_until',
        CountUntilAction,
        self.on_goal,
        auto_start = False)
        self._action_server.start()
        self._counter = 0 
        rospy.loginfo('Simple action server has been started')

    def on_goal(self, goal):
        rospy.loginfo("A goal has been reveived!")
        rospy.loginfo(goal)
        max_number = goal.max_numberf
        wait_duration = goal.wait_duration
        self._counter = 0
        rate = rospy.Rate(1/wait_duration)
        success = False
        while not rospy.is_shutdown():
            self._counter += 1
            if self._counter > 9:
                success = False
                break
            if self._counter >= max_number:
                success = True
                break
            
            feedback = CountUntilFeedback()
            feedback.percentage = float(self._counter)/float(max_number)
            self._action_server.publish_feedback(feedback)
            rate.sleep()

        result = CountUntilResult()
        result.count = self._counter
        if success:
            self._action_server.set_succeeded(result)
        else:
            rospy.loginfo("Failure")
            self._action_server.set_aborted(result)


if __name__ == '__main__':
    rospy.init_node('count_until_server', anonymous = True)
    server = CountUntilServer()
    rospy.spin()