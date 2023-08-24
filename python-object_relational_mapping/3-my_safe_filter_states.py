import sys
import MySQLdb as mdb


def main():
    database = mdb.connect(
        host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = database.cursor()

    cur.execute("SELECT * FROM states ORDER BY id")
    results = cur.fetchall()

    search_value = sys.argv[4]

    for result in results:
        if result[1] == search_value:
            print(result)

    cur.close()
    database.close()


if __name__ == "__main__":
    main()
