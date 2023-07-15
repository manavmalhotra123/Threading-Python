# Threading-Python
Tutorials of threading 

Thread Basics
- A thread is a flow of execution.


One Thread 
![image](https://github.com/manavmalhotra123/Threading-Python/assets/110531978/1effdf58-c6b3-4c1f-a635-0776658bae71)

Two Thread 
![image](https://github.com/manavmalhotra123/Threading-Python/assets/110531978/60dd6cf0-947c-45f4-ad2b-27ae518925c3)



Folder: BasicsOfThreading

files: 
1. gettting-started.py 
  contains the basics thread creation and calling it in main function 

2. two_threads.py
  contains the two thread system running in FCFS served order where thread 1 is waiting for thread 2 to finish before starting

3. prempt.py 
  code for demonstrating two treads run in preemptive order 

4. showPremp.py 
  code two demonstrate the working of two threads in preemptive order with time of 2 seconds with logs in the console

5. n_threads.py
  to create the n number of threads with the time duration defined by the user itself.

----------DAEMON THREADS : BACKGROUND THREADS-----------

Daemon Threads: A thread in the python that will immediately shutdown when the program exits. If a program is running threads that are not daemon, then the program will wait for those threads to finish before it terminates.

They are thread that are killed wherever they are when the program exits
Daemon threads are useful in situations where you have tasks that need to be performed continuously or in the background, but you don't want them to keep the program running indefinitely. 
For example, if you have a web server running as the main program and you want to have a separate thread to handle incoming requests, you can make that thread a daemon thread. 

Folder - Daemon
Daemon threads basics files; 

1. daemon_threads.py
How to create daemon threads 

2. show_daemon_threads.py
n this example, the daemon_task() function runs an infinite loop, printing a message every second. Meanwhile, the main_task() function is a countdown that prints the remaining seconds, with a delay of 1 second between each count.

----------- Thread Pool Executer------------
A thread pool executor is a concurrent programming construct that manages and reuses a pool of worker threads to execute tasks concurrently. It is a form of thread management that improves the efficiency of thread utilization and simplifies the process of managing threads in concurrent applications.

- helps to run the thread in concurrent applications where the pool of worker threads works on n number of tasks simultaneously

Folder - ThreadPoolExecutor

Files;
1.pool_executor.py 
contains the basic of pool executor 

2.file_download.py
contains the basics application of pool executor to download files in form of chunk 

------------ Race Conditions --------
It occurs when more than one thread working on same data simuntaneously which lead to inconsistency in data 

Folder RaceCondition 
File: 
1. fakedatabase.py 
contains the code without any race condition.

2. race_condition.py 
contains the code which is demonstrating the race condition as the copy of updating variable is not made which means 
they need to share the same variable

3.LockSync.py 
contains the code for locking mechanism for handling the synchronization
 