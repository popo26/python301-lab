# Write a script that demonstrates a try/except/else statement.
# For example, you can revisit the course module about database interactions
# and include a try/except/else statement based on what to do whether or not
# the database connection can be established.


import sqlalchemy
from dotenv import load_dotenv
import os

load_dotenv()

PASSWORD = os.getenv("PASSWORD")

try:
    engine = sqlalchemy.create_engine(f'mysql+pymysql://root:{PASSWORD}@localhost/sakila')
    connection = engine.connect()
    metadata = sqlalchemy.MetaData()
    actor = sqlalchemy.Table('actor',metadata, autoload=True, autoload_with=engine)
except:
    print("Have you started MySQL service? \nHave you entered correct credentials? \nHave you add correct table name?\nSomething is not right.")
else:
    print(actor.columns.keys())