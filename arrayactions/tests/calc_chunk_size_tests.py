import os
import sys
import unittest


current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from calc_chunk_size import calc_chunk_size

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
