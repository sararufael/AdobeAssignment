import unittest
import Attendance


class TestAttendance(unittest.TestCase):
    """ Unit test for Attendance module """

    def test_count_prize_strings(self):
        self.assertEqual(1918080160, Attendance.count_prize_strings(30))
        self.assertEqual(43, Attendance.count_prize_strings(4))

if __name__ == '__main__':
    unittest.main()
