import logging 
import time 
import threading

def my_thread(name):
    logging.info(f"Thread {name} : starting")
    time.sleep(10)
    logging.info(f"Thread {name} : finished")


if __name__ == "__main__":
    # configure the logging format 
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    
    # maing program start here
    logging.info("Starting the main thread...")

    # creating the thread 1 
    x1 = threading.Thread(target=my_thread, args=(1,))

    # creating the thread 2 
    x2 = threading.Thread(target=my_thread, args=(2,))

    logging.info("Threads initialized")

    x1.start() # thread started

    x2.start() # thread started

    logging.info("Main : Waiting for threads to finish...")

    # make the thread 2 waiting for thread 1 to finish 
    x1.join()

    x2.join()

    logging.info("All threads are finished!!!")

