from cantok import ConditionToken, SimpleToken, AbstractToken
import time
from random import randint
from threading import Thread
import os


class RedisService:
    def __init__(self):
        self.token = SimpleToken()

    def cancel_operation(self):
        self.token.cancel()

    def perform_task(self):
        print('async perform_task\n')
        time.sleep(2)
        if self.token.is_cancelled():
            print(f'action is not completed')
            return
        print('task is done')


def sum_values(a: int, b: int)->None:
    c = randint(1, 10)
    print(f'sum: {a}+{b}+{c} =', a + b + c, end='\n')

def wait_token_to_execute(token: AbstractToken, index: int, function, *args)->None:
    print('lunch function in await on signal from token\n')
    while not token.is_cancelled():
        time.sleep(0.1)
    print(f'\naction {index}')
    function(*args)

def main(index: int = 1)->None:
    token = SimpleToken()
    task_thread2 = Thread(target=wait_token_to_execute, args=(token, index, sum_values, 2, 3))
    task_thread2.start()
    while True:
        os.system("cls")
        print('go to sleep')
        time.sleep(2)
        print('go to wake up')
        token.cancel()

        if input('exit y/n:').lower().startswith('y'):
            break
        else:
            index += 1
            token = SimpleToken()
            task_thread2 = Thread(target=wait_token_to_execute, args=(token, index, sum_values, 2, 3))
            task_thread2.start()

    token.cancel()
    task_thread2.join()
    print('stop function')
