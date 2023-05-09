#!/bin/bash

vmstat 15 482 -n | awk '{print $4}' > VMSTAT.txt

python3 crearCSV.py

rm VMSTAT.txt

time vmstat 1 1 -n
