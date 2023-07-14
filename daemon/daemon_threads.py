import threading
import time

def daemon_thread():
    while True:
        print("Daemon thread is running.........")
        time.sleep(1)

Daemon = threading.Thread(target=daemon_thread)
Daemon.daemon = True
Daemon.start()

# the main program continues here 
time.sleep(10)
print("Main is finishd!!")