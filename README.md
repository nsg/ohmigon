# Ohmigon

A add-on to control Ohmigo-USB from Home Assistant. At the moment this is mostly written for my needs where I controls an Elomax 250 with values specific for my needs. If you find this useful feel free to contribute and/or ask me for assistance. I'm happy to make this a more generic addon in the future.

## Possible improvements

* I have hard coded temperature/ohm values for my specific needs. This should of course move over to the configuration.
* Figure out _why_ `uart: true` do not work, remove the need for `full_access`.

## Install

At the moment I'm the only user so there is no point for me to publish this to a HA repository. If you like to use this (as a user) feel free to open an issue and I can probably set something up for you.

If you like to thinker and/or contribute, this is how I install this add-on, read the Makefile and the [tutorial](https://developers.home-assistant.io/docs/add-ons/tutorial/) as a hint.
