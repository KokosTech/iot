from db import DB


def create_tables():
    with DB() as db:
        # таблица за термометри,

        db.execute('''
                     CREATE TABLE  IF NOT EXISTS thermometers (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        manufacturer TEXT,
                        room TEXT
                     );''')
        
        # таблица за отчетени температури,

        db.execute('''
                   CREATE TABLE IF NOT EXISTS temperature_reports (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        thermometer_id INTEGER,
                        time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        temperature FLOAT,
                        FOREIGN KEY (thermometer_id) REFERENCES thermometers(id) ON DELETE CASCADE
                   );''')

if __name__ == "__main__":
    print("Creating tables...")
    create_tables()
    print("Tables created.")