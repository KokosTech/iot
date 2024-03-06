import sqlite3

DB_NAME = "database.db"


class DB:
    def __enter__(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.conn.execute("PRAGMA foreign_keys = ON")
        return self.conn.cursor()

    def __exit__(self, type, calue, traceback):
        self.conn.commit()
        self.conn.close()


# with DB() as db:
#     db.execute('''
#                INSERT INTO motion_sensor (manufacturer, room)
#                VALUES ('Philips', 'Living Room')''')
