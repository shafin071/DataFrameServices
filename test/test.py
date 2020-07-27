import unittest
import pandas as pd
import numpy as np
from ..dfs.dataframe_services import DataFrameServices



class TestDataFrameServices(unittest.TestCase):

    def setUp(self):
        self.data = DataFrameServices()


    def test_file_type(self):
        '''
        Tests if the load_data method is treating the file types correctly
        '''
        # Base case
        self.data.load_data(filepath='data_files/example.txt')
        self.assertEqual(isinstance(self.data.df, pd.DataFrame), True, '\ntest_file_type 1: Provided file format is not acceptable')

        self.data.load_data(filepath='data_files/example.csv')
        self.assertEqual(isinstance(self.data.df, pd.DataFrame), True, '\ntest_file_type 2: Provided file format is not acceptable')

        # Edge case: Unacceptable file format
        self.assertRaises(ValueError, lambda: self.data.load_data(filepath='data_files/example.jpg'))



    def test_file_path(self):
        '''
        Tests if the filepath and file name exists and they are correct
        '''
        # Base case: Correct file path
        self.assertEqual(self.data.check_file_path('data_files/example.txt'), True, '\ntest_file_path 1: file path does not exist')

        # Test cases: Incorrect file path
        self.assertEqual(self.data.check_file_path('data_filessss/example.txt'), False, '\ntest_file_path 1: file path does not exist')
        self.assertEqual(self.data.check_file_path('example.csv'), False, '\ntest_file_path 1: file path does not exist')
        self.assertEqual(self.data.check_file_path('example.pql'), False, '\ntest_file_path 1: file path does not exist')


    def test_change_dtype(self):
        '''
        Test functionality of change_dtype
        '''
        self.data.load_data(filepath='data_files/Automobile_data.csv')
        columns = ['normalized-losses', 'bore', 'stroke', 'horsepower', 'peak-rpm', 'price']
        self.data.df.replace('?', np.NaN, inplace=True)

        # Base Case
        self.data.change_dtype(cols=columns, from_dtype='object', to_dtype='float64')
        self.assertEqual(self.data.df['bore'].dtype, 'float64', '\ntest_change_dtype 1: dtype conversion failed')

        # Edge Case
        self.assertRaises(TypeError, lambda: self.data.change_dtype(cols=columns, from_dtype='object', to_dtype='float40'))
        self.assertRaises(TypeError, lambda: self.data.change_dtype(cols=columns, from_dtype='', to_dtype='float64'))
        self.assertRaises(TypeError, lambda: self.data.change_dtype(cols=columns, from_dtype='object', to_dtype=''))
        self.assertRaises(TypeError, lambda: self.data.change_dtype(cols=columns, from_dtype='', to_dtype=''))
        self.assertRaises(TypeError, lambda: self.data.change_dtype(cols=columns, from_dtype='float8', to_dtype='float64'))


    def test_reduce_mem_usage(self):
        '''
        Test if the int & float type variables are being down-casted correctly
        '''
        self.data.load_data(filepath='data_files/Automobile_data.csv')
        self.data.df.replace('?', np.NaN, inplace=True)
        self.data.change_dtype(cols=['normalized-losses', 'bore', 'horsepower', 'stroke', 'peak-rpm', 'price'],
                               from_dtype='object', to_dtype='float64')

        # Before mem reduction:
        self.assertEqual(self.data.df['price'].dtypes, 'float64', '\ntest_reduce_mem_usage before 1: dtype did not match')
        self.assertEqual(self.data.df['stroke'].dtypes, 'float64', '\ntest_reduce_mem_usage before 2: dtype did not match')
        self.assertEqual(self.data.df['engine-size'].dtypes, 'int64', '\ntest_reduce_mem_usage after 3: dtype did not match')
        self.data.reduce_memory_usage(verbose=False)

        # After mem reduction:
        self.assertEqual(self.data.df['price'].dtypes, 'float16', '\ntest_reduce_mem_usage after 1: dtype did not match')
        self.assertEqual(self.data.df['stroke'].dtypes, 'float16', '\ntest_reduce_mem_usage after 2: dtype did not match')
        self.assertEqual(self.data.df['engine-size'].dtypes, 'int16', '\ntest_reduce_mem_usage after 3: dtype did not match')





if __name__ == '__main__':
    unittest.main()


