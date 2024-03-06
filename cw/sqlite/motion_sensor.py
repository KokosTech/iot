from db import DB


class MotionSensor():
    def __init__(self, id, manufacturer, room):
        self.id = id
        self.manufacturer = manufacturer
        self.room = room

    def create(self):
        with DB() as db:
            db.execute('''
                       INSERT INTO motion_sensor (manufacturer, room)
                       VALUES (?, ?)''', (self.manufacturer, self.room))

    @staticmethod
    def find_by_room(room):
        if room is None:
            return None
        
        with DB() as db:
            row = db.execute('''
                       SELECT * FROM motion_sensor
                       WHERE room = ?''', (room, )).fetchone()
            
            if row is None:
                return None
            
            return MotionSensor(*row)

# MotionSensor(None, "Philips", "Living Room").create()
