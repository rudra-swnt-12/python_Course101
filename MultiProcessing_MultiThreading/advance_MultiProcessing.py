''' Multiprocessing with ProcessPoolExecutor
- ProcessPoolExecutor is a class in the concurrent.futures module that provides a simple high-level interface for asynchronously executing callables in multiple processes.
- The ProcessPoolExecutor class uses the multiprocessing module to create a pool of worker processes. The number of worker processes can be specified using the max_workers parameter.'''

from concurrent.futures import ProcessPoolExecutor
import time

def square_number(number):
    time.sleep(2)
    return f"Square: {number * number}"

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
if __name__=="__main__": 

    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square_number,numbers)

    for result in results:
        print(result)