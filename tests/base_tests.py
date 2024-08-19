import unittest
import ast
from src import statements

class IndependentTests(unittest.TestCase):

    def test_assignments(self):

        tests = [ast.parse(command) for command in [
            "a = 10",
            "a = b",
            "a, b = 10, 20",
            "a, b = c, 20",
            "a = 10 + 5",
            "a = 10 - 5 * 2 + 7",
            "a = 10 - (5 + 2)",
            "a = 10 - 5 + 2",
            "a = 10 - (25 * 25)",
            "a = 10 * (25 / 100)",
            "a = 'string'",
            "a, b = 10, 'string'",
            "a, b = 'string', 'string'"
        ]]

        results = []
        for test in tests:
            for obj in test.body:
                if isinstance(obj, ast.Assign):
                    for inst in statements.assign(obj):
                        results.append(inst)

        self.assertEqual("LET a = 10", results[0])
        self.assertEqual("LET a = b", results[1])

        self.assertEqual("LET a = 10", results[2])
        self.assertEqual("LET b = 20", results[3])

        self.assertEqual("LET a = c", results[4])
        self.assertEqual("LET b = 20", results[5])

        self.assertEqual("LET a = 10 + 5", results[6])
        self.assertEqual("LET a = 10 - 5 * 2 + 7", results[7])
        self.assertEqual("LET a = 10 - (5 + 2)", results[8])
        self.assertEqual("LET a = 10 - 5 + 2", results[9])
        self.assertEqual("LET a = 10 - 25 * 25", results[10])
        self.assertEqual("LET a = 10 * (25 / 100)", results[11])

        self.assertEqual('LET a = "string"', results[12])

        self.assertEqual('LET a = 10', results[13])
        self.assertEqual('LET b = "string"', results[14])

        self.assertEqual('LET a = "string"', results[15])
        self.assertEqual('LET b = "string"', results[16])

if __name__ == '__main__':
    unittest.main()
