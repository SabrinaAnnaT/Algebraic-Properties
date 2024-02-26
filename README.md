# Algebraic-Properties
This project aims to experimentally verify the mathematical property that for two square matrices A and B, where B = cA (with c being a scalar), the equality AB = BA holds true. The project includes both a sequential and a parallel implementation using Python and NumPy.

# Implementation

Sequential Version
* Generates 10 random matrices of size N x N.
* Creates corresponding matrices by multiplying each by a scalar c.
* Tests the equality AB = BA for each pair of matrices.

Parallel Version
* Implements the verification in a parallel computing environment using Python's multiprocessing module.
* Uses T processes to verify the property in parallel, with T > 10.

## Setup and Parameters

* Matrix Size (N): 2000
* Scalar (c): 2
* Number of Threads (T): 12
* The values for N, c, and T are hard-coded to manage execution time. These values are chosen to ensure a balance between computational efficiency and program stability, as very high values of N can lead to extremely long execution times and risk crashing the program.

# Observations

* The parallel method demonstrates increased efficiency, particularly for larger values of N. This is due to the effective distribution of computation across multiple processors.
* For smaller matrices, the overhead of process creation and management in the parallel method may not justify its use over the sequential method.
* The choice of hard-coded values facilitates direct comparison between the sequential and parallel methods under specific conditions.

# Conclusions
The project successfully verifies the specified matrix multiplication property using both sequential and parallel approaches. The parallel method, while more complex, provides a significant performance advantage for large-scale matrix operations. 
