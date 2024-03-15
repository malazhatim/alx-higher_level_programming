#!/usr/bin/python3
"""
 write a script that takes in arguments
and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that
is safe from MySQL injections!
"""
import sys
import MySQLdb


def main():
    connect = MySQLdb.connect(
                        host="localhost",
                        port=3306,
                        user=sys.argv[1],
                        passwd=sys.argv[2],
                        db=sys.argv[3],
                        charset="utf8"
                            )
    c = connect.cursor()
    search = sys.argv[4]
    c.execute("""SELECT id,name FROM states where name = %s
                ORDER by id ASC""", (search,))
    row = c.fetchall()
    for r in row:
        print(r)
    c.close()
    connect.close()


if __name__ == "__main__":
    main()
