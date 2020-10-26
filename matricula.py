import rospy
from std_msgs.msg import String


rospy.init_node('Atividade_4')

num = 'matricula = 2017001704'

def num_callBack(msg):
    global num
    num = msg.data

def timerCallBack(event):
    msg = String()
    msg.data = '2017001704000000000'
    pub.publish(msg)
    
pub = rospy.Publisher('/matricula', String, queue_size = 1)
timer = rospy.Timer(rospy.Duration(0.05), timerCallBack)
sub = rospy.Subscriber('/soma', String, num_callBack)

rospy.spin()