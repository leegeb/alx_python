import sys
import MySQLdb as mdb


def main():
    database = mdb.connect(
        host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = database.cursor()

    pattern = 'N%'
    query = "SELECT * FROM states WHERE BINARY name LIKE %s ORDER BY id"
    cur.execute(query, (pattern,))

    results = cur.fetchall()

    for result in results:
        print(result)

    cur.close()
    database.close()


if __name__ == "__main__":
    main()
