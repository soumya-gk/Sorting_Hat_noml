#include <Servo.h>

Servo mservo1;
Servo mservo2;

int pneum1 = 4;
int pneum2 = 5;

char START = 's';
char END = 'e';
char UP = 'u';
char DOWN = 'd';

int sentDat;

void setup() {
  Serial.begin(9600); 
  initServo();
  pinMode(pneum1,OUTPUT);  
  pinMode(pneum2,OUTPUT);
}

void initServo() {
  
  mservo1.attach(3);// attaches the servo on pin 3 to the servo object
  mservo1.write(70);

  mservo2.attach(2);
  mservo2.write(110);
}

void startSpeak() {
  int pos1 = 70;
  int pos2 = 110;
  for(int st_time = 0; st_time < 7; st_time += 1)
  {                                
    mservo1.write(pos1);
    mservo2.write(pos2);
    pos1 -= 11;
    pos2 += 6;         
    delay(80);
  }
  for(int st_time = 0; st_time < 7; st_time += 1)
  {                                
    mservo1.write(pos1);
    mservo2.write(pos2);
    pos1 += 11;
    pos2 -= 6;         
    delay(80);
  }
}

void loop() {
  if (Serial.available() > 0) {
    sentDat = Serial.read(); 
    if(sentDat == START) {
      while (Serial.read() != END) {
        startSpeak();
      }
    } else if (sentDat == UP) {
      digitalWrite(pneum1, HIGH);
      digitalWrite(pneum2, HIGH);
      delay(500);
      digitalWrite(pneum2, LOW);
    } else if (sentDat == DOWN) {
      digitalWrite(pneum1, LOW); 
    } 
  }  
}

