const int ledPin = 2;     // the number of the pushbutton pin
const int buttonPin = 3;     // the number of the pushbutton pin

int buttonState = 0;         

int sentDat;

void setup() {
  Serial.begin(9600); 
     
  pinMode(ledPin, OUTPUT);    
  pinMode(buttonPin, INPUT);  
}

void loop() {
  buttonState = digitalRead(buttonPin);

  if (Serial.available() > 0) {
    sentDat = Serial.read(); 
    if(sentDat == 'h') {
        digitalWrite(ledPin, HIGH);
        delay(1000);
        digitalWrite(ledPin, LOW);
    }
  }

  if (buttonState == HIGH) {     
    Serial.println('z');
    Serial.println("Patata");
    delay(1000); 
  } else if(buttonState == LOW) {
//    Serial.println('a');    
  }
  
}

