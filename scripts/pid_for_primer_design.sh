#!/usr/bin/env bash

declare -a PIDs=$1

for PID in ${PIDs[@]};
do
	echo "[PID_FOR_][MESSAGE!] - Designing primers for $PID pid"

	if [ ! -d cuff_out.${PID} ];
	then
		echo "[PID_FOR_][ERROR!] - Folder does not exist!"
		exit 1
	fi

	gimme-the-primers cuff_out.${PID}/ 100 300
	primers-summary cuff_out.${PID}/ transcripts.gtf > cuff_out.${PID}/primers.smy
	smy2gtf cuff_out.${PID}/primers.smy

	echo "[PID_FOR_][MESSAGE!] - I designed the primers at cuff_out.${PID} folder"
done
