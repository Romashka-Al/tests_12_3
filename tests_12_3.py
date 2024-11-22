import unittest
from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.r1 = Runner('Злюка', speed=10)
        self.r2 = Runner('Килза', speed=9)
        self.r3 = Runner('Рома', speed=3)

    @classmethod
    def tearDownClass(cls):
        for res in cls.all_results:
            print({place: str(runner) for place, runner in res.items()})

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test1(self):
        tournament = Tournament(90, *[self.r1, self.r3])
        self.all_results.append(tournament.start())
        self.assertEqual(self.all_results[0][2], 'Рома')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test2(self):
        tournament = Tournament(90, *[self.r2, self.r3])
        self.all_results.append(tournament.start())
        self.assertEqual(self.all_results[1][2], 'Рома')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test3(self):
        tournament = Tournament(90, *[self.r1, self.r2, self.r3])
        self.all_results.append(tournament.start())
        self.assertEqual(self.all_results[2][3], 'Рома')


if __name__ == '__main__':
    unittest.main()
