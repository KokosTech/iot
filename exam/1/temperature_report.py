from db import DB


class TemperatureReport():
    def __init__(self, id, thermometer_id, time, temperature):
        self.id = id
        self.thermometer_id = thermometer_id
        self.time = time
        self.temperature = temperature

    def create(self):
        with DB() as db:
            db.execute('''
                       INSERT INTO temperature_reports (thermometer_id, temperature)
                          VALUES (?, ?)''', (self.thermometer_id, self.temperature))
            
        return self
    
    def delete(self):
        with DB() as db:
            db.execute('''
                       DELETE FROM temperature_reports
                       WHERE id = ?''', (self.id, ))
            