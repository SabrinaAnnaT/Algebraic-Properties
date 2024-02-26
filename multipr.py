import numpy as np
import time
import multiprocessing as mp

# Print some context
print("Given two square matrices A and B, it is generally not true that AB = BA.")
print("However, if B = cA, where c is a scalar, then AB = BA holds.")
print("Let't verify it sperimetally!")

try:
        N = 2000
        c = 2
except ValueError:
	raise ValueError("Invalid input type. Please enter an integer for N and a float for c.")

def verify_property(N, c):
    for _ in range(10):
        A = np.random.rand(N, N)
        B = c * A
        AB = np.dot(A, B)
        BA = np.dot(B, A)
        if not np.allclose(AB, BA):
            return False
    return True

# Compute the execution time
start = time.time()

# Test the property
result = verify_property(N, c)

# Calculate the execution time
execution_time = time.time() - start

# Print the results and the execution time
if result:
    print("The hypothesis holds true.")
else:
    print("The hypothesis does not hold true.")

print("Sequential execution time:", execution_time, "seconds")

try:
        N = 2000
        c = 2
        T = 12
except ValueError:
	raise ValueError("Invalid input type. Please enter an integer for N and a float for c.")


def test_property(A, B, task_queue, result_queue):
    while True:
        i = task_queue.get() # Get a task
        if i is None: # If all tasks are finished, exit
            break
          
        # Check the i-th row of A*B and B*A
        if not np.allclose(np.dot(A[i], B[:, i]), np.dot(B[i], A[:, i])):
            return result_queue.put(False)
        result_queue.put(True)

def verify_property(N, c):
    for _ in range(10):
        A = np.random.rand(N, N)
        B = c * A
        
        task_queue = mp.Queue() # Queue that contains task
        result_queue = mp.Queue() # Queue that contains each task's result
        
        processes = []
        for i in range(N):
             task_queue.put(i) # Each task represents a row to check
            
        for _ in range(T): # The last T tasks are None, a sentinel value to signify task completion
             task_queue.put(None)
        
        # task_queue = [0,1,2,3,4,5,.....N-1, None, None, None... ] 

        for _ in range(T): # Creation of T processes
             p = mp.Process(target=test_property, args=(A, B, task_queue, result_queue))
             p.start()
             processes.append(p) # Add the processes' list
        
        for p in processes:
             p.join() # Wait for all processes to complete
        
        result=all(result_queue.get() for _ in range(T))
        if not result:
             return False
    return True

try: 
    mp.set_start_method('fork')
except Exception:
    pass

# Compute the execution time
start = time.time()

# Test the property
result = verify_property(N, c)

# Calculate the execution time
execution_time = time.time() - start

# Print the results and the execution time
if result:
    print("The hypothesis holds true.")
else:
    print("The hypothesis does not hold true.")

print("Parallel execution time:", execution_time, "seconds")
