import math
import os
import unittest

from week03_pattern.pattern import build_pattern


class MyPatternTests(unittest.TestCase):

    def test_my_pattern_geometry(self):
        segments = build_pattern(os.environ["WEEK03_ASSIGNED_PATTERN"])

        self.assertEqual(len(segments), 4)

        for segment in segments:
            self.assertGreater(segment.linear_x, 0.0)

            radius = abs(segment.linear_x / segment.angular_z)
            self.assertAlmostEqual(radius, 0.30, places=5)

            angle = abs(segment.angular_z * segment.duration)
            self.assertAlmostEqual(angle, math.pi / 4, places=5)

    def test_my_pattern_order(self):
        segments = build_pattern(os.environ["WEEK03_ASSIGNED_PATTERN"])

        expected_signs = [1, -1, 1, -1]

        actual_signs = [
            1 if segment.angular_z > 0 else -1
            for segment in segments
        ]

        self.assertEqual(actual_signs, expected_signs)

        final_heading = sum(
            segment.angular_z * segment.duration
            for segment in segments
        )

        self.assertAlmostEqual(final_heading, 0.0, places=5)


if __name__ == "__main__":
    unittest.main()