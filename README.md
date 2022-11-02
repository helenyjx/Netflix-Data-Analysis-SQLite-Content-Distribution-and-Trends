# Project-3-SQL-Jiaxin-Ying
This is project 3 from Jiaxin Ying for IDS706 course.

## Key Objectives of Project
In project 3, the main goal is to generate a script that queries a database by using Sqlite. I use the dataset called netflix_titles.csv and netflix_titles.db. This dataset comes from Kaggle called Netflix Dataset (https://www.kaggle.com/code/arvinthsss/sql-syntax-series-using-netflix-dataset/data), which is about 8807 historical records of TV shows and movies which were broadcasted on Netflix from 1925 to 2021. There are twelve main variables: show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, and description. In this time, I want to do five main queries to answer my reseach questions one by one below:
* What are the top five countries who have the most TV Shows on Netflix?
* What are the top five countries who have the most movies on Netflix?
* What are the top five directors who directed the most movies or TV shows on Netflix?
* What are the top five directors who have the most movies or TV shows on Netflix which are listed in Documentaries?
* What are the top five directors who have the most adult movies or TV shows on Netflix?

Later, I will show how I use the command line on Terminal to show each result after querying my local database.

## Structure Diagram


## Demo Video Link


## Advance Preparation
### 1. Build virtual environment
By building isolated Python virtual environments for them, a virtual environment is a tool that aids in maintaining the separation of dependencies needed by various projects. Therefore, we need to build the devcontainer (Python 3 & 3.10-bullseye) at first.

### 2. Create a workflow at Github
A workflow is an automated procedure that can be configured to execute one or more operations. Workflows are defined by a YAML file that is checked into your repository and run when prompted by an event there, manually, or according to a set schedule.
* Go to the homepage at GitHub, click the repository, find the button "Actions", then choose "set up a workflow yourself".
* Once setup the code we need at main.yml file, we can check the status of workflows from "Actions" page, so make sure the program could pass the tests. Otherwise, we need to fix the code where the bugs/errors are reported.

### 3. Create a Makefile
A makefile is a unique file that contains instructions on how to compile a project. These rules comprise targets, which can be files or objects that make needs to construct as well as actions make needs to perform (like "clean" or "build"), as well as the commands that need to be executed in order to accomplish those actions.

### 4. Add requirements.txt
A requirement.txt file is a special type of file that typically contains details about all the libraries, modules, and packages that are utilized throughout the development of a specific project. Additionally, it keeps all of the files and packages needed for the project to function or on which it depends.

## Steps of querying data via Sqlite.
### 1. Set up: import required modules 
Type: `import csv` and `import sqlite3`

### Step 1: Do SQL queries via a cursor after connecting to netflix_titles database
* `connects = sqlite3.connect('netflix_titles.db')`
* `cursor = connects.cursor()`

### Step 2: Create a new table called netflix_type1
* `new_table = '''CREATE TABLE netflix_type00(show_id VAR PRIMARY KEY,type VAR,title VAR,director VAR,cast VAR,country VAR,date_added DATE,release_year DATE,rating VAR,duration VAR,listed_in VAR,description VAR);'''`

### Step 3: Insert the new table into the original database, then insert data into table netflix_type by using SQL query
* `cursor.execute(new_table)`
* `insert_data = "INSERT INTO netflix_type00 (show_id, type, title, director,cast,country,date_added,release_year,rating,duration,listed_in,description) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"`

### Step 4: Read each record from netflix_titles.csv file and import its records to new table netflix_type
* `file = open('netflix_titles.csv')`
* `records = csv.reader(file)`
* `cursor.executemany(insert_data, records)`

## Generate a script that queries a database via Sqlite
### Query 1: Find the top five countries who have the most TV Shows on Netflix
<img width="576" alt="1" src="https://user-images.githubusercontent.com/112274822/199576122-43c2c3de-8f5a-4ac5-b7bb-a75ed7a619f7.png">

### Query 2: Find the top five countries who have the most movies on Netflix
<img width="558" alt="2" src="https://user-images.githubusercontent.com/112274822/199576182-bf2a8508-692b-47a1-b050-9034c1e595a8.png">

### Query 3: Find the top five directors who directed the most movies or TV shows on Netflix
<img width="672" alt="3" src="https://user-images.githubusercontent.com/112274822/199576221-a5d89bf4-162c-43d7-b4fc-6cb6ca18276c.png">

### Query 4: Find the top five directors who have the most movies or TV shows on Netflix are listed in Documentaries
<img width="846" alt="4" src="https://user-images.githubusercontent.com/112274822/199576271-8cae94d2-f938-47c5-818a-c77349f55eeb.png">

### Query 5: Find the top five directors who have the most adult movies or TV shows in Netlfix
<img width="686" alt="5" src="https://user-images.githubusercontent.com/112274822/199576326-be1283c2-a568-4b88-b5cc-4a3804ab920a.png">

## Show all the results after querying data on Terminal
### We need to use the print function at netflix_type.py, the code is shown below:
<img width="846" alt="print" src="https://user-images.githubusercontent.com/112274822/199576355-b5292d61-75de-4e92-ad57-77582a6c9080.png">

### Now, we just need to type: `netflix_type.py` on Terminal to see answers of five research questions
<img width="1028" alt="bash" src="https://user-images.githubusercontent.com/112274822/199576394-8f128cd0-295c-4248-9964-b496389012a1.png">

## Finally: Commit all changes and then close the database connection
* `connects.commit()`
* `connects.close()`


