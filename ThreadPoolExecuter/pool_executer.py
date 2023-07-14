# Code demonstates the working of three threads in concurrency to whom 10 task are assigned 


from concurrent.futures import ThreadPoolExecutor
import threading

# function to executed by the worker threads 
def task(task_number):
    thread_name = threading.currentThread().name
    print(f"Task {task_number} executed by {thread_name}")


# creating a thread pool - of 3 threads decided by max_workers
executor = ThreadPoolExecutor(max_workers=3)


# number of tasks to assign
for i in range(10):
    task_number = i + 1
    executor.submit(task,task_number)


executor.shutdown()