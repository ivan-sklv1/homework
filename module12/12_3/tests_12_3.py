import inspect
import unittest
import runner
from runner_and_tournament import Runner, Tournament

class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        person = runner.Runner('Petr')
        for i in range(10):
            person.walk()
        self.assertEqual(person.distance, 50)
    
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        person = runner.Runner('Petr')
        for i in range(10):
            person.run()
        self.assertEqual(person.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        person1 = runner.Runner('Vasya')
        person2 = runner.Runner('Egot')
        for i in range(10):
            person1.run()
            person2.walk()
        self.assertNotEqual(person1, person2)


class TournamentTest(unittest.TestCase):
    is_frozen = True
    
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
    
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_usain_nik(self):
        tournament = Tournament(90, self.usain_runner, self.nik_runner)
        result = tournament.start()
        self.all_results[inspect.stack()[0][3]] = result
        self.assertTrue('Ник' == result[len(result)].name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_andrey_nik(self):
        tournament = Tournament(90, self.andrey_runner, self.nik_runner)
        result = tournament.start()
        self.all_results[inspect.stack()[0][3]] = result
        self.assertTrue('Ник' == result[len(result)].name)
        
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_usain_andrey_nik(self):
        tournament = Tournament(90, self.usain_runner, self.andrey_runner, self.nik_runner)
        result = tournament.start()
        self.all_results[inspect.stack()[0][3]] = result
        self.assertTrue('Ник' == result[len(result)].name)
    

if __name__ == '__main__':
    unittest.main()
