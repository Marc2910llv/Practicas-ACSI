#!/bin/bash

for i in 25000 50000 100000 150000
do
	
	for j in 1 2 3 4 5 6 7 8 9 10
	do
		sysbench --test=cpu --cpu-max-prime="$i" --num-threads=2 run

		sleep 2
	done
done
