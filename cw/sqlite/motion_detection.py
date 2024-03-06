from db import DB


class MotionDetection():
    def __init__(self, id, motion_sensor_id, timestamp):
        self.id = id
        self.motion_sensor_id = motion_sensor_id
        self.timestamp = timestamp

    def create(self):
        with DB() as db:
            db.execute('''
                       INSERT INTO motion_detection (motion_sensor_id)
                       VALUES (?)''', (self.motion_sensor_id, ))

    def find_by_motion_id(self):
        pass

# MotionSensor(None, "Philips", "Living Room").create()
