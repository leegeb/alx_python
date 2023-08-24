import sys
import MySQLdb as mdb

def main():
    database = mdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = database.cursor()

    cur.execute("SELECT * FROM states ORDER BY id")
    results = cur.fetchall()

    for result in results:
        print(result)

    cur.close()
    database.close()

if __name__ == "__main__":
    main()
