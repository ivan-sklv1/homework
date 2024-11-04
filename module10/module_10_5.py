import threading
import multiprocessing
import os
from datetime import datetime


def read_info(name):
    
    all_data = []
    with open(name, 'r') as file:
        for line in file:
            line = file.readline()
            all_data.append(line)

files = [f'./file {number}.txt' for number in range(1, 5)]

start = datetime.now()

for file in files:
    read_info(file)

end = datetime.now()

res = end - start
print(f'{res} линейный')

start_multi = datetime.now()
if __name__ == '__main__':
    
    
    with multiprocessing.Pool() as pool:
        pool.map(read_info, files)
    
end_multi = datetime.now()
print(f'{end_multi - start_multi} многопроцессный')
