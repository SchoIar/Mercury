#TODO: Create testing file, with Python's MagicMock to simulate the behavior of the components for testing purposes
import unittest
from unittest.mock import MagicMock
from main import create_servo, create_stepper, test_servo, test_stepper

class TestMotorControl(unittest.TestCase):

    def test_create_servo(self):
        servo = create_servo()
        self.assertIsNotNone(servo)

    def test_create_stepper(self):
        stepper = create_stepper()
        self.assertIsNotNone(stepper)

    def test_test_servo(self):
        servo = MagicMock()
        test_servo(servo)
        self.assertEqual(servo.angle.call_count, 7)  # We expect the servo angle to be set 7 times

    def test_test_stepper(self):
        stepper = MagicMock()
        test_stepper(stepper)
        self.assertEqual(stepper.motor_go.call_count, 2)  # We expect the stepper motor to be called twice (CW and CCW)

if __name__ == "__main__":
    unittest.main()
