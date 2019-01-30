#!/usr/bin/env bash

PATH_QUERY_GENOME=$1
SIZE=$2

if [ ! -f $(dirname ${PATH_QUERY_GENOME})/splited-genome.fas ];
then
	echo -e "\e[102m[MESSAGE!] - Splited query genome was not found\e[0m"
	echo -e "\e[102m[MESSAGE!] - Building splited query genome...\e[0m"
	split $PATH_QUERY_GENOME $SIZE
else
	echo "[MESSAGE!] - A splited query genome file was found"
	echo "[MESSAGE!] - $(dirname ${PATH_QUERY_GENOME})/splited-genome.fas"
fi
