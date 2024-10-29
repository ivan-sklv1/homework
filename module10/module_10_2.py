import threading
import time


class Knight(threading.Thread):

    def __init__(self, name:str, power:int, delay=1):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.delay = delay

    def run(self):
        print(f'{self.name}, на нас напали!')
        days = 0
        warriors = 100
        while warriors !=0:
            time.sleep(self.delay)
            days += 1
            warriors -= self.power
            print(f'{self.name} сражается {days} день(дня)..., осталось {warriors} воинов.')
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
