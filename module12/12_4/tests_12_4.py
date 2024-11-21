import logging
import unittest
import runner


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            person = runner.Runner('Petr', -1)
            for i in range(10):
                person.walk()
            self.assertEqual(person.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            person = runner.Runner(2007)
            for i in range(10):
                person.run()
            self.assertEqual(person.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        filemode='w',
        filename='runner_tests.log',
        encoding='utf-8',
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    unittest.main()
