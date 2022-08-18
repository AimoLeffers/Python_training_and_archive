import unittest
import pandas as pd
import pandas_dataframes.pd_concat_vs_append


class TestAppendDataframe(unittest.TestCase):
    def test_wrong_column_names(self):
        test_data_1 = {
            'A': [10, 20],
            'B': [30, 40]
        }
        df1 = pd.DataFrame(test_data_1)

        test_data_3 = {
            'B': [50, 60],
            'A': [70, 80]
        }
        df2 = pd.DataFrame(test_data_3)

        test_data_4 = {
            'X': [50, 60],
            'Y': [70, 80]
        }
        df3 = pd.DataFrame(test_data_4)

        self.assertRaises(ValueError, pandas_dataframes.pd_concat_vs_append.append_dataframe, df1, df2)
        self.assertRaises(ValueError, pandas_dataframes.pd_concat_vs_append.append_dataframe, df3, df2)
        self.assertRaises(ValueError, pandas_dataframes.pd_concat_vs_append.append_dataframe, df1, df3)

    def test_expected_input(self):
        test_data_1 = {
            'A': [10, 20],
            'B': [30, 40]
        }

        test_data_2 = {
            'A': [50, 60],
            'B': [70, 80]
        }

        expected_data_1 = {
            'A': [10, 20, 50, 60],
            'B': [30, 40, 70, 80]
        }

        df1 = pd.DataFrame(test_data_1)
        df2 = pd.DataFrame(test_data_2)
        expected_data_df = pd.DataFrame(expected_data_1)
        resulting_data_df = pandas_dataframes.pd_concat_vs_append.append_dataframe(df1, df2)
        pass
        self.assertEqual(True, expected_data_df.equals(resulting_data_df))


class TestConcatDataframe(unittest.TestCase):
    def test_wrong_column_names(self):
        test_data_1 = {
            'A': [10, 20],
            'B': [30, 40]
        }
        df1 = pd.DataFrame(test_data_1)

        test_data_3 = {
            'B': [50, 60],
            'A': [70, 80]
        }
        df2 = pd.DataFrame(test_data_3)

        test_data_4 = {
            'X': [50, 60],
            'Y': [70, 80]
        }
        df3 = pd.DataFrame(test_data_4)

        self.assertRaises(ValueError, pandas_dataframes.pd_concat_vs_append.concat_dataframe, df1, df2)
        self.assertRaises(ValueError, pandas_dataframes.pd_concat_vs_append.concat_dataframe, df3, df2)
        self.assertRaises(ValueError, pandas_dataframes.pd_concat_vs_append.concat_dataframe, df1, df3)

    def test_expected_input(self):
        test_data_1 = {
            'A': [10, 20],
            'B': [30, 40]
        }

        test_data_2 = {
            'A': [50, 60],
            'B': [70, 80]
        }

        expected_data_1 = {
            'A': [10, 20, 50, 60],
            'B': [30, 40, 70, 80]
        }

        df1 = pd.DataFrame(test_data_1)
        df2 = pd.DataFrame(test_data_2)
        expected_data_df = pd.DataFrame(expected_data_1)
        resulting_data_df = pandas_dataframes.pd_concat_vs_append.concat_dataframe(df1, df2)
        self.assertEqual(True, expected_data_df.equals(resulting_data_df))
