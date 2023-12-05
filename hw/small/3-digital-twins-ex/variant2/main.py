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
        print(" -------------------------------------------------------")
        print("| Bulb ID\t|\tColor\t|   Brightness  | State |")
        print(" -------------------------------------------------------")

        for freezer in get_freezer_data():
            thing_id = freezer['thingId']
            color = freezer['features']['indicators']['properties']['color']
            brightness = freezer['features']['indicators']['properties']['brightness']
            state = freezer['features']['state']['properties']['on']

            print(
                f"| {thing_id}\t|\t{color}\t|\t{brightness}\t|  {state and 'On ' or 'Off'}  |")
            print(" -------------------------------------------------------")

        print("\n")
        time.sleep(1)


if __name__ == "__main__":
    dashboard()
