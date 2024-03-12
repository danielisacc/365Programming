"""
Programming exercise: Find the missing Number:
I am given an array containing n distinct numbers taken from 0...n.
However, one number is missing from the array.
Find the missing number from the unsorted list.

I would like to take a slightly more advanced approcah to this
classic interview question and use Multi-Threading to solve this issue.
Although some may choose to sort this list before searching the list,
Instead I am taking the approach of loading n numbers into a Queue object,
then using python's .contains() method with a Thread object.
"""

import queue as q
import threading
import time
import random as ran

q = q.Queue()
threads = []
num_list = []


def load_queue(list_length):
    for x in range(list_length):
        num_list.append(x)
    ran.shuffle(num_list)
    print("Unsorted Number List Generated with Missing Number!")
    del num_list[ran.randint(0, list_length)]

    for num in range(list_length):
        q.put(num)

    print("Queue loaded Successfully!")


def thread_term():
    for thread in threads:
        q.put(None)


def threaded_list_checker():
    while True:
        num = q.get()
        if num is None:
            print("Thread Broken!")
            break
        if num not in num_list:
            print(f"The missing number is... {num}!")
        q.task_done()


def thread_gen(num_threads: int = 5):
    for x in range(num_threads):
        thread = threading.Thread(target=threaded_list_checker)
        thread.start()
        threads.append(thread)
        print(f"Thread {x} started!")
    print("All Threads Running!")


def basic_list_checker():
    for num in range(len(num_list)+1):
        if num not in num_list:
            print(f"The missing number is... {num}!")


load_queue(10000000)

start = time.time()
thread_gen(3)
q.join()
thread_term()
end = time.time()
print(f"The Threaded Search took {end-start} time to complete!")

start = time.time()
basic_list_checker()
end = time.time()
print(f"The Basic Search took {end-start} time to complete!")
