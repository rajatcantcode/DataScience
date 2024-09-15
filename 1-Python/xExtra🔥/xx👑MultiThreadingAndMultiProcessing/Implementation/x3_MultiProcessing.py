# We are running because Some issues is happening with Jupyter Notebook


import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Square: {i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Cube: {i * i * i}")

# It is mandatory to use the if __name__ == '__main__': to avoid the error
# used to avoid recursive process creation

if __name__ == '__main__':
    # Create processes
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    t = time.time()

    # Start the processes
    p1.start()
    p2.start()

    # Wait for the processes to finish
    p1.join()
    p2.join()

    print("Time taken:", time.time() - t)