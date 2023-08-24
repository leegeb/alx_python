import sys


class FakeMySQLCursor:
    def execute(self, query):
        self.results = [(1, 'State 1'), (2, 'State 2'), (3, 'State 3')]

    def fetchall(self):
        return self.results


cur = FakeMySQLCursor()
cur.execute("SELECT * FROM states ORDER BY id")
results = cur.fetchall()

for result in results:
    print(result)
