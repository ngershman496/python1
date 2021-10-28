import threading
from queue import Queue
import time

print_lock = threading.Lock()

def job(worker):
    time.sleep(3)
    with print_lock:
        print(threading.current_thread().name, worker)

def threader():
    while True:
        worker = q.get()
        job(worker)
        q.task_done()

q = Queue()

for x in range(10):
    t = threading.Thread(target = threader)
    t.daemon = True
    t.start()

start = time.time()

for worker in range(20):
    q.put(worker)

q.join()

print('Done')