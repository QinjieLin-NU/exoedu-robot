/*
 * rosserial Publisher Example
 * Prints "hello world!"
 */

#include <ros.h>
#include <std_msgs/String.h>
#include <std_msgs/Float64.h>
#include <std_msgs/Int8.h>

int servoAnalogInPin = A0;
int posIs;
float posIsDeg;

ros::NodeHandle  nh;
float x; 
std_msgs::Float64 angle;
std_msgs::String str_msg;
ros::Publisher chatter("chatter", &angle);

void setup()
{
  Serial.begin(96);
  delay(100);

  nh.initNode();
  nh.advertise(chatter);
  delay(10);
}

void loop()
{
  posIs = analogRead(servoAnalogInPin);
  posIsDeg = (90.0/(255.0-80.0))*(posIs-80);
  Serial.print("Position (in degree):");
  Serial.println(posIsDeg);
  
  angle.data = posIsDeg;
  chatter.publish( &angle );
  nh.spinOnce();
  
  delay(10);
}
