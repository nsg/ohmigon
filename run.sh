#!/usr/bin/with-contenv bashio

export MQTT_HOST=$(bashio::services mqtt "host")
export MQTT_USERNAME=$(bashio::services mqtt "username")
export MQTT_PASSWORD=$(bashio::services mqtt "password")

python3 /ohmigon.py
