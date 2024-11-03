import threading
import random
from queue import Queue
from time import sleep


class Table:
    
    def __init__(self, number: int):
        self.number = number
        self.guest = None
        

class Guest(threading.Thread):
    
    def __init__(self, name: str):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        sleep(random.randint(3, 10))
        # print(f'{self.name} ушёл(ушла) из кафе')


class Cafe:

    def __init__(self, *tables: int):
        self.tables = list(tables)
        self.queue = Queue()

    def guest_arrival(self, *guests):
        list_guests = list(guests)
        len_list_guests = len(list_guests)
        min_guests_tables = min(len_list_guests, len(self.tables))
        for i in range(min_guests_tables):
            self.tables[i].guest = guests[i]
            thr1 = guests[i]
            thr1.start()
            print(f'{list_guests[i].name} сел(-а) за стол номер {self.tables[i].number}')
        if len_list_guests > min_guests_tables:
            for i in range(min_guests_tables, len_list_guests):
                self.queue.put(guests[i])
                print(f'{list_guests[i].name} в очереди')

    def discuss_guests(self):
        for table in self.tables:
            while not self.queue.empty() or table.guest is not None:
                for table in self.tables:
                    if table.guest is not None and not (table.guest.is_alive()):
                        print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                        print(f'Стол номер {table.number} свободен')
                        table.guest = None
                    if not self.queue.empty() and table.guest is None:
                        table.guest = self.queue.get()
                        print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                        thread1 = table.guest
                        thread1.start()


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
