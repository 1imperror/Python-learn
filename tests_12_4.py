from rt_with_exceptions import Runner
import unittest
import logging


logging.basicConfig(handlers=[logging.FileHandler("runner_tests.log", "w", "utf-8")],
                    level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'ok')
    def test_walk(self):
        try:
            logging.info('test_walk" выполнен успешно')
            runner = Runner('Run_Obi', -1)
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
        except ValueError as err:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'ok')
    def test_run(self):
        try:
            logging.info('test_run" выполнен успешно')
            runner = Runner(1, 5)
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
        except TypeError as err:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'ok')
    def test_challenge(self):
        runner1 = Runner('Run_Logan')
        runner2 = Runner('Run_Pool')
        for _ in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == '__main__':
    unittest.main()
