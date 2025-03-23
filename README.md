#Real-Time Hand-Controlled LEDs

Project Idea

The program detects the number formed by the hand, converts it to Binary, and then sends it to the Arduino using the SPI protocol between the camera and the Arduino. Once the data is received, the Arduino takes the binary values and converts them into Digital Signals to turn the LEDs on or off based on the received number.

How It Works

Capturing the Image: The camera is used to analyze hand movements using Mediapipe.

Number Recognition: The number formed by the hand is identified using a machine learning model.

Binary Conversion: The number is converted to its binary representation to determine the state of each LED.

Data Transmission via SPI: The binary values are sent from the computer to the Arduino via the SPI protocol.

LED Control: The Arduino receives the data and converts it into digital signals to control the LEDs accordingly.

Requirements

Python with the following libraries:

opencv-python

mediapipe

numpy

pickle

pyserial

Arduino with 3 LEDs connected to pins 11, 12, 13.

How to Run

Run the Python script to process the video and send data to the Arduino.

Connect the Arduino to the computer and run its code.

Place your hand in front of the camera, and the system will recognize the number and light up the corresponding LEDs based on its binary representation.

Notes

Ensure that the COM port is correctly set in both the Python and Arduino code.

Make sure the camera is functioning properly and that lighting conditions are sufficient for accurate hand tracking.

The accuracy of number recognition can be improved by training a more precise machine learning model.
