# Smart-Home-Hub

## What is a Smart Home Hub?

A smart home hub is hardware and/or software that connects devices together on a home automation network and controls communications among them. Smart home hubs, which connect either locally or to the cloud, are useful for internet of things (IoT) devices.

## Why creating my own?

There are a lot of smart devices on the market to allow people to connect devices in their house. However most of them are not open source and rely on the internet and cloud services provided by third parties.

I am a big fan of privacy and after everything that has happened in the past few years regarding data breaches I wanted to explore and provide a solution that is 100% open source and does not rely on any third parties.

## Hardware used:

- Raspberry Pi 3b+
- Pi Camera V2
- Raspberry Pi 7" touchscreen
- Ultrasonic sensor HC-SR04
- Temperature/Humidity sensor DHT-11
- 1 x RGB LED
- 1 x Blue LED
- 1 x Red LED
- 8 x 220 ohms resistor
- 1 x Hole breadboard
- 1 RPI GPIO extension board
- 20 x Jumper wires
- 3 x Sonoff mini relays (firmware flashed)
- 3 x light bulbs
- 3 x light switches

## Technologies used:

- Debian version v10.3
- Node-Red version v1.0.4
- NodeJS v12.16.1
- MQTT
- Mosquitto v1.5.7
- Tasmota v8.1.0.10

## Flows:

- Flow for the door camera presence detection and emailing photo:
  ![](./flowScreenshots/emailImg.png)

- Flow to detect is home by using WiFi detection:
  ![](./flowScreenshots/isHome.png)

- Flow to control the lights:
  ![](./flowScreenshots/lightControl.png)

- Flow for the temperature control:
  ![](./flowScreenshots/tempCtrl.png)
