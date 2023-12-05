import json
import time
import threading


class Bulb:
    def __init__(self, thing_id):
        self.thing_id = self.policy_id = thing_id
        self.file_name = thing_id + '.json'
        self.event = threading.Event()
        self.attributes = {
            "model": "Smart Bulb",
            "diameter": 160,
            "warranty": 6,
        }
        self.features = {
            "indicators": {
                "properties": {
                    "brightness": 0,
                    "color": "white",
                }
            },
            "state": {
                "properties": {
                    "on": False,
                }
            },
        }

    def save_to_json(self):
        serializable = {
            "thingId": self.thing_id,
            "policyId": self.policy_id,
            "attributes": self.attributes,
            "features": self.features
        }

        with open("./digital-twins/" + self.file_name, 'w') as f:
            json.dump(serializable, f, indent=4, ensure_ascii=False)

    def break_bulb(self):
        print("Bulb with ID: " + self.thing_id + " is broken")

        self.features["state"]["properties"]["on"] = False
        self.save_to_json()

    def fix_bulb(self, tech_id):
        print("Technician " + str(tech_id) +
              " is fixing bulb with ID: " + self.thing_id)

        time.sleep(5)

        print("Bulb with ID: " + self.thing_id + " is fixed")

        self.features["state"]["properties"]["on"] = True
        self.save_to_json()

    def update_indicators(self, brightness, color):
        try:
            brightness = int(brightness)
        except:
            raise ValueError("Brightness must be a number")    

        if (brightness < 0 or brightness > 100):
            raise ValueError("Brightness must be between 0 and 100")

        self.features["indicators"]["properties"]["brightness"] = brightness
        self.features["indicators"]["properties"]["color"] = color

        print("Updated bulb with ID: " + self.thing_id + " indicators")
        print("Brightness: " + str(brightness) + "%")
        print("Color: " + color)
        self.save_to_json()
