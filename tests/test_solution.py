from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution

        dict1 = {1: 10, 2: 20}
        dict2 = {3: 30, 4: 40}

        res = solution(dict1, dict2)

        self.assertEqual(10, res[1])
        self.assertEqual(20, res[2])
        self.assertEqual(30, res[3])
        self.assertEqual(40, res[4])

    def test_solution_same_keys(self):
        from build import solution

        dict1 = {1: 10, 2: 20}
        dict2 = {2: 30, 4: 40}

        res = solution(dict1, dict2)

        self.assertEqual(10, res[1])
        self.assertEqual(30, res[2])
        self.assertEqual(40, res[4])
