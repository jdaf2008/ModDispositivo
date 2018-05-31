
/*

code by Juan Arias 8/05/2018

This program sends data from air sensor:

Metano MQ4, AO: 0 DO:3
Air quality, AO: 1 DO:4
Sound, DO: 2


*/

// Pines 
int firstASPin = A0;
int secondASPin = A1;
int thirdASPin = A2;
int firstDSPin = 2;
int secondDSPin = 3;
int thirdDSPin = 4;

//Variables
int firstAS = 0;
int secondAS = 0;
int thirdAS = 0;
int firstDS = 0;
int secondDS = 0;
int thirdDS = 0;


void setup(){
  //start serial port at 9600 bps:
  Serial.begin(9600);
  
  pinMode(firstDSPin,INPUT);
  pinMode(secondDSPin,INPUT);
  pinMode(thirdDSPin,INPUT);

  // establishContact();
  
}

void loop()
{
  
   // read  analog input, divide by 4 to make the range 0-255:
   firstAS = analogRead(firstASPin);
   delay(10);
   secondAS = analogRead(secondASPin);
   delay(10);
   thirdAS = analogRead(thirdASPin);
   
   // read digital input
   firstDS = digitalRead(firstDSPin);
   secondDS = digitalRead(secondDSPin);
   thirdDS = digitalRead(thirdDSPin);
   
   // send sensor values:
   Serial.println( String(firstAS) + ',' +  String(secondAS) + ',' + String(thirdDS) );
   delay(5000);
   // Serial.println(firstAS);
   // delay(1000);
   // Serial.println(secondAS);
   // delay(1000);
   // Serial.println(thirdDS);
   // delay(1000);
   
}



void establishContact() {
  while (Serial.available() <= 0) {
    Serial.print('A');   // send a capital A
    delay(300);
  }
}

