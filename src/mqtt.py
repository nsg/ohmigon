import random

from paho.mqtt import client as mqtt_client


class MQTT:
    def __init__(self, broker, topic_base, username, password, port=1883):
        client_id = f"python-mqtt-{random.randint(0, 1000)}"

        self.client = mqtt_client.Client(client_id)
        self.client.username_pw_set(username, password)
        self.client.on_connect = self.on_connect
        self.client.connect(broker, port)
        self.client.loop_start()
        self.topic_base = topic_base

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!", flush=True)
        else:
            print("Failed to connect, return code %d\n", rc, flush=True)

    def publish(self, topic, message):
        result = self.client.publish(f"{self.topic_base}/{topic}", message, retain=True)
        if result[0] != 0:
            print(f"Failed to publish to topic {self.topic_base}/{topic}", flush=True)

    def subscribe(self, topic, callback):
        self.client.subscribe(f"{self.topic_base}/{topic}")
        self.client.on_message = callback
        print(f"Subscribed to topic {self.topic_base}/{topic}", flush=True)
