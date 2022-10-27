from enum import auto
import rospy
import actionlib
import math

from actions.msg import DriveAction
from actions.msg import DriveFeedback
from actions.msg import DriveResult

class drive_server:
    def __init__(self):
        #stworzenie servera
        self.action_server = actionlib.SimpleActionServer('drive',
        DriveAction,
        self.on_goal,
        auto_start = False)
        self.action_server.start()        
        rospy.loginfo("SERVER HAS BEEN STARTED")
        
    def on_goal(self, goal):
        rospy.loginfo("A GOAL HAS BEEN RECEIVED!!!"+str(goal))

        #stworzenie zmiennych przyjmujacych inf od clienta
        self.x_goal = goal.x_goal
        self.y_goal = goal.y_goal

        #zmienne opisujace aktualny stan obiektu
        self.x_actual = 0
        self.y_actual = 0
        self.z_angualar_actual = 0

        #zmeinna do wysylania feedbacku
        self.feedback = DriveFeedback()

        #musze wyznaczyc kat miedzy pozycja aktualna a celem
        self.z_angular = math.atan2(self.y_goal - self.y_actual, self.x_goal - self.x_actual)
        rospy.loginfo("KAT O JAKI SIE OBRACAM: "+ str(self.z_angular))

        rate = rospy.Rate(1)
        
        while self.z_angualar_actual <= self.z_angular:
            self.z_angualar_actual = self.z_angualar_actual + 0.01
            self.feedback.left_engine = True
            self.feedback.right_engine = False
        
        while not rospy.is_shutdown():
            if self.x_actual<= self.x_goal:
                self.feedback.left_engine = True
                self.feedback.right_engine = True
                self.x_actual = self.x_actual+1
                self.feedback.actual_x = self.x_actual
            if self.y_actual<= self.y_goal:
                self.feedback.left_engine = True
                self.feedback.right_engine = True
                self.y_actual = self.y_actual+1
                self.feedback.actual_y = self.y_actual
            if self.x_actual == self.x_goal and self.y_actual == self.y_goal:
                self.feedback.left_engine = False
                self.feedback.right_engine = False
                break
            self.action_server.publish_feedback(self.feedback)
            rate.sleep()
        result = DriveResult()
        result.is_goal_reached = True
        self.action_server.set_succeeded(result)



if __name__ == '__main__':
    rospy.init_node('drive_server', anonymous = True) 
    server = drive_server()