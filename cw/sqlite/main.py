import time

from db import DB
from motion_detection import MotionDetection
from motion_sensor import MotionSensor

# MotionSensor(None, "Siemens", "Kitchen").create()

motion_sensor_id = MotionSensor.find_by_room("Kitchen").id

MotionDetection(None, motion_sensor_id, None).create()
time.sleep(1)

MotionDetection(None, motion_sensor_id, None).create()

time.sleep(3)
MotionDetection(None, motion_sensor_id, None).create()

motion_sensor_id = MotionSensor.find_by_room("Living Room").id
MotionDetection(None, motion_sensor_id, None).create()

# with DB() as db:
#     db.execute('''
#                 DELETE FROM motion_sensor
#                 WHERE room = "Kitchen";
#     ''')
