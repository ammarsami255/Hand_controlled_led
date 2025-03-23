#define LED1 13  
#define LED2 12  
#define LED3 11  

void setup() {
    pinMode(LED1, OUTPUT);
    pinMode(LED2, OUTPUT);
    pinMode(LED3, OUTPUT);
    Serial.begin(9600);
}

void loop() {
    if (Serial.available() >= 3) {  
        char data[4]; 
        Serial.readBytes(data, 3);  
        data[3] = '\0';  

        digitalWrite(LED1, data[0] == '1' ? HIGH : LOW);
        digitalWrite(LED2, data[1] == '1' ? HIGH : LOW);
        digitalWrite(LED3, data[2] == '1' ? HIGH : LOW);
    }
}
