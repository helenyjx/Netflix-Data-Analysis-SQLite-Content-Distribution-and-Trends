
## Import required modules
from sqlalchemy import create_engine
import pandas as pd

# Step 1: Create a dataframe from the csv file
df_netflix = pd.read_csv('netflix_titles.csv', encoding='latin')

# Step 2: Create a sqlite engine
engine = create_engine('sqlite://',echo = False)
 
# Step 3: Attach the data frame to the sql library and name the table as "mv_ratings"
netflix_mv_ratings.to_sql('mv_ratings',con = engine)


# export the dataframe as a table 'playstore' to the sqlite engine
df_netflix.to_sql("netflix", con =engine)