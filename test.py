## Prepare for testing
import sqlite3
from faker import Faker
faker = Faker()
names = [faker.name().split() for _ in range(1000)]
names = [name for name in names if len(name) == 2]

##Create a new table at the data.db
# connects = sqlite3.connect('test.db')
# table = 'CREATE TABLE users (id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT)'
# cursor = connects.cursor()
# cursor.execute(table)
# connects.commit()

##Insert all data into the new table
connects = sqlite3.connect('test.db')
insert_query = 'INSERT INTO users (FIRST_NAME, last_name) VALUES (?, ?)'
cursor = connection.cursor()
for name in names:
    cursor.execute(insert_query, name)
connects.commit()

##Select each record from the table
select_query = 'SELECT * FROM users LIMIT 5'
for i in cursor.execute(select_query):
    print(i)