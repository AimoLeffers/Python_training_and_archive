import unittest
from arrayactions.calc_chunk_size import calc_chunk_size


class CalcChunkSizeTest(unittest.TestCase):
    def test_even_input_length_even_chunk_size(self):
        input_length = 10
        n_chunks = 2
        result = [5, 5]
        self.assertEqual(calc_chunk_size(n_chunks, input_length), result)

    def test_uneven_input_length_even_chunk_size(self):
        input_length = 11
        n_chunks = 2
        result = [6, 5]
        self.assertEqual(calc_chunk_size(n_chunks, input_length), result)

    def test_even_input_length_uneven_chunk_size(self):
        input_length = 10
        n_chunks = 3
        result = [4, 4, 2]
        self.assertEqual(calc_chunk_size(n_chunks, input_length), result)

    def test_uneven_input_length_uneven_chunk_size(self):
        input_length = 11
        n_chunks = 3
        result = [4, 4, 3]
        self.assertEqual(calc_chunk_size(n_chunks, input_length), result)


if __name__ == '__main__':
    unittest.main()
