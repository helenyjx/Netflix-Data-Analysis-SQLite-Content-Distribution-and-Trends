import numpy as np 
import pandas as pd
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
import pandas as pd
import sqlite3

## Read the file
df_netflix = pd.read_csv('netflix_titles.csv')

## print the columns of all dataframes
print('The columns of the Netflix data frame are :-  ',df_netflix.columns)

# import sqlalchemy and create a sqlite engine
from sqlalchemy import create_engine
engine = create_engine('sqlite://', echo=False)

# export the dataframe as a table 'playstore' to the sqlite engine
df_netflix.to_sql("netflix", con =engine)
