import logging
import threading
import time

# Thread function
def thread_function(name, duration):
    logging.info("Thread %s: starting", name)
    start_time = time.time()  # Record the start time

    while duration > 0:
        logging.info("Thread %s: running for %d seconds", name, duration)
        if duration == 8:
            time.sleep(2)  # Sleep for 2 seconds at the 8th second
        else:
            time.sleep(1)
        duration -= 1

    elapsed_time = time.time() - start_time  # Calculate elapsed time
    logging.info("Thread %s: finished in %d seconds", name, elapsed_time)

if __name__ == "__main__":
    # Configure logging format
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    # Main program starts here
    logging.info("Main    : before creating threads")

    # Create the first thread - thread 1
    x1 = threading.Thread(target=thread_function, args=(1, 10))

    # Create the second thread - thread 2
    x2 = threading.Thread(target=thread_function, args=(2, 10))

    logging.info("Main    : before running threads")

    # Start the first thread
    x1.start()

    # Sleep for approximately 2 seconds
    time.sleep(2)

    # Start the second thread
    x2.start()

    logging.info("Main    : wait for the threads to finish")

    # Wait for the first thread to finish
    x1.join()

    # Wait for the second thread to finish
    x2.join()

    logging.info("Main    : all done")
