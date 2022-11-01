## Import required modules
import csv
import sqlite3

## Step 1: Connect to the netflix_titles database
connection = sqlite3.connect('netflix_titles.db')

## Step 2: Create a cursor object to execute SQL queries on the netflix_titles database
cursor = connection.cursor()

## Step 3: Define table schema for the new table netflix_type
# create_table = '''CREATE TABLE netflix_types(
# 				show_id VAR PRIMARY KEY,
# 				type VAR,
# 				title VAR,
# 				director VAR,
# 				cast VAR,
# 				country VAR,
# 				date_added DATE,
# 				release_year DATE,
# 				rating VAR,
# 				duration VAR,
# 				listed_in VAR,
# 				description VAR
# 				);
# 				'''

## Step 4: Insert the new table into the original database, then insert data into table netflix_type by using SQL query
# ursor.execute(new_table)
# insert_data = "INSERT INTO netflix_types (show_id, type, title, director,cast,country,date_added,release_year,rating,duration,listed_in,description) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

## Step 5: Read each record from netflix_titles.csv file and import its records to new table netflix_type
# file = open('netflix_titles.csv')
# records = csv.reader(file)
# cursor.executemany(insert_data, records)

### Query 1: Find top five production countries with the most TV Show in Netlfix
query1 = """SELECT Distinct country, count(type) 
		   FROM nfxtitle
		   WHERE country != '' AND type='TV Show'
		   Group by country
		   Order by count(title) DESC
		   LIMIT 5;"""
top5_tv_country = cursor.execute(query1).fetchall()


### Query 2: Find top five production countries with the most movie in Netlfix
query2 = """SELECT Distinct country, count(type) 
		   FROM nfxtitle
		   WHERE country != '' AND type='Movie'
		   Group by country
		   Order by count(title) DESC
		   LIMIT 5;"""
top5_movie_country = cursor.execute(query2).fetchall()


## Step 10: Output to the console screen
###FROM Query 1
print('#'* 50)
print(f"Top five production countries with the most TV Show in Netlfix:")
for i in top5_tv_country:
    print(i)

###FROM Query 2
print('#'* 50)
print(f"Top five production countries with the most movie in Netlfix:")
for j in top5_movie_country:
	print(j)

## Step 11: Commit the changes
connection.commit()

## Step 12: Close the database connection
connection.close()