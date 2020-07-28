# dfs: DataFrame Services

### What is it?

**dfs** is a Python package built on top of Pandas providing an OOP approach
to simplify and reduce redundant coding for dataframe upload and manipulation

### Current Version:
1.1.3

### Main Features:
- A unified ```load_data``` method to simplify loading excel, csv, text and pickle file to a dataframe
- Change data type of dataframe columns
- Downcast dataframe columns variable type to reduce memory usage


### How to Install:
Currently dfs is in TestPyPI: https://test.pypi.org/project/dfs/

Pip install: ```pip install -i https://test.pypi.org/simple/ dfs```

### Dependencies
- Pandas

### Licence
- [licence.txt](https://github.com/shafin071/DataFrameServices/blob/master/dfs/license.txt)


### How it Works:
To instantiate an object:<br>
```data = DataFrameServices()```<br>
You can use ```load_data``` method to load your file into a dataframe

If you want to load your dataframe using pandas loading methods, you can pass in your dataframe as an argument<br>
```df = pd.read_csv('data_file.csv')``` <br>
```data = DataFrameServices(df) ```

 

#### Methods available:
```check_file_path```<br>
Checks if file path is valid<br>

Args:
- ```filepath: (str)```: <br>
&nbsp;file path of data file <br>

Returns:
- Bool. <br>
&nbsp;```True``` if ```filepath``` is valid, ```False``` if otherwise

Example:<br>
```data.check_file_path(filepath='files/example.csv')```<br>
```>> True```

<br>
<hr>
<br>

```load_data``` <br>
loads data file into pandas dataframe<br>

Args:
- ```filepath:``` _(str)_<br>
&nbsp;file path of data file<br><br>
- ```delimiter```: _(str), default: None_
[From pandas API documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)<br>
&nbsp;Delimiter to use. If sep is None, the C engine cannot automatically detect the separator, but the Python parsing engine can, meaning the latter will be used and automatically detect the separator by Python’s builtin sniffer tool, csv.Sniffer. In addition, separators longer than 1 character and different from '\s+' will be interpreted as regular expressions and will also force the use of the Python parsing engine. Note that regex delimiters are prone to ignoring quoted data. Regex example: '\r\t'.<br><br>
- ```header```: _(int, list of int), default 'infer'_ <br>
&nbsp;Row number(s) to use as the column names, and the start of the data. Default behavior is to infer the column names: if no names are passed the behavior is identical to header=0 and column names are inferred from the first line of the file, if column names are passed explicitly then the behavior is identical to header=None. Explicitly pass header=0 to be able to replace existing names. The header can be a list of integers that specify row locations for a multi-index on the columns e.g. [0,1,3]. Intervening rows that are not specified will be skipped (e.g. 2 in this example is skipped). Note that this parameter ignores commented lines and empty lines if skip_blank_lines=True, so header=0 denotes the first line of data rather than the first line of the file.<br><br>
- ```index_col```: _(int, str, sequence of int / str, or False), default None_ <br>
&nbsp;Column(s) to use as the row labels of the DataFrame, either given as string name or column index. If a sequence of int / str is given, a MultiIndex is used.
_Note_: index_col=False can be used to force pandas to not use the first column as the index, e.g. when you have a malformed file with delimiters at the end of each line.
- ```sheet_name:``` _(str, int, list, or None), default 0_<br>
&nbsp;Strings are used for sheet names. Integers are used in zero-indexed sheet positions. Lists of strings/integers are used to request multiple sheets. Specify None to get all sheets.<br>
Available cases:<br>
    - Defaults to ```0```: 1st sheet as a DataFrame
    - ```1```: 2nd sheet as a DataFrame
    - ```"Sheet1"```: Load sheet with name “Sheet1”
    - ```[0, 1, "Sheet5"]```: Load first, second and sheet named “Sheet5” as a dict of DataFrame
    - ```None```: All sheets.<br>

Returns:
- None

Example:<br>
```data.check_file_path(filepath='files/example.csv')```<br>
```data.df``` now holds the dataframe from the loaded file

<br>
<hr>
<br>

```change_dtype```<br>
Change ALL columns data type stated in ```cols``` to preferred ```to_dtype```
Best used for changing _Object_ type data to either _int_ or _float_<br>

Args:
- ```cols```: _(list of str)_<br>
&nbsp;list of dataframe columns to be converted<br><br>
- ```from_dtype```: _(str)_<br>
&nbsp;Pandas data type _['int64', 'float64', 'object', 'bool', 'datetime64', 'timedelta[ns]', 'category']_<br><br>
- ```to_dtype```: _(str)_<br>
&nbsp;Python data type _['int16', 'int32', 'int64', 'float16', 'float32', 'float64', 'str', 'bool']_<br><br>

Returns:
- None

Example:<br>
```data.df['col1'].dtypes```<br>
```>> object```<br>
```columns = ['col1', 'col2', 'col3']```<br>
```data.change_dtype(cols=columns, from_dtype='object', to_dtype='float64')```<br>
```data.df['col1'].dtypes```<br>
```>> float64```

<br>
<hr>
<br>

```reduce_memory_usage```<br>
Reduces memory usage of DataFrame by down-casting _int_ and _float_ variable types
The down-casting is done based on the range of values of the data

Range of values of data types can be found here: (scroll to the bottom)
https://jakevdp.github.io/PythonDataScienceHandbook/02.01-understanding-data-types.html

For example: Converts a DataFrame column series of type _int64_ to _int8_<br>

Args:
- ```verbose```: _(bool), default:True_<br>
&nbsp;if ```True```, prints how much memory usage was reduced after using this method<br>

Returns:
- None

Example:<br>
```data.df['col1'].dtypes```<br>
```>> int64```<br>
```data.reduce_memory_usage(verbose=True)```<br>
```>> Memory usage of dataframe reduced from 0.04 Mb to  0.02 Mb (47.5% reduction)```
```data.df['col1'].dtypes```<br>
```>> int8```<br>


### What's next?
More dataframe functionalities will be added  

