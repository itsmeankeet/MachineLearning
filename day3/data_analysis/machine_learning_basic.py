# step 1: Viewing the data
'''
1. load data 
2. view data 
        .head()
        .tail()
        .shape
        .colums
2. summarize the data  
        .describe()
        .info()
        .unique()
'''

#step 2: cleanig the data
'''
1. Handle the missing values
    find the missing values
        .isnull().sum()
        .isnull().mean()
        .isnull().any()
    Options to deals with missing values
        - drop the column/rows
        - fill the missing values
        - fillna()
2. Hanlde the duplicate datas 
    find the duplicate data
        .duplicated().sum()
        .duplicated().any()
    - drop the duplicate values 
        .drop_duplicates()
3.Fixed Datatype
    Check datatypes 
        .dtypes
    Convert the datatypes if necessary
        .astype(int/float)
'''
