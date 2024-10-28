import threading
from datetime import datetime
from time import sleep


def write_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i + 1} \n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

time_start = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_end = datetime.now()
time_res_1 = time_end - time_start
print(f'Работа потоков {time_res_1}')

thread_start = datetime.now()

thread1 = threading.Thread(target=write_words, args=(10, 'example1.txt'))
thread2 = threading.Thread(target=write_words, args=(30, 'example2.txt'))
thread3 = threading.Thread(target=write_words, args=(200, 'example3.txt'))
thread4 = threading.Thread(target=write_words, args=(100, 'example4.txt'))

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

thread_stop = datetime.now()
time_res_2 = thread_stop - thread_start
print(f'Работа потоков {time_res_2}')
