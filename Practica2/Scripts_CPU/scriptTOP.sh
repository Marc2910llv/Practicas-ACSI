#!/bin/bash

lscpu

top -b -n 1442 -d 5 > TOP.txt
grep "top -" TOP.txt > timestamp.txt
grep "%Cpu(s)" TOP.txt > CPU.txt

python3 crearCSV.py

rm TOP.txt timestamp.txt CPU.txt

time top -b -n 1
