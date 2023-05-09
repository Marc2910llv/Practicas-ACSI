#!/bin/bash

top -b -n 2140 -d 1 > TOP.txt
grep "%Cpu(s)" TOP.txt > TOP2.txt
awk '{print $2, $4, $8}' TOP2.txt > CPU.txt
rm TOP.txt TOP2.txt
