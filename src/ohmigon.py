import json
import time
import os
import datetime

import utils
import ohmigo
import mqtt

#
# Load config from options.json and environment
#
config = json.load(open("/data/options.json"))
device = config["device"]
startup_outdoor_temperature = config["startup_outdoor_temperature"]
mqtt_host = os.environ["MQTT_HOST"]
mqtt_topic = config["mqtt_topic"]
mqtt_username = os.environ["MQTT_USERNAME"]
mqtt_password = os.environ["MQTT_PASSWORD"]


def cur_datetime():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def process_set_temperature(client, userdata, msg):
    set_temperature(int(msg.payload.decode()))


def set_temperature(temperature, table="outdoor"):
    k_ohm = utils.temp_to_kilo_ohm(temperature, table)
    ohm.atr(k_ohm * 1000)
    mq.publish("kilo_ohm", k_ohm)
    mq.publish("temperature", temperature)
    mq.publish("updated_at", cur_datetime())
    print(f"set kilo_ohm={k_ohm}; set temperature={temperature}", flush=True)


#
# Setup MQTT connection and subscribe for messages
#
mq = mqtt.MQTT(mqtt_host, mqtt_topic, mqtt_username, mqtt_password)
mq.publish("started_at", cur_datetime())
mq.subscribe("set_temperature", process_set_temperature)

#
# Connect to the Ohmigo-USB device and set start temperature
#
ohm = ohmigo.Ohmigo(device=device)
set_temperature(startup_outdoor_temperature)

#
# Main loop
#
while True:
    time.sleep(60)
