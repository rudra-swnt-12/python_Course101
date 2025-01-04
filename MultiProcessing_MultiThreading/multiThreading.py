"""
MULTI THREADING
- Multi-threading is a technique that allows a CPU to execute multiple tasks concurrently.
- In multi-threading, multiple threads share the same memory space and resources.
- Each thread has its own execution path.
"""


"""
When to use Multi Threading
- I/O-bound tasks: Tasks that spend more time waiting for I/O operations (e.g., file operations, network requests).
- Concurrent execution: When you want to improve the throughput of your application by performing multiple operations concurrently.
- Parallel Working: When you want to perform multiple tasks in parallel.
"""

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number:{i}")

def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter: {letter}")

#STEP 1: Create 2 threads
t1 = threading.Thread(target=print_numbers) 
# This will create a thread that will execute the print_numbers function

t2 = threading.Thread(target=print_letter)
# This will create a thread that will execute the print_letter function

t = time.time()

#STEP 2: Start the thread
t1.start()
t2.start()

#STEP 3: Wait for the threads to complete
t1.join()
t2.join()

finished_time = time.time()-t 
# time.time() returns the current time in seconds & t is the time before starting the threads
print(finished_time)