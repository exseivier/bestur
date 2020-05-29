#!/usr/bin/env bash

PATH_QUERY_GENOME=$1
SIZE=$2
STEPS=$3
FILE_NAME=$(basename ${PATH_QUERY_GENOME} "/")

if [ ! -f $(dirname ${PATH_QUERY_GENOME})/splited-genome.${FILE_NAME:0:15}.${SIZE}.${STEPS}.fas ];
then
	echo -e "[SPLIT-GE][MESSAGE!] - Splited query genome was not found!"
	echo -e "[SPLIT-GE][MESSAGE!] - Formating query genome sequence!"
	format-seq $PATH_QUERY_GENOME
	echo -e "[SPLIT-GE][MESSAGE!] - Building splited query genome!"
	split ${PATH_QUERY_GENOME} $SIZE $STEPS
else
	echo "[SPLIT-GE][MESSAGE!] - A splited query genome file was found"
	echo "[SPLIT-GE][MESSAGE!] - $(dirname ${PATH_QUERY_GENOME})/splited-genome.${FILE_NAME:0:15}.${SIZE}.${STEPS}.fas"
fi
