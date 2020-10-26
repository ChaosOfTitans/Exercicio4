import rospy
from std_msgs.msg import String


rospy.init_node('Atividade_4_soma')

valor = '0'

def topic_callBack (soma_total):
    global valor
    valor = soma_total.data
    
    
    
rospy.Subscriber('/matricula', String, topic_callBack)
    
def timerCallBack(event):
    soma_total = 0
    
    for i in valor:
        soma_total = soma_total +int(i)
    msg = String()
    msg.data = str(soma_total)
        
    pub.publish(msg)
        
pub = rospy.Publisher('/soma', String, queue_size = 1)
timer = rospy.Timer(rospy.Duration(0.05), timerCallBack)
        
rospy.spin()
    
