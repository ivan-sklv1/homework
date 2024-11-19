import inspect
import unittest
from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
        
    def setUp(self):
        self.usain_runner = Runner('Усэйн', 10)
        self.andrey_runner = Runner('Андрей', 9)
        self.nik_runner = Runner('Ник', 3)
    
    @classmethod
    def tearDownClass(cls):
        print()
        for test in cls.all_results:
            print()
            print(f'{test}:')
            print({k: str(v) for k, v in cls.all_results[test].items()})
    
    def test_usain_nik(self):
        tournament = Tournament(90, self.usain_runner, self.nik_runner)
        result = tournament.start()
        self.all_results[inspect.stack()[0][3]] = result
        self.assertTrue('Ник' == result[len(result)].name)

    def test_andrey_nik(self):
        tournament = Tournament(90, self.andrey_runner, self.nik_runner)
        result = tournament.start()
        self.all_results[inspect.stack()[0][3]] = result
        self.assertTrue('Ник' == result[len(result)].name)
        
    def test_usain_andrey_nik(self):
        tournament = Tournament(90, self.usain_runner, self.andrey_runner, self.nik_runner)
        result = tournament.start()
        self.all_results[inspect.stack()[0][3]] = result
        self.assertTrue('Ник' == result[len(result)].name)
    

if __name__ == '__main__':
    unittest.main()
