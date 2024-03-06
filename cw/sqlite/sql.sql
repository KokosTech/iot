-- SQLite
DELETE FROM motion_sensor WHERE room = "kitchen";

DELETE FROM motion_detection;

DELETE FROM motion_sensor;

DROP TABLE motion_sensor;

DROP TABLE motion_detection;

PRAGMA foreign_keys = ON;

PRAGMA foreign_keys;

CREATE TABLE IF NOT EXISTS motion_sensor (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    manufacturer TEXT NOT NULL,
    room TEXT NOT NULL
)

CREATE TABLE IF NOT EXISTS motion_detection (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    motion_sensor_id INTEGER NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(motion_sensor_id) REFERENCES motion_sensor(id) ON DELETE CASCADE
)