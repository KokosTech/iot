import os
import time
import random
import threading
from queue import Queue

from bulb import Bulb

BULBS = 5
TECHNITIANS = 2


def bulb_functioning(bulb):
    while True:
        if random.randint(0, 100) < 40:
            bulb.break_bulb()
            manager_queue.put(bulb)
            manager_event.set()
            manager_event.clear()
            bulb.event.wait()
        else:
            brightness = random.randint(0, 100)
            color = random.choice([
                "white",
                "red",
                "green",
                "blue",
                "yellow",
                "purple",
                "orange",
                "pink",
                "cyan",
                "magenta",
                "lime",
                "brown",
                "olive",
                "grey",
                "silver",
                "black",
            ])
            bulb.update_indicators(brightness, color)

        time.sleep(random.randint(3, 5))


def technician_fix_bulb(technician_id, bulb):
    bulb.fix_bulb(technician_id)
    bulb.event.set()
    bulb.event.clear()
    available_technitians.put(technician_id)


def manager():
    while True:
        manager_event.wait()
        while not manager_queue.empty():
            if not available_technitians.empty():
                threading.Thread(
                    target=technician_fix_bulb,
                    args=(
                        available_technitians.get(),
                        manager_queue.get()
                    ),
                    daemon=True
                ).start()


if __name__ == "__main__":
    if not os.path.exists("./digital-twins"):
        os.makedirs("./digital-twins")
    
    manager_thread = threading.Thread(target=manager, daemon=True)
    manager_queue = Queue()
    manager_event = threading.Event()

    manager_thread.start()

    available_technitians = Queue()

    for i in range(TECHNITIANS):
        available_technitians.put(i + 1)

    bulbs_ids = ["bulb-" + str(i + 1) for i in range(BULBS)]
    bulbs = [Bulb(bulb) for bulb in bulbs_ids]

    bulb_threads = []
    
    for bulb in bulbs:
        bulb_thread = threading.Thread(
            target=bulb_functioning, args=(bulb,), daemon=True)
        bulb_threads.append(bulb_thread)

    for bulb_thread in bulb_threads:
        bulb_thread.start()
        time.sleep(.5)

    for bulb_thread in bulb_threads:
        bulb_thread.join()
