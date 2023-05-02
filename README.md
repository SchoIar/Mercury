# Mercury

This Python script is designed to test the motor functions of a Raspberry Pi 4 connected to MG996R 360-degree servo motors and various stepper motors using an A4988 driver.

## Prerequisites

Install the required libraries:
`pip3 install RPi.GPIO`
`pip3 install adafruit-circuitpython-servokit`
`pip3 install RpiMotorLib`

## Hardware Setup

1. Connect the MG996R 360-degree servo motor to one of the channels on the PWM/Servo HAT.
2. Connect the stepper motor to the A4988 driver and the driver to the appropriate GPIO pins on the Raspberry Pi.

See end note for more detailed setup 

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
```

## Detailed setup
### Raspberry Pi 4 Setup for Servos and Stepper Motors

#### 1. Set up your Raspberry Pi 4

1. Download the latest Raspberry Pi OS from the official website: https://www.raspberrypi.org/software/operating-systems/
2. Flash the Raspberry Pi OS onto a microSD card (minimum 8GB recommended) using a tool like Balena Etcher: https://www.balena.io/etcher/
3. Insert the microSD card into your Raspberry Pi 4, connect a keyboard, mouse, and monitor, and then power it up using a USB-C power supply (5.1V/3A recommended).

#### 2. Configure Raspberry Pi OS

1. On first boot, follow the on-screen instructions to configure your Raspberry Pi OS, including setting your locale, keyboard layout, and Wi-Fi credentials (if using Wi-Fi).
2. Open a terminal and run the following commands to update your system:
`sudo apt update`
`sudo apt upgrade`

#### 3. Install required Python libraries

1. Install pip:
`sudo apt install python3-pip`
2. Install the Adafruit ServoKit library for controlling the servos:
`pip3 install adafruit-circuitpython-servokit`
3. Install the RPi.GPIO library for controlling the stepper motors:
`pip3 install RPi.GPIO`

#### 4. Connect the MG996R servos

1. Connect the servos to your Raspberry Pi using a PCA9685 16-Channel Servo Driver, which can be controlled using the Adafruit ServoKit library. The PCA9685 module communicates with the Raspberry Pi using I2C.
2. Connect the PCA9685 module's VCC pin to the Raspberry Pi's 3.3V or 5V power pin, the GND pin to the Raspberry Pi's GND, the SDA pin to the Raspberry Pi's SDA (GPIO 2), and the SCL pin to the Raspberry Pi's SCL (GPIO 3).
3. Connect each servo's signal wire (usually orange or white) to one of the PCA9685 module's PWM channels (0 to 15). Connect the servo's power (red) wire to the module's 5V or external power supply, and the ground (black or brown) wire to the module's GND.

#### 5. Connect the stepper motors

1. For each stepper motor, use an A4988 stepper motor driver. Connect the driver's VMOT pin to a suitable power supply for your stepper motor (check the motor's specifications), and the GND pin to the power supply's ground.
2. Connect the A4988 driver's VDD pin to the Raspberry Pi's 3.3V or 5V power pin, and the GND pin to the Raspberry Pi's GND.
3. Connect the A4988 driver's STEP pin to a GPIO pin on the Raspberry Pi (e.g., GPIO 23), and the DIR pin to another GPIO pin (e.g., GPIO 18).
4. (Optional) Connect the A4988 driver's MS1, MS2, and MS3 pins to additional GPIO pins on the Raspberry Pi (e.g., GPIO 24, 25) to enable microstepping.
5. Connect the A4988 driver's 1A and 1B pins to one coil of the stepper motor, and the 2A and 2B pins to the other coil. Refer to your stepper motor's documentation




