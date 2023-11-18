import os
import random
import requests
import threading
from datetime import datetime
from time import sleep

class Thermometer:
    def __init__(self, id: int):
        self.id = 'thermometer_' + str(id)
        self.interval = self.gen_value(1, 15)

    def gen_value(self, min: int, max: int):
        return random.randint(min, max)

    def send_data(self):
        while True:
            value = self.gen_value(18, 25)
            timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

            res = requests.post(
                url='http://iot-sensors-server-01:5000/data', 
                json={
                    'value': value,
                    'timestamp': timestamp,
                    'device_id': self.id
                }
            )
            print(res.content)
            sleep(self.interval)
            

def create_threads(num: int = 3):
    threads: [threading.Thread] = []
    
    for i in range(num):
        thermometer = Thermometer(id=i)
        thread = threading.Thread(target=thermometer.send_data)
        thread.start()
        threads.append(thread)
    
    return threads

def join_threads(threads: [threading.Thread]):
    for i in threads:
        i.join()    

if __name__ == '__main__':
    sleep(5)
    term_num = int(os.getenv('THERM_NUM'))    
    threads = create_threads(term_num)
    join_threads(threads=threads)
