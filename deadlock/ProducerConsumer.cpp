#include <iostream>
#include <queue>
#include <thread>
#include <mutex>
#include <condition_variable>

using namespace std;

const int BUFFER_SIZE = 5;
queue<int> buffer;
mutex mtx;
condition_variable cv;

void producer() {
    for (int i = 1; i <= 10; ++i) {
        this_thread::sleep_for(chrono::milliseconds(500)); // Simulate some work
        unique_lock<mutex> lock(mtx);
        cv.wait(lock, [] { return buffer.size() < BUFFER_SIZE; }); // Wait until buffer is not full
        buffer.push(i);
        cout << "Produced: " << i << endl;
        lock.unlock();
        cv.notify_all(); // Notify consumers that the buffer has changed
    }
}

void consumer(int id) {
    while (true) {
        this_thread::sleep_for(chrono::milliseconds(700)); // Simulate some work
        unique_lock<mutex> lock(mtx);
        cv.wait(lock, [] { return !buffer.empty(); }); // Wait until buffer is not empty
        int value = buffer.front();
        buffer.pop();
        cout << "Consumer " << id << " consumed: " << value << endl;
        lock.unlock();
        cv.notify_all(); // Notify producer that the buffer has changed
    }
}

int main() {
    thread producerThread(producer);
    thread consumerThread1(consumer, 1);
    thread consumerThread2(consumer, 2);

    producerThread.join();
    consumerThread1.join();
    consumerThread2.join();

    return 0;
}
