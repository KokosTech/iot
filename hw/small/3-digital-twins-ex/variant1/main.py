import json
import os
import time

def get_freezer_data():
    filenames = os.listdir("./digital-twins")
    freezer_data = []

    for filename in filenames:
        with open("./digital-twins/" + filename, 'r') as f:
            freezer_data.append(json.load(f))

    return freezer_data

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def dashboard():
    while True:
        clear_screen()
        print(" ---------------------------------------------------------")
        print("| Freezer ID\t|  Temperature  |    Humidity   | Working |")
        print(" ---------------------------------------------------------")

        for freezer in get_freezer_data():
            thing_id = freezer['thingId']
            temperature = freezer['features']['temperatureControl']['properties']['temperature']
            humidity = freezer['features']['temperatureControl']['properties']['humidity']
            state = freezer['features']['state']['properties']['working']
            
            print(f"| {thing_id}\t|\t{temperature}\t|\t{humidity}\t|  {state and f'{state} '}  |")
            print(" ---------------------------------------------------------")

        print("\n")
        time.sleep(1)
        
if __name__ == "__main__":
    dashboard()