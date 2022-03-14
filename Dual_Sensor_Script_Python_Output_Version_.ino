/*
  Dual Sensor Direct Serial Output

  Reads analog inputs on pin 0 and 1, prints the results to the Serial Monitor.
  
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

// print the rounded margin of error between sensors
   if(float(sensorValue1) <= float(sensorValue2)){
    float x = static_cast<float>(sensorValue1) / static_cast<float>(sensorValue2);
    Serial.print("Margin: ");
    Serial.print(x);
  } else if(float(sensorValue2) < float(sensorValue1)){
    float x = static_cast<float>(sensorValue2) / static_cast<float>(sensorValue1);
    Serial.print("Margin: ");
    Serial.print(x);
  }
  
 // print the actual values
  Serial.print(" (");
  Serial.print(sensorValue1);
  Serial.print(", ");
  Serial.print(sensorValue2);
  Serial.println(")");
  
  delay(5000);
}


 
