import unittest
import tests_12_3


runTour = unittest.TestSuite()

runTour.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
runTour.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runTour)
