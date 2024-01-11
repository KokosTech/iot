import network

from machine import I2C, Pin, SoftI2C

from lcd_api import LcdApi
from i2c_lcd import I2cLcd

from umqtt.simple import MQTTClient

from time import sleep

# Relay / VIrtual Door

PIN_RELAY = 18
RELAY = Pin(PIN_RELAY, Pin.OUT)

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

def clear_lcd():
    LCD.clear()

def running_msg():
    print_msg("System's up!")

# MQTT Funtions

MQTT_CLIENT_ID  = "kaloyan-acs-door"
MQTT_BROKER     = "broker.mqttdashboard.com"
MQTT_TOPIC      = "tech/kaloyan/acs/door"

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

# Door Funtions

def open():
    RELAY.on()

def close():
    RELAY.off()

# Process Message

def process_msg(message):
    if(message == "123#" or message == "456#"):
        print_msg(f"Welcome back!   {'Janitor' if message == '123#' else 'Security' } {message}")
        open()
        sleep(5)
        close()
        running_msg()
    else:
        print_msg("Access denied!")

# MQTT Callback

def callback(topic, message):
    topic = topic.decode("utf-8")
    message = message.decode("utf-8")
    print_msg(message)

    process_msg(message)

# Init

print_msg("Loading...")

client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER)
client.set_callback(callback)
connect_to_mqtt_broker()

running_msg()

try:
    while 1:
        client.wait_msg()
finally:
    client.disconnect()