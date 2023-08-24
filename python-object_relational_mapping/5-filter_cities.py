import sys
import MySQLdb as mdb


def main():
    database = mdb.connect(
        host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = database.cursor()

    query = ("SELECT cities.name, states.name FROM "
             "cities JOIN states ON cities.state_id = states.id")
    cur.execute(query)

    results = cur.fetchall()

    city_names = []
    search_state = sys.argv[4]

    for result in results:
        if result[1] == search_state:
            city_names.append(result[0])

    print(", ".join(city_names))

    cur.close()
    database.close()
