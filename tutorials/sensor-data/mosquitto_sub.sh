#!/usr/bin/env bash

mosquitto_sub -t 'sensor/#' -h poseidon.local -p 1883 >> data.json.txt
