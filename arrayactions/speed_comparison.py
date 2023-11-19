import timeit
import numpy as np

def calc_chunk_size_original(n_chunks, input_length):
    # Original implementation with for loop
    aprox_chunk_size, remainder = divmod(input_length, n_chunks)
    chunk_sizes = [aprox_chunk_size + 1 if i < remainder else aprox_chunk_size for i in range(n_chunks)]
    return chunk_sizes

def calc_chunk_size_optimized(n_chunks, input_length):
    # Optimized implementation using numpy
    aprox_chunk_size, remainder = divmod(input_length, n_chunks)
    chunk_sizes = np.full(n_chunks, aprox_chunk_size, dtype=int)
    chunk_sizes[:remainder] += 1
    return chunk_sizes.tolist()

def compare_speed(n_chunks, input_length, num_iterations=10000):
    # Measure the execution time of the original implementation
    original_time = timeit.timeit(lambda: calc_chunk_size_original(n_chunks, input_length), number=num_iterations)

    # Measure the execution time of the optimized implementation
    optimized_time = timeit.timeit(lambda: calc_chunk_size_optimized(n_chunks, input_length), number=num_iterations)

    print(f"Original implementation time: {original_time:.6f} seconds")
    print(f"Optimized implementation time: {optimized_time:.6f} seconds")

if __name__ == "__main__":
    # Beispielaufruf mit n_chunks = 100 und input_length = 1000
    compare_speed(1000, 100000)