#!/usr/bin/env bash

declare -a PIDs=$1
DESTINY=$2

for PID in ${PIDs[@]};
do
	cp -r cuff_out.${PID} $DESTINY
	echo "I sent cuff_out.${PID} to $DESTINY"
done
