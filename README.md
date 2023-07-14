# Threading-Python
Tutorials of threading 

Thread Basics
- A thread is a flow of execution.

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