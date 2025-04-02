void setup() {
    // Initialize the onboard LED pin (usually GPIO 2 for ESP32)
    pinMode(LED_BUILTIN, OUTPUT);
  }
  
  void loop() {
    // Turn the LED on (HIGH is the voltage level)
    digitalWrite(LED_BUILTIN, HIGH);
    delay(1000);  // Wait for 1 second
  
    // Turn the LED off by making the voltage LOW
    digitalWrite(LED_BUILTIN, LOW);
    delay(1000);  // Wait for 1 second
  }