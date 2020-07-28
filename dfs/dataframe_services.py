import errno
import os
import warnings

import numpy as np
import pandas as pd


class DataFrameServices():
    def __init__(self, df=None):
        '''
        Initialize DataFrameServices class
        Args:
            - df: DataFrame. If you want to load your df externally and still use this class

        '''
        self.df = df
        self.python_dtypes = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64', 'str', 'bool']
        self.pandas_dtypes = ['int64', 'float64', 'object', 'bool', 'datetime64', 'timedelta[ns]', 'category']



    def check_file_path(self, filepath):
        '''
        Checks if file path is valid
        Args:
            filepath (str)
        Returns:
            True / False (Bool)
        '''
        print(filepath)
        return os.path.exists(filepath)



    def load_data(self, filepath, delimiter=',', header='infer', index_col=None, sheet_name=0):
        '''
        Loads data from excel, csv, tsv, or txt file

        Args:
            - filepath (str): path and name of file to be loaded
            - format (str): format of loaded file

        Returns: None

        '''
        file_extensions = {
            'excel_extension' : ['.xls', '.xlsb', '.xlsm', '.xlsx'],
            'csv_extension' : '.csv',
            'tsv_extension' : '.tsv',
            'textfile_extension' : '.txt',
            'pickle_extension' : '.pkl'
        }

        if self.df is not None:
            warnings.warn('Using this method will overwrite your current DataFrame')

        file_dir, file_extension = os.path.splitext(filepath)


        if self.check_file_path(filepath):
            if file_extension in file_extensions['excel_extension']:
                self.df = pd.read_excel(filepath, header=header,  sheet_name=sheet_name )

            elif file_extension == file_extensions['csv_extension']:
                self.df = pd.read_csv(filepath, delimiter=delimiter, header=header, index_col= index_col)

            elif file_extension == file_extensions['tsv_extension']:
                self.df = pd.read_csv(filepath, delimiter='\t', header=header, index_col= index_col)

            elif file_extension == file_extensions['textfile_extension']:
                self.df = pd.read_csv(filepath, delimiter=" ", header=header, index_col= index_col)

            elif file_extension == file_extensions['pickle_extension']:
                self.df = pd.read_pickle(filepath)

            else:
                raise ValueError(f'Invalid file format.  Accepted format= {[ext for ext in file_extensions.values()]}.')

        else:
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), filepath)



    def change_dtype(self, cols, from_dtype, to_dtype):
        '''
        Change ALL columns data type stated in cols to preferred to_dtype
        Best used for changing Object type data to either int or float
        Args:
            - cols (list of str): list of df columns
            - from_dtype (str): Pandas data type ['int64', 'float64', 'object', 'bool', 'datetime64', 'timedelta[ns]', 'category']
            - to_dtype (str): Python data type ['int16', 'int32', 'int64', 'float16', 'float32', 'float64', 'str', 'bool']
        Returns: None
        '''

        if from_dtype not in self.pandas_dtypes:
            raise TypeError('from_dtype is not recognized. '
                            'Acceptable dtypes: int64, float64, object, bool, datetime64, timedelta[ns], category')

        if to_dtype not in self.python_dtypes:
            raise TypeError('from_dtype is not recognized. '
                            'Acceptable dtypes: int16, int32, int64, float16, float32, float64, str, bool')

        for col in cols:
            if self.df[col].dtype == from_dtype:
                self.df[col] = self.df[col].astype(to_dtype)





    def reduce_memory_usage(self, verbose=True):
        '''
        Reduces memory usage of DataFrame by down-casting INT and FLOAT variable types
        The down-casting is done based on the range of values of the data

        Range of values of data types can be found here: (scroll to the bottom)
        https://jakevdp.github.io/PythonDataScienceHandbook/02.01-understanding-data-types.html

        For example: Converts a DataFrame column series of type int64 to int8

        Args:
            verbose (Bool): if True, prints reduction in memory usage

        Returns:
            None
        '''

        df = self.df

        start_mem = df.memory_usage().sum() / 1024 ** 2

        for col in df.columns:
            col_type = df[col].dtypes

            if col_type in self.python_dtypes:
                c_min = df[col].min()
                c_max = df[col].max()

                if str(col_type)[:3] == 'int':
                    if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                        df[col] = df[col].astype(np.int8)
                    elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                        df[col] = df[col].astype(np.int16)
                    elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                        df[col] = df[col].astype(np.int32)
                    elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                        df[col] = df[col].astype(np.int64)

                else:
                    if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
                        df[col] = df[col].astype(np.float16)
                    elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                        df[col] = df[col].astype(np.float32)
                    else:
                        df[col] = df[col].astype(np.float64)

        end_mem = df.memory_usage().sum() / 1024 ** 2

        if verbose:
            print('Memory usage of dataframe reduced from {:5.2f} Mb to {:5.2f} Mb ({:.1f}% reduction)'.format(start_mem, end_mem, 100 * (start_mem - end_mem) / start_mem))

        self.df = df



