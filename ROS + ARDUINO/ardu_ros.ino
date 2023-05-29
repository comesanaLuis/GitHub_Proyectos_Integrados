#include <ros.h>
#include <std_msgs/Int32.h>

ros::NodeHandle  nh;

std_msgs::Int32 valor;
ros::Publisher chatter("arduino", &valor);

int contador = 0;

void setup()
{
  nh.initNode();
  nh.advertise(chatter);
}

void loop()
{
  contador++;
  valor.data = contador;
  chatter.publish( &valor );
  nh.spinOnce();
  delay(1000);
}
