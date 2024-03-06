import threading
import queue
import time

name_q = queue.Queue()
threads = []
names = []

def name_loader(file = "name_list.txt"):
    with open(file, "r") as names:
        for name in names:
            name_q.put(name)

def worker():
    while True:
        item = name_q.get()
        if item is None:
            break
        names.append(item)
        name_q.task_done()

def gen_threads(num_threads):
    for x in range(num_threads):
        thread = threading.Thread(target=worker)
        thread.start()
        threads.append(thread)

def term_threads():
    for thread in threads:
        name_q.put(None)


def threaded_print(num_threads = 5, file = "name_list.txt"):
    name_loader(file)
    start = time.time()

    gen_threads(num_threads)
    name_q.join()
    term_threads()

    end = time.time()
    print(end-start)

threaded_print()
