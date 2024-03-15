#!/usr/bin/python3
"""
Write a script that takes in an argument and
displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
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
    query = """SELECT * FROM states where name = '{:s}'
            ORDER by id ASC""".format(search)
    c.execute(query)
    row = c.fetchall()
    for r in row:
        if r[1] == search:
            print(r)
    c.close()
    connect.close()


if __name__ == "__main__":
    main()
