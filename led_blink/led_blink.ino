/*
  Physical Pixel

 An example of using the Arduino board to receive data from the
 computer.  In this case, the Arduino boards turns on an LED when
 it receives the character 'H', and turns off the LED when it
 receives the character 'L'.

 The data can be sent from the Arduino serial monitor, or another
 program like Processing (see code below), Flash (via a serial-net
 proxy), PD, or Max/MSP.

 The circuit:
 * LED connected from digital pin 13 to ground

 created 2006
 by David A. Mellis
 modified 30 Aug 2011
 by Tom Igoe and Scott Fitzgerald

 This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/PhysicalPixel
 */

const int ledPin = 13; // the pin that the LED is attached to
int incomingByte;      // a variable to read incoming serial data into

void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // see if there's incoming serial data:
  if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer:
    incomingByte = Serial.read();
    // if it's a capital H (ASCII 72), turn on the LED:
    if (incomingByte == 'J') {
      Serial.println('J');
      for (int i=0; i <=2; i++){
      //Serial.println("Jaw Clenching ");
      digitalWrite(ledPin, HIGH);
      delay(300);
      digitalWrite(ledPin, LOW);
      delay(300);
      }
    }
    // if it's an L (ASCII 76) turn off the LED:
    if (incomingByte == 'B') {
      Serial.println('B');
      for (int i=0; i <= 6; i++){
      //Serial.println("Blinking ");

      digitalWrite(ledPin, HIGH);
      delay(100);
      digitalWrite(ledPin, LOW);
      delay(100);
      }
    }

  }
}

