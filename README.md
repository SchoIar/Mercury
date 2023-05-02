# Mercury

This Python script is designed to test the motor functions of a Raspberry Pi 4 connected to MG996R 360-degree servo motors and various stepper motors using an A4988 driver.

## Prerequisites

Install the required libraries:
```pip3 install RPi.GPIO
pip3 install adafruit-circuitpython-servokit
pip3 install RpiMotorLib```

## Hardware Setup

1. Connect the MG996R 360-degree servo motor to one of the channels on the PWM/Servo HAT.
2. Connect the stepper motor to the A4988 driver and the driver to the appropriate GPIO pins on the Raspberry Pi.

## Configuration

Update the configuration variables in `main.py` according to your setup:

```python
SERVO_CHANNEL = 0  # Change this to the channel your servo is connected to
GPIO_PINS = [18, 23, 24, 25]  # Change these to the GPIO pins connected to your stepper motor

## Usage

Run the `main.py` script to test motor function

NOTE: **This will only run on a Raspberry Pi system, as the RPi.GPIO library will not work on anything else as it is specifically designed for Raspberry Pi systems**

`python3 main.py`

## License

This project is licensed under the MIT License - see the LICENSE file for details.


