import network

from machine import I2C, Pin, SoftI2C

from lcd_api import LcdApi
from i2c_lcd import I2cLcd

from umqtt.simple import MQTTClient

from time import sleep

# Keyboard

ROWS = [19, 18, 5, 17]
COLS = [16, 4, 0]

KEYS_MAP = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['*', '0', '#']
]

# for loops to setup all the pins as inputs with pullups
KEYBOARD = []

for row in ROWS:
    KEYBOARD.append(Pin(row, Pin.IN, Pin.PULL_UP))

for col in COLS:
    KEYBOARD.append(Pin(col, Pin.OUT))


def read_keypad():
    for i in range(len(COLS)):
        KEYBOARD[i + len(ROWS)].value(0)
        for j in range(len(ROWS)):
            if KEYBOARD[j].value() == 0:
                return KEYS_MAP[j][i]
        KEYBOARD[i + len(ROWS)].value(1)

    return None


# Display

SDA_DISPLAY = Pin(25)
CLK_DISPLAY = Pin(26)

# The default I2C address of the LCD1602 module is 0x27. You can change the address by setting the i2cAddress attribute.
I2C_ADDR = 0x27

ROWS_DISPLAY = 2
COLS_DISPLAY = 16

I2C = SoftI2C(scl=CLK_DISPLAY, sda=SDA_DISPLAY, freq=10000)
LCD = I2cLcd(I2C, I2C_ADDR, ROWS_DISPLAY, COLS_DISPLAY)

# LCD Functions


def print_msg(msg):
    LCD.clear()
    LCD.putstr(msg)


def print_agr_msg(msg):
    LCD.putstr(msg)


def clear_lcd():
    LCD.clear()


def running_msg():
    print_msg("System's up!")

# MQTT Funtions


MQTT_CLIENT_ID = "kaloyan-acs-keyboard"
MQTT_BROKER = "broker.mqttdashboard.com"
MQTT_TOPIC = "tech/kaloyan/acs/door"


def connect_to_wifi():
    print_msg("Connecting to Wi-Fi...")
    print("Connecting to Wi-Fi", end="")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('Wokwi-GUEST', '')
    while not sta_if.isconnected():
        print(".", end="")
        sleep(0.1)
    print(" Connected!")


def connect_to_mqtt_broker():
    connect_to_wifi()
    print_msg("Connecting to MQTT server...")
    print("Connecting to MQTT server... ", end="")
    client.connect()
    print_msg("Connected!")
    print("Connected!")
    client.subscribe(MQTT_TOPIC)
    print("Subscribed to {}".format(MQTT_TOPIC))

# Keyboard Functions


def get_code():
    code = ""
    while True:
        key = read_keypad()
        if key != None:
            code += key
            print_agr_msg(key)

            if key == "#":
                break
            elif key == "*":
                code = ""
                print_msg("Code cleared!")

            sleep(0.5)
    return code


def runner():
    print_msg("Enter code:\n")
    code = get_code()
    print_msg("Code entered!\nCode: {}".format(code))
    client.publish(MQTT_TOPIC, code)
    sleep(5)

# MQTT Callback


def callback(topic, message):
    topic = topic.decode("utf-8")
    message = message.decode("utf-8")
    print_msg("Server:\n" + message)
    sleep(5)

# Init


print_msg("Loading...")

client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER)
client.set_callback(callback)
connect_to_mqtt_broker()

try:
    while 1:
        client.check_msg()
        runner()
finally:
    client.disconnect()
