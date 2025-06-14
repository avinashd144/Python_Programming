# Exercise 4 - Python Pandas Exercise

#%% 1.	Write a Pandas program to create and display a one-dimensional array-like object containing an array of data using Pandas module.

import pandas as pd
data = pd.Series([3.0, 5, 7, 9])
print(data)

#%% 2.	Write a Pandas program to convert a Panda module Series to Python list and it's type. 

import pandas as pd
data = pd.Series([3.0, 5, 7, 9])
data_list = data.tolist()
print('data_list type: ',type(data_list))
print('data_list: ', data_list)

#%% 3.	Write a Pandas program to add, subtract, multiple and divide two Pandas Series. 
# Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]

import pandas as pd
s1 = pd.Series([2, 4, 6, 8, 10])
s2 = pd.Series([1, 3, 5, 7, 9])

# addition
addition = s1 + s2
print('Addition of the given series:\n',addition)

# subtract
subtract = s1 - s2
print('Subtract of the given series:\n',subtract)

# multiple
multiple = s1 * s2
print('multiple of the given series:\n',multiple)

# divide
divide = s1 / s2
print('divide of the given series:\n',divide)

#%% 4.	Write a Pandas program to compare the elements of the two Pandas Series. 
# Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 10]

import pandas as pd
s1 = pd.Series([2, 4, 6, 8, 10])
s2 = pd.Series([1, 3, 5, 7, 10])

# compare the elements of the two series
compare1 = s1 > s2
compare2 = s1 < s2
compare3 = s1 == s2

# printing the results
print("Series1 > Series2:\n", compare1)
print("\nSeries1 < Series2:\n", compare2)
print("\nSeries1 == Series2:\n", compare3)


#%% 5.	Write a Pandas program to convert a NumPy array to a Pandas series. 

import pandas as pd
import numpy as np

np_array = np.array([3.0, 5, 7, 9])

pd_data = pd.Series(np_array)

print("Pandas series:\n", pd_data)

#%% 6.	Write a Pandas program to change the data type of given a column or a Series.

import pandas as pd
data = pd.Series([3.0, 5, 7, 9.8])
print("Intial data: ", data)
print("Intial data type: ",type(data))

# Change type to int
data_int = data.astype(int)

print("Data after data type change: ",data_int)
print("Data type after data type change:",type(data_int))

#%% 7.	Write a Pandas program to convert the first column of a DataFrame as a Series.


import pandas as pd

# sample dataframe, form of dict
data = {'column1': [3, 5, 7, 9],
        'column2': [11, 13, 15, 17],
        'column3': [22, 33, 44, 55]}

data_frame = pd.DataFrame(data)

# Display the DataFrame
print("Original DataFrame:\n", data_frame)

# 1st column
column1 = data_frame.iloc[:, 0]

# 2nd column
column2 = data_frame.iloc[:, 1]

# 3rd column
column3 = data_frame.iloc[:, 2]

# Print the columns
print("\ncolumn1:\n", column1)
print("\ncolumn2:\n", column2)
print("\ncolumn3:\n", column3)

#%% 8.	Write a Pandas program to convert a dictionary to a Pandas series. 

import pandas as pd

# sample dictionary
data_dict = {'x': 3, 'y': 5, 'z': 7}
print(data_dict)

# adding as a Pandas series
data_pd = pd.Series(data_dict)
print(data_pd)


#%% 9.	Write a Pandas program to add some data to an existing Series. 

import pandas as pd

data = pd.Series([3.0, 5, 7, 9])
print("data: ",data)

add_data = pd.Series([11, 33])
print("add_data: ",add_data)

final_data = pd.concat([data, add_data])
print(final_data)

#%% 10.	Write a Pandas program to create a subset of a given series based on value and condition. 

import pandas as pd

data = pd.Series([3.0, 5, 7, 9])
print("data: ",data)

data_subset = data[data<9]

print("data set with less than 9 numbers: ",data_subset)

#%% 11.	Write a Pandas program to create a dataframe from a dictionary and display it. Sample data: {'X':[78,85,96,80,86],'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}

import pandas as pd 

# sample data

Sample_data = {
    'X':[78,85,96,80,86],
    'Y':[84,94,89,83,86],
    'Z':[86,97,96,72,83]
    }

print("Sample_data: \n",Sample_data)

data_frame = pd.DataFrame(Sample_data)
print("data_frame:\n",data_frame)


#%% 12.	Write a Pandas program to create and display a DataFrame from a specified dictionary data which has the index labels. 
#Sample Python dictionary data and list labels:
#exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
#'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
#'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
#'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
#labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

import pandas as pd
import numpy as np

exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
    }

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels)

print(df)

#%% 13.	Write a Pandas program to display a summary of the basic information about a specified DataFrame and its data. 

import pandas as pd
import numpy as np

exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
    }

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels)

print(df)
print("\nSummary \n:")
print(df.describe())

#%% 14.	Write a Pandas program to get the first 3 rows of a given DataFrame. 

import pandas as pd
import numpy as np

exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
    }

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels)

print(df)
print("\nSummary \n:")
print(df.describe())

column1_3 = df.iloc[:, 0:2]
print("First three columns: \n", column1_3)

rows1_3 = df.head(3)
print("First three rows: \n", rows1_3)


#%% 15.	Write a Pandas program to select the 'name' and 'score' columns from the following 

import pandas as pd
import numpy as np

exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
    }

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels)

print(df)
print("\nSummary \n:")
print(df.describe())

column1_3 = df.iloc[:, 0:2]
print("First three columns: \n", column1_3)

rows1_3 = df.head(3)
print("First three rows: \n", rows1_3)

selected_columns = df[['name', 'score']]
print("Print the selected columns: \n", selected_columns)

#%% 16.	Write a Pandas program to select the rows where the number of attempts in the examination is greater than 2. 

import pandas as pd
import numpy as np

exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
    }

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels)

print(df)

rows = df[df['attempts']>2]
print("rows where the number of attempts in the examination is greater than 2: \n", rows)

#%% 17.	Write a Pandas program to count the number of rows and columns of a DataFrame. 

import pandas as pd
import numpy as np

exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
    }

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels)

print(df)

num_rows, num_columns = df.shape

print("Number of rows:", num_rows, "\nNumber of columns:", num_columns)
#%% 18.	Write a Pandas program to select the rows the score is between 15 and 20 (inclusive).  

import pandas as pd
import numpy as np

exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
    }

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels)

print(df)

rows = df[(df['score']>=15) & (df['score']<=20)]


print("rows the score is between 15 and 20 (inclusive): \n", rows)


#%% 19.	Write a Pandas program to select the rows where number of attempts in the examination is less than 2 and score greater than 15. 

import pandas as pd
import numpy as np

exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
    }

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels)

print(df)

rows = df[(df['attempts']<2) & (df['score']>15)]


print("rows where number of attempts in the examination is less than 2 and score greater than 15. : \n", rows)

#%% 20.	Write a Pandas program to extract items at given positions of a given series. 

import pandas as pd

# Sample data
data = pd.Series([3.0, 5, 7, 9])

positions = [1, 3]

exctracted_items = data.iloc[positions]

print("extract items at given positions of a given series: \n", exctracted_items)

