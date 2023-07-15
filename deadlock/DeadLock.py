import threading 

lock = threading.Lock()
print("Before the lock is acquired")
lock.acquire()
print("Before second lock acquired")
lock.acquire()

# here the lock program will stuck at first lock as the conditon of deadlock is there now which is not giving the access to acquire the other lock 

# output:
#Before the lock is acquired
#Before second lock acquired