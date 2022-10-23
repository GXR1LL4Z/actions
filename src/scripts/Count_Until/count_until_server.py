import rospy
import actionlib
from actions.msg import CountUntilAction
from actions.msg import CountUntilGoal
from actions.msg import CountUntilActionResult

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
        max_number = goal.max_number
        wait_duration = goal.wait_duration
        self._counter = 0
        rate = rospy.Rate(1/wait_duration)
        while self._counter < max_number:
            self._counter += 1
            rate.sleep()
        result = CountUntilActionResult()
        result.count = self._counter
        self._action_server.set_succeeded(result)


if __name__ == '__main__':
    rospy.init_node('count_until_server', anonymous = True)
    server = CountUntilServer()
    rospy.spin()