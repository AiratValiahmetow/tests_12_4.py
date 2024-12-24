import logging
import unittest
from rt_with_exceptions import Runner

# Настройка логирования
logging.basicConfig(level=logging.INFO,filemode='w',filename='runner_tests.log',
encoding='utf-8',
format='%(asctime)s - %(levelname)s - %(message)s')


class Runner:
    def __init__(self, name: str, speed: float):
        if not isinstance(name, str):
            raise TypeError("name должен быть строкой")
        if speed < 0:
            raise ValueError("speed не может быть отрицательным")
        self.name = name
        self.speed = speed

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner = Runner("Runner1", -10)
        except ValueError as e:
            logging.warning("Неверная скорость для Runner: %s", e)
        else:
            logging.info('"test_walk" выполнен успешно')

    def test_run(self):
        try:
            runner = Runner(123, 10)
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner: %s", e)
        else:
            logging.info('"test_run" выполнен успешно')

if __name__ == '__main__':
    unittest.main()