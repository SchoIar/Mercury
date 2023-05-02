import unittest
from unittest.mock import MagicMock, patch
import os
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'


mocked_modules = {
    'RPi.GPIO': MagicMock(),
    'RPi': MagicMock(),
    'adafruit_servokit': MagicMock(),
    'RpiMotorLib': MagicMock()
}

with patch.dict('sys.modules', mocked_modules):
    from main import test_servo, test_stepper

class TestMotorControl(unittest.TestCase):

    def test_test_servo(self):
        servo = MagicMock()
        test_servo(servo)
        self.assertEqual(servo.angle.call_count, 5)

    def test_test_stepper(self):
        stepper = MagicMock()
        test_stepper(stepper)
        self.assertEqual(stepper.motor_go.call_count, 2)

if __name__ == "__main__":
    unittest.main()
