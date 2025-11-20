# SW: PIN23
# DT: PIN25
# CLK: PIN24

import string

print(string.printable)

''' Arduino Code
const int interruptA = 0;      
const int interruptB = 1;      
int CLK = 24;     // PIN24
int DAT = 25;     // PIN25
int BUTTON = 23;  // PIN23
int COUNT = 0;

void setup()
 {
  attachInterrupt(interruptA, RoteStateChanged, FALLING);
 // attachInterrupt(interruptB, buttonState, FALLING);
  pinMode(CLK, INPUT);
  digitalWrite(2, HIGH);  // Pull High Restance 
  pinMode(DAT, INPUT);
  digitalWrite(3, HIGH);  // Pull High Restance
pinMode(BUTTON, INPUT);
  digitalWrite(4, HIGH);  // Pull High Restance
   Serial.begin(9600);
 }
void loop()
{
  if  (!(digitalRead(BUTTON)))
    {
     COUNT = 0; 
     Serial.println("STOP COUNT = 0");
     delay (2000);
    }
     Serial.println(COUNT); 
}
//-------------------------------------------
void RoteStateChanged() //When CLK  FALLING READ DAT
{
 if  (digitalRead(DAT)) // When DAT = HIGH IS FORWARD
   {
    COUNT++;
    delay(20);
   }
 else                   // When DAT = LOW IS BackRote
   {
    COUNT--;
    delay(20);
   }
}
'''