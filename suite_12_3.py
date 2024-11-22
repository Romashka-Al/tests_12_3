import unittest
import tests_12_3
from tests_12_1 import RunnerTest

testcase = unittest.TestSuite()
testcase.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))
testcase.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(testcase)
