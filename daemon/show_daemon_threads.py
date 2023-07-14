import threading
import logging
import time 

def create():
    count = 1
    while True:
        print("Daemon thread is running!!!!")
        print(f"{count}")
        count += 1
        time.sleep(2)

#creating thread 
daemon = threading.Thread(target=create)
daemon.daemon = True

# start the daemon thread 
daemon.start()

try:
    while True:
        print("Main thread is running")
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Main thread recieved keyboard interrupt.Exiting...")