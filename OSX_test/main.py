import time
import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit
from RpiMotorLib import RpiMotorLib

SERVO_CHANNEL = 0
GPIO_PINS = [18, 23, 24, 25]

kit = ServoKit(channels=16)
servo = kit.servo[SERVO_CHANNEL]

direction_pin = 18
step_pin = 23
mode_pins = (24, 25)
stepper = RpiMotorLib.A4988Nema(direction_pin, step_pin, mode_pins, GPIO_PINS)

def test_servo():
    servo.angle = 0
    time.sleep(1)
    servo.angle = 90
    time.sleep(1)
    servo.angle = 180
    time.sleep(1)
    servo.angle = 90
    time.sleep(1)
    servo.angle = 0
    time.sleep(1)

def test_stepper():
    steps = 200
    sleep_time = 0.005
    stepper.motor_go(True, "Full", steps, sleep_time, False)
    time.sleep(1)
    stepper.motor_go(False, "Full", steps, sleep_time, False)
    time.sleep(1)

try:
    while True:
        print("Testing servo...")
        test_servo()
        print("Testing stepper...")
        test_stepper()
except KeyboardInterrupt:
    print("Exiting...")
