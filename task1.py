from queue import Queue
from faker import Faker
import random
import time
import sys
import os

def generate_request(queue, data):
    print('Додаємо заявки .. ', end="", flush=True)
    for i in range(1,random.randint(5, 9)):   
        time.sleep(1)
        request = {'id': i, 'name': data.name()}
        queue.put(request)
        print(i, end=" ", flush=True)
    print('\n')    

def process_request(queue):
    while not queue.empty():
        current_request = queue.get()
        print(f"Обробляємо заявку №{current_request['id']} від клієнта {current_request['name']} ...")
        time.sleep(1)
    else:
        print('Черга пуста\n')

def main():
    q = Queue()
    f = Faker()
    while True:
        # Додаємо заявки
        generate_request(q, f)
        time.sleep(2)
        
        # Обробляємо заявки
        process_request(q)
        time.sleep(3)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)