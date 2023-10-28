#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


# Provide your MySQL server credentials and database name as command line arguments
if __name__ == "__main__":
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    # Create a cursor object to interact with the database
    curs = db.cursor()
    # Execute the SQL query to retrieve all states
    curs.execute("SELECT * FROM states")
    # Fetch all the rows as a list of tuples
    rows = curs.fetchall()
    # Display the results
    for row in rows:
        print(row)
    # Close the cursor and database connection
    curs.close()
    db.close()
