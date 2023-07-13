import threading
import logging
import time

# creating a function that will work on different time durations as set by the user
def create(name, duration):
    logging.info(f"Thread {name} : starting")
    time.sleep(duration)
    logging.info(f"Thread {name} : completed in {duration} seconds")

if __name__ == "__main__":
    import logging
    import time

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    # main program starting here
    logging.info("Main Thread: before creating any threads")

    # taking the number of threads user want to create
    numberOfThreads = int(input("Enter the number of threads you want to create: "))

    # as thread is a kind of object so we need to create an empty list for it
    THREADS = []

    # creating and starting threads
    for i in range(numberOfThreads):
        duration = int(input(f"Enter the duration of thread {i+1}: "))
        t = threading.Thread(target=create, args=(i+1, duration))
        # adding the created thread to list we created before
        THREADS.append(t)
        # after adding it to list we need to start that thread
        t.start()

    logging.info("Main  : before running threads")
    logging.info("Main  : Waiting for threads to finish")

    for thread in THREADS:
        thread.join()

    logging.info("Main    : All done !!!!!!!")
