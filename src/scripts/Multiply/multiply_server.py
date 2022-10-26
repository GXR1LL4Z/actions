import rospy

class multiply_server:
    def __init__(self):
        pass



if __name__ == '__main__':
    rospy.init_node('multiply_server', anonymous = True)
    server = multiply_server()
    rospy.spin()
