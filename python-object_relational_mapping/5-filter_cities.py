import sys
import MySQLdb


def main():
    database = MySQLdb.connect(
        host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = database.cursor()

    query = ("SELECT cities.name, states.name FROM "
             "cities JOIN states ON cities.state_id = states.id")
    cur.execute(query)

    results = cur.fetchall()

    city_names = [result[0] for result in results if result[1] == sys.argv[4]]

    print(", ".join(city_names))

    cur.close()
    database.close()


if __name__ == "__main__":
    main()
