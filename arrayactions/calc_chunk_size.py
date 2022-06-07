import math


def main():
    print(calc_chunk_size(10, 2))


def calc_chunk_size(n_chunks: int, input_length: int):
    """
    :param n_chunks: Number of chunks in that the input length will be splitted
    :param input_length: complete length of the element that will be splitted
    :return: list with chunk sizes
    """
    chunk_sizes = []

    aprox_chunk_size = int(math.ceil(input_length / n_chunks))
    df_rows_left = input_length

    for ii in range(n_chunks):
        if df_rows_left > aprox_chunk_size:
            chunk_sizes.append(aprox_chunk_size)
            df_rows_left = df_rows_left - aprox_chunk_size
            continue

        if df_rows_left <= aprox_chunk_size:
            chunk_sizes.append(df_rows_left)
            continue

    return chunk_sizes


if __name__ == "__main__":
    main()
