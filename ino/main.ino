const int ledPin = 2;     // the number of the pushbutton pin
const int buttonPin = 3;     // the number of the pushbutton pin

int buttonState = 0;         

int sentDat;

void setup() {
  Serial.begin(9600); 
     
  pinMode(ledPin, OUTPUT);    
  pinMode(buttonPin, INPUT);  
  // pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  buttonState = digitalRead(buttonPin);

  if (Serial.available() > 0) {
    sentDat = Serial.read(); 
    if(sentDat == 'h') {
      digitalWrite(ledPin, HIGH);
      delay(1000);
      digitalWrite(ledPin, LOW);
    } else if (sentDat == 'm') {
      Serial.println('m');
      delay(1000);  
    }
  }

  if (buttonState == HIGH) {     
    Serial.println('m');
    delay(1000); 
  } else if(buttonState == LOW) {
  //  Serial.println('a');    
  }
  
}

