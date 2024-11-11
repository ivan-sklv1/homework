import unittest
import runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        person = runner.Runner('Petr')
        for i in range(10):
            person.walk()
        self.assertEqual(person.distance, 50)
    
    def test_run(self):
        person = runner.Runner('Petr')
        for i in range(10):
            person.run()
        self.assertEqual(person.distance, 100)

    def test_challenge(self):
        person1 = runner.Runner('Vasya')
        person2 = runner.Runner('Egot')
        for i in range(10):
            person1.run()
            person2.walk()
        self.assertNotEqual(person1, person2)

if __name__ == '__main__':
    unittest.main()
