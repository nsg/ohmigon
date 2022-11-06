# Ohmigon Documentation

## Prerequisites

This service requires a mqtt service, it will automatically pickup the needed credentials from Home Assistant.

## Configure

Connect your [Ohmigo-USB](https://www.ohmigo.io/en/product-page/ohmigo-usb) to the computer running Home Assistant. Specify the device name under the configuration tab.

`startup_outdoor_temperature`

The default temperature that the system will start with. Set it any value you prefer.

`mqtt_topic`

The base name for the MQTT topics

## Read data from MQTT

`${mqtt_topic}/started_at` and `${mqtt_topic}/updated_at` contains human readable strings with the add-on startup time, and when the last temperature value was changed.

`${mqtt_topic}/kilo_ohm` and `${mqtt_topic}/temperature` shows the current values.

## Write data to MQTT

`${mqtt_topic}/set_temperature` write a temperature (in Celsius) to this topic to change the current temperature. This will update the current Ohm value sent out to your heating system.
