import numpy as np
from typing import List

def main():
    print(calc_chunk_size(19, 164))


def calc_chunk_size(n_chunks: int, input_length: int) -> List[int]:
    """
    Calculate the size of each chunk for dividing a dataset into a specified
    number of chunks.

    Parameters:
    - n_chunks (int): The desired number of chunks.
    - input_length (int): The total length of the dataset.

    Returns:
    - List[int]: A list containing the calculated size for each chunk.

    Raises:
    - ValueError: If the number of chunks requested is greater than the length
      of the dataset, or if either n_chunks or input_length is non-positive.

    The function calculates the approximate size of each chunk by dividing
    the total length of the dataset by the specified number of chunks.
    The actual sizes are then determined, ensuring that each chunk is as
    evenly distributed as possible, and the remaining rows are accommodated.

    Example:
    >>> calc_chunk_size(3, 10)
    [4, 3, 3]
    """
    if n_chunks > input_length:
        raise ValueError("Number of chunks requested is greater than the length of the dataset.")
    
    if n_chunks <= 0 or input_length <= 0:
        raise ValueError("Invalid input. Number of chunks and input length must be positive integers.")

    # Calculate the approximate size of each chunk and the remainder
    aprox_chunk_size, remainder = divmod(input_length, n_chunks)

    # Create a NumPy array with pre-defined sizes for each chunk
    # The majority of chunks have the approximate size 'aprox_chunk_size'
    chunk_sizes = np.full(n_chunks, aprox_chunk_size, dtype=int)

    # Add 1 to the first 'remainder' chunks to distribute the remainder
    chunk_sizes[:remainder] += 1

    # Convert the NumPy array to a Python list and return it
    return chunk_sizes.tolist()

if __name__ == "__main__":
    main()
