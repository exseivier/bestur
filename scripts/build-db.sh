#!/usr/bin/env bash

PATH_GENOMES_DB=$1
# CHECKS IF $PATH_GENOMES_DB/DUILD.DB EXIST
if [ ! -f ${PATH_GENOMES_DB}/build.db.1.bt2 ];
then
	FILES=""
	for file in ${PATH_GENOMES_DB}/*;
	do	if [ -z $FILES ];
		then
			FILES=$file
		else
			FILES="${FILES},${file}"
		fi

		FILES="${FILES},${file}"
	done
	echo -e "\e[102m[MESSAGE!] - Building database file...\e[0m"
	bowtie2-build -f $FILES ${PATH_GENOMES_DB}/build.db
	echo "[MESSAGE!] - Database was builded with following files:\n$FILES"
else
	echo "[MESSAGE!] - A Database file was found"
	echo "[MESSAGE!] - ${PATH_GENOMES_DB}/build.db"
fi


