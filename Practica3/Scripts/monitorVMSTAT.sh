#!/bin/bash

vmstat 1 2140 -n > VMSTAT.txt
awk '{print $4}' VMSTAT.txt > MEM.txt
rm VMSTAT.txt
