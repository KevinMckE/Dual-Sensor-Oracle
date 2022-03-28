/*
  Dual Sensor Script Edge Version

  Reads an analog input on pins 0 and 1, calculates the margin for error, and prints acceptable results to the Serial Monitor.
  Graphical representation is available using Serial Plotter (Tools > Serial Plotter menu).

*/

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
 
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0 and 1:
  int sensorValue1 = analogRead(A0);
  int sensorValue2 = analogRead(A1);
  
  float matchTest = test(float(sensorValue1), float(sensorValue2));
  Serial.print("Margin: ");
  Serial.print(matchTest);
  if(matchTest > 0.95){
    // print out the values you read:
    Serial.print(" (");
    Serial.print(sensorValue1);
    Serial.print(", ");
    Serial.print(sensorValue2);
    Serial.print(")");
  } else{
    Serial.print(" Replace Sensor");
  }
  
  delay(10000);
  Serial.println();
}

// test the difference between sensor values as a percentage of the input
float test(float SV1,float SV2){
  float matchTest;
  if(SV1 > SV2){
    matchTest = SV2 / SV1;
  } else if (SV2 > SV1){
    matchTest = SV1 / SV2;
  } else {
    matchTest = 1.00;
  }
  return matchTest;
  }


 
