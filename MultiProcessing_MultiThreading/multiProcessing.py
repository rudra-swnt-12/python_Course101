'''
MULTIPROCESSING
- Processes that run in parallel
- Each process has its own memory space
'''

'''
When to use:
- CPU-Bound Tasks - Tasks that are heavy on CPU usage (e.g., mathematical computations, data processing).
- Parallel execution - Multiple cores of the CPU
'''
import multiprocessing

import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube: {i * i * i}")

if __name__=="__main__": # This is used to prevent the code from running when the module is imported
    # Create 2 processes
    p1=multiprocessing.Process(target=square_numbers)
    p2=multiprocessing.Process(target=cube_numbers)
    t=time.time()

    # Start the process
    p1.start()
    p2.start()

    # Wait for the process to complete
    p1.join()
    p2.join()

    finished_time=time.time()-t
    print(finished_time)