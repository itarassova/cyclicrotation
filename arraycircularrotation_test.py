import unittest

import alt_sol_circ_rot_arr as test_solution

class MyTest(unittest.TestCase):
    def test_full_wraparound(self):
        self.assertEqual(test_solution.solution(
            4, [1, 2, 3, 4]), [1, 2, 3, 4])

    def test_off_by_one(self):
        self.assertEqual(test_solution.solution(
            1, [1, 2, 3, 4]), [4, 1, 2, 3])

    def test_thesame(self):
        self.assertEqual(test_solution.solution(
            1, [0,0,0,0]), [0,0,0,0])

    def test_double_wraparound(self):
        self.assertEqual(test_solution.solution(
            8, [1, 2, 3, 4]), [1, 2, 3, 4])

    def test_empty_array(self):
        self.assertEqual(test_solution.solution(
            8, []), [])
