import time
import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit
from RpiMotorLib import RpiMotorLib

SERVO_CHANNEL = 0
GPIO_PINS = [18, 23, 24, 25]

def create_servo(channel=SERVO_CHANNEL):
    kit = ServoKit(channels=16)
    return kit.servo[channel]

def create_stepper(pins=GPIO_PINS):
    return RpiMotorLib.A4988Nema(direction_pin=18, step_pin=23, mode_pins=(24, 25), motor_pins=pins)

def test_servo(servo):
    for angle in range(0, 361, 60):
        servo.angle = angle
        time.sleep(1)

def test_stepper(stepper, steps=200, delay=0.01):
    stepper.motor_go(True, "Full", steps, delay, 0.0, True)
    time.sleep(1)
    stepper.motor_go(False, "Full", steps, delay, 0.0, True)

if __name__ == "__main__":
    try:
        servo = create_servo()
        stepper = create_stepper()

        test_servo(servo)
        test_stepper(stepper)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        GPIO.cleanup()
