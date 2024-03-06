from db import DB


class Thermometer():
    def __init__(self, id, manufacturer, room):
        self.id = id
        self.manufacturer = manufacturer
        self.room = room

    def create(self):
        with DB() as db:
            res = db.execute('''
                       INSERT INTO thermometers (manufacturer, room)
                       VALUES (?, ?)
                       RETURNING id''', (self.manufacturer, self.room))
            
            self.id = res.fetchone()[0]
            
        return self

    def update(self, manufacturer, room):
        self.manufacturer = manufacturer
        self.room = room

        with DB() as db:
            db.execute('''
                       UPDATE thermometers
                       SET manufacturer = ?, room = ?
                       WHERE id = ?''', (self.manufacturer, self.room, self.id))

    def delete(self):
        with DB() as db:
            db.execute('''
                       DELETE FROM thermometers
                       WHERE id = ?''', (self.id, ))

    # ======== SELECT METHODS =========

    @staticmethod
    def avg_by_room(room):
        if room is None:
            return None

        with DB() as db:
            row = db.execute('''
                        SELECT AVG(temperature) FROM temperature_reports
                        JOIN thermometers ON thermometers.id = temperature_reports.thermometer_id
                        WHERE thermometers.room = ?''', (room, )).fetchone()

            if row is None:
                return None

            return row[0]

    # ========

    def min_by_thermometer(self):
        with DB() as db:
            row = db.execute('''
                        SELECT MIN(temperature) FROM temperature_reports
                        WHERE thermometer_id = ?''', (self.id, )).fetchone()

            if row is None:
                return None

            return row[0]

    # ========

    @staticmethod
    def find_by_manufacturer(manufacturer):
        if manufacturer is None:
            return None

        with DB() as db:
            row = db.execute('''
                        SELECT COUNT(*) FROM thermometers
                        WHERE manufacturer = ?''', (manufacturer, )).fetchone()

            if row is None:
                return None

            return row[0]
        
