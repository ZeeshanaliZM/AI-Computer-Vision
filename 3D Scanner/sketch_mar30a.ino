import cv2
import matplotlib.pyplot as plt
import serial
import time
while(bool(input('Enter a value to begin'))==False):
    pass
COMPort = input('Enter the COM port value')
countImages = 0
ArduinoSerial = serial.Serial(COMPort,9600)
time.sleep(2)
capture = cv2.VideoCapture(0)
captureFlag = False
ArduinoSerial.write(b'1')
print('...Starting Motor...')
time.sleep(5)
while(captureFlag==False):
    pass
    
    
const int dirPin = 13;
const int stepPin = 12;
const int stepsPerRevolution = 200;
int startSignal;
void setup() {
  pinMode(LED_BUILTIN,OUTPUT);
  digitalWrite(LED_BUILTIN,LOW);
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
  Serial.begin(9600);
}
void loop() {
  if (Serial.available() > 0){
    startSignal = Serial.read();}
  if(startSignal == '1')
  {digitalWrite(LED_BUILTIN,HIGH);
    rotateMotor();}
    }

void rotateMotor(){
  digitalWrite(dirPin, HIGH);
  digitalWrite(stepPin, HIGH);
  delayMicroseconds(2000);
  digitalWrite(stepPin, LOW);
  delayMicroseconds(2000);  
}
