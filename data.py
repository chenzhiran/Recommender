"""Definition of the Data class.

This module contains the definition of the Data class.
"""


import pandas as pd


class Data:
    """Data class with ``users``, ``items``, and ``ratings`` information.
    
    Attributes:
        users: data frame containing users information
        items: data frame containing items information
        ratings: data frame containing the users` ratings of the items
    """

    def __init__(self, user_files=None, user_cols=None, item_files=None, item_cols=None, rating_files=None,
                 rating_cols=None):
        """Initialize Data with ``users``, ``items``, and ``ratings`` information.
        
        :param user_files: list of user file names
        :param user_cols: list of user column names
        :param item_files: list of item file names
        :param item_cols: list of item column names
        :param rating_files: list of rating file names
        :param rating_cols: list of rating column names
        """
        self.users = self.__read_data(user_files, user_cols)
        self.items = self.__read_data(item_files, item_cols)
        self.ratings = self.__read_data(rating_files, rating_cols)

    @staticmethod
    def __read_data(files=None, cols=None):
        """Read multiple files as data frames and concatenate them as one data frame.
        
        :param files: list of file names
        :param cols: list of column names
        :return: data frame
        """
        if files is not None:
            if cols is None:
                cols = []
            dfs = [pd.read_table(file, names=cols) for file in files]
            df = pd.DataFrame(pd.concat(dfs, ignore_index=True))
            return df
        else:
            return None
