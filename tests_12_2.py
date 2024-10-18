from runner_and_tournament import Runner, Tournament
import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner('Усэйн', speed=10)
        self.runner2 = Runner('Андрей', speed=9)
        self.runner3 = Runner('Ник', speed=3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print({key: str(value) for key, value in result.items()})

    def test_Us_Ni(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        TournamentTest.all_results['Усэйн и Ник'] = results
        self.assertTrue(results[max(results.keys())] == 'Ник')

    def test_And_Ni(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        TournamentTest.all_results['Андрей и Ник'] = results
        self.assertTrue(results[max(results.keys())] == 'Ник')

    def test_Us_And_Ni(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        TournamentTest.all_results['Усэйн, Андрей и Ник'] = results
        self.assertTrue(results[max(results.keys())] == 'Ник')


if __name__ == '__main__':
    unittest.main()
