#!/bin/bash

# Update package list and install Mosquitto
sudo apt-get update
sudo apt-get install -y mosquitto mosquitto-clients

# Start Mosquitto server
sudo systemctl start mosquitto

# Enable Mosquitto to start on boot
sudo systemctl enable mosquitto
