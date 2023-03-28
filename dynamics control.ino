/*******************************************************************************
* Copyright 2016 ROBOTIS CO., LTD.
*
* Licensed under the Apache License, Version 2.0 (the "License");
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at
*
*     http://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
*******************************************************************************/

#include <Dynamixel2Arduino.h>

// Please modify it to suit your hardware.
#if defined(ARDUINO_AVR_UNO) || defined(ARDUINO_AVR_MEGA2560) // When using DynamixelShield
  #include <SoftwareSerial.h>
  SoftwareSerial soft_serial(7, 8); // DYNAMIXELShield UART RX/TX
  #define DXL_SERIAL   Serial
  #define DEBUG_SERIAL soft_serial
  const int DXL_DIR_PIN = 2; // DYNAMIXEL Shield DIR PIN
#endif

const uint8_t DXL_ID = 1;
const float DXL_PROTOCOL_VERSION = 2.0;

Dynamixel2Arduino dxl(DXL_SERIAL, DXL_DIR_PIN);

//This namespace is required to use Control table item names
using namespace ControlTableItem;

void setup() {
  // put your setup code here, to run once:
  
  // Use UART port of DYNAMIXEL Shield to debug.
  DEBUG_SERIAL.begin(115200);
  
  // Set Port baudrate to 57600bps. This has to match with DYNAMIXEL baudrate.
  dxl.begin(57600);
  // Set Port Protocol Version. This has to match with DYNAMIXEL protocol version.
  dxl.setPortProtocolVersion(DXL_PROTOCOL_VERSION);
  // Get DYNAMIXEL information
  dxl.ping(DXL_ID);

  // Turn off torque when configuring items in EEPROM area
  dxl.torqueOff(DXL_ID);
  dxl.setOperatingMode(DXL_ID, OP_POSITION);
  dxl.torqueOn(DXL_ID);

  DEBUG_SERIAL.setTimeout(100);
  pinMode(LED_BUILTIN, OUTPUT);

}

int speed = 0;
void loop() {
  while (DEBUG_SERIAL.available() == 0) {}     //wait for data available
  String teststr = DEBUG_SERIAL.readString();  //read until timeout
  teststr.trim();                        // remove any \r \n whitespace at the end of the String
  control(teststr[0]);
  speed = dxl.getPresentPosition(DXL_ID, UNIT_DEGREE);
  Serial.print(" ");
  Serial.print(speed);
  Serial.print("\n");
}

void control(char choice) {
  switch(choice) {
    case '1':
      dxl.setGoalPosition(DXL_ID, 0.0, UNIT_DEGREE);
      digitalWrite(LED_BUILTIN, HIGH);
      break;
    case '2':
      dxl.setGoalPosition(DXL_ID, 90.0, UNIT_DEGREE);
      digitalWrite(LED_BUILTIN, LOW);
      break;
    case '3':
      dxl.setGoalPosition(DXL_ID, 180.0, UNIT_DEGREE);
      digitalWrite(LED_BUILTIN, HIGH);
      break;
    default:
      dxl.setGoalPosition(DXL_ID, 0, UNIT_DEGREE);
      digitalWrite(LED_BUILTIN, LOW);
  }
}

