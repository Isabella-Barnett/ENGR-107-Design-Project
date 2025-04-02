void setup() {
    // Initialize GPIO 2 as an output for the onboard LED
    pinMode(2, OUTPUT);
  }
  
  void loop() {
    // Turn the LED on
    digitalWrite(2, HIGH);
    delay(1000);  // Wait for 1 second
  
    // Turn the LED off
    digitalWrite(2, LOW);
    delay(1000);  // Wait for 1 second
  }
  