## Import required modules
import numpy as np 
import pandas as pd
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
import sqlite3

## Read the csv file
df_netflix = pd.read_csv('netflix_titles.csv')

## print the columns of all dataframes
print('The columns of the Netflix data frame are :-  ',df_netflix.columns)

# import sqlalchemy and create a sqlite engine
from sqlalchemy import create_engine
engine = create_engine('sqlite://', echo=False)

# export the dataframe as a table 'playstore' to the sqlite engine
df_netflix.to_sql("netflix", con =engine)

# Step 1: Create a dataframe from the csv file
netflix_mv_ratings = pd.read_csv('Netflix_datasets/netflix_movie_rating.csv', encoding='latin')

# Step 2: Create a reference for sql library
engine = create_engine('sqlite://',echo = False)
 
# Step 3: Attach the data frame to the sql library and name the table as "mv_ratings"
netflix_mv_ratings.to_sql('mv_ratings',con = engine)
