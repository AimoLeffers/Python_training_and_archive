import pandas as pd


def append_dataframe(dataframe_1: pd.DataFrame, dataframe_2: pd.DataFrame) -> pd.DataFrame:
    """
    Appends two pandas dataframes and returns one dataframe.
    The dataframes must have the same column names and the same column order

    :param dataframe_1: first dataframe which data well be on first half of the new dataframe
    :param dataframe_2: second dataframe which data well be on second half of the new dataframe
    :return dataframe_3: resulting dataframe which holds the data from the two input dataframes
    """
    if not list(dataframe_1.columns) == list(dataframe_2.columns):
        raise ValueError('Names of the dataframe columns must be the same in each dataframe and in the same order')

    dataframe_3 = dataframe_1.append(dataframe_2, ignore_index=True)
    return dataframe_3


def concat_dataframe(dataframe_1: pd.DataFrame, dataframe_2: pd.DataFrame) -> pd.DataFrame:
    """
    Appends two pandas dataframes and returns one dataframe.
    The dataframes must have the same column names and the same column order

    :param dataframe_1: first dataframe which data well be on first half of the new dataframe
    :param dataframe_2: second dataframe which data well be on second half of the new dataframe
    :return dataframe_3: resulting dataframe which holds the data from the two input dataframes
    """
    if not list(dataframe_1.columns) == list(dataframe_2.columns):
        raise ValueError('Names of the dataframe columns must be the same in each dataframe and in the same order')

    dataframe_3 = pd.concat([dataframe_1, dataframe_2], ignore_index=True)
    return dataframe_3
