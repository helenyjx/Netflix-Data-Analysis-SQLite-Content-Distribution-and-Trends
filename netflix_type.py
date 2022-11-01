## Import required modules
import csv
import sqlite3

## Step 1: Do SQL queries via a cursor after connecting to netflix_titles database
connects = sqlite3.connect('netflix_titles.db')
cursor = connects.cursor()

## Step 3: Create a new table called netflix_type1
new_table = '''CREATE TABLE netflix_type1(
 				show_id VAR PRIMARY KEY,
 				type VAR,
 				title VAR,
 				director VAR,
 				cast VAR,
 				country VAR,
 				date_added DATE,
 				release_year DATE,
 				rating VAR,
 				duration VAR,
 				listed_in VAR,
 				description VAR
 				);
 				'''

## Step 4: Insert the new table into the original database, then insert data into table netflix_type by using SQL query
cursor.execute(new_table)
insert_data = "INSERT INTO netflix_type1 (show_id, type, title, director,cast,country,date_added,release_year,rating,duration,listed_in,description) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

## Step 5: Read each record from netflix_titles.csv file and import its records to new table netflix_type
file = open('netflix_titles.csv')
records = csv.reader(file)
cursor.executemany(insert_data, records)

### Query 1: Find the top five countries who have the most TV Shows in Netlfix
query1 = """SELECT Distinct country, count(type) 
		   FROM netflix_type1
		   WHERE country != '' AND type='TV Show'
		   Group by country
		   Order by count(type) DESC
		   LIMIT 5;"""
top5_tv_country = cursor.execute(query1).fetchall()

### Query 2: Find the top five countries who have the most movies in Netlfix
query2 = """SELECT Distinct country, count(type) 
		   FROM netflix_type1
		   WHERE country != '' AND type='Movie'
		   Group by country
		   Order by count(type) DESC
		   LIMIT 5;"""
top5_movie_country = cursor.execute(query2).fetchall()


## Step 10: Output to the console screen
###Query 1
print('#'* 50)
print(f"Top five countries who have the most TV Shows in Netlfix:")
for i in top5_tv_country:
    print(i)

###Query 2
print('#'* 50)
print(f"Top five countries who have the most movies in Netlfix:")
for j in top5_movie_country:
	print(j)

## Finally: Commit all changes and close the database connection
connects.commit()
connects.close()