from cantok import TimeOutToken, SimpleToken
import asyncio
import time
from threading import Thread
from token_service import RedisService, wait_token_to_execute, sum_values
from token_service import main

# r_service = RedisService()
# task_thread = Thread(target=r_service.perform_task)

if __name__ == '__main__':

    print('hello python cantok')
    # run independent threads: variant 1

    # task_thread.start()
    # print('start task of RedisService')
    # time.sleep(1)
    # r_service.cancel_operation()
    # print('end of task of RedisService')
    # task_thread.join()

    # run independent threads: variant 2
    main()