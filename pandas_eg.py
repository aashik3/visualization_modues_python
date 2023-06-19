#introduction
'''Pandas is a Python library used for working with data sets.
It has functions for analyzing, cleaning, exploring, and manipulating data.'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

#1 series
'''#A Pandas Series is like a column in a table.
#It is a one-dimensional array holding data of any type

s1=pd.Series([72,54,58,76],index= ['a','b','c','d'])
s2=pd.Series([92,44,38,66],index= ['a','b','c','d'])

#sorting 
s2.sort_values(inplace=True)
s2.sort_index(inplace=True)
print(s2)
#head(19) gives the no. of headers mentioned from the table 
#tail(11) gives the no. of footers mentioned from the table 
print(s2.head(2))
print(s1.tail(3))

def square(x):
    return x*2
#inside the apply method we call specify the function name to be called
s3=s1.apply(square)
print(s3)

#you can pass the key value in squarebracket -- s1.loc['a'] -- to access value
#same like loc[] method iloc[] but you can specify the index directly here it is not possible in dictionary
print(s2.loc['d'])
#below statement print the 1st row and 4th row of th series 
print(s1.iloc[[0,3]])'''

#2 DataFrames

'''#A Pandas DataFrame is a 2 dimensional data structure,
# like a 2 dimensional array, or a table with rows and columns
data = {
    "index":[111,112,113,114],
  "name": ['aashik','dhina','vasim','manic'],
  "age": [22, 23, 24,25],
  "height": [150, 140, 145,160],
"gender": ['m', 'm', 'm','o']
}

df= pd.DataFrame(data)
df.set_index('index',inplace=True)
print(df)

#numpy basic attributes functions
print(df.size)
print(df.shape)
print(df.dtype)

#data frame indexing
#diff between iloc and loc is --iloc-- takes integers as input referring the index values
# where loc takes index values as input for fetching the required row

print(df.iloc[1]) , print(df.loc[113])
#this statement prints the 1st 3rd 4th row age and height column only
print(df.loc[[111,113,114],['age','height']]) #or print(df.iloc[[0,2,3],[1,2]])

print(df['age'].iloc[:,])
#plotting the dataframe
#df.plot.bar()
#df.height.plot()
#plt.show()'''

#one of the method for reading normal text file into csv file
'''with open('greetings','r') as csv_file:
    data_csv= csv.reader(csv_file)
    for x in data_csv:
        print(x)'''
#3 statistical function
'''
df= pd.read_csv('data')
#use to_string() to print the entire DataFrame. eg. print(df.to_string())
print(df.count()) # tells the no. of rows present in each columns
print(df.info()) # shows the total information about the file
print(df['Calories'].min())
print(df['Calories'].max())
#Mean = the average value (the sum of all values divided by number of values
print(df['Calories'].mean())
#Median = the value in the middle, after you have sorted all values ascending.
print(df['Calories'].median())
#Mode = the value that appears most frequently.
print(df['Calories'].mode())
print(df['Duration'].std())#std means standard deviation
#groupby
print(df.groupby(Duration.mean())
print(df.describe())# very important function'''

#sort by values
'''df= pd.read_csv('data',nrows=25)# nrows= limit the rows of a file
#skiprows=15-- skip the first mentioned rows and takes the other rows
df.sort_values(by=['Duration','Pulse'],inplace=True)
print(df)'''



#4 merging
'''data1 = {
    "index.no" :[11,12,13,14],
  "name": ["Sally", "Mary", "John","sonu"],
  "age": [50, 40, 30,22]
}

data2 = {
"index.no" :[10,12,15,14],
  "language": ["python", "java", "R","typescript"],
  "age": [77, 44, 22,42]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

df= pd.merge(df1,df2,on='index.no',how='outer')
# how= 'left','right','outer','inner' these are the types of merging 
df.set_index('index.no',inplace=True)
print(df)'''

#



