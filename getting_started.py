import logging
import threading
import time

# Thread function
def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    # Configure logging format
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    # Main program starts here
    logging.info("Main    : before creating thread")

    # Create a new thread
    x = threading.Thread(target=thread_function, args=(1,))

    logging.info("Main    : before running thread")
    
    # Start the thread
    x.start()

    logging.info("Main    : wait for the thread to finish")
    # x.join()

    logging.info("Main    : all done")
