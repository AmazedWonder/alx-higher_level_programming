#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


# Get the MySQL username, password, and database
# name from command-line arguments
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    curs = db.cursor()
    # Execute the query to retrieve states starting with 'N'
    curs.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id""")
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    db.close()
