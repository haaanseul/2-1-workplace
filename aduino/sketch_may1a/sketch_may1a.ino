const int red =32;
const int green = 33;

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
   pinMode(red, OUTPUT);
    pinMode(green, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
  digitalWrite(red, HIGH);   
  digitalWrite(green, HIGH);   
  delay(1000);                       // wait for a second
  digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
  digitalWrite(red, LOW);    
  digitalWrite(green, LOW);    
  delay(1000);                       // wait for a second
}
