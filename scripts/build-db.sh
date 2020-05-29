#!/usr/bin/env bash

# // $INPUT is the full path to txt file which contains
# // the names of the full path to fasta sequences you
# // want to use to build the blastn databases.
INPUT=$1
FORCE_TO_BUILD_DB=$2
DB_FILE_NAME=${INPUT##*/}
PATH_GENOMES_DB=${INPUT%/*}

if [ -f ${PATH_GENOMES_DB}/${DB_FILE_NAME%.*}.db.nal ] && [ "$FORCE_TO_BUILD_DB" == "no" ];
then
	# // Basicaly, it does not perform anything.
	echo "[BUILD-DB][MESSAGE!] - A blast database was found, & you do not want to rebuild it!"
	echo "[BUILD-DB][MESSAGE!] - The name of the database is: ${DB_FILE_NAME%.*}.db"
	echo "[BUILD-DB][MESSAGE!] - Proceed to next analysis, partner!"
	echo "[BUILD-DB][MESSAGE!] - Leaving build-db from useq-0.2!"
elif [ -f ${PATH_GENOMES_DB}/${DB_FILE_NAME%.*}.db.nal ] && [ "$FORCE_TO_BUILD_DB" == "yes" ];
then
	# // Build database.
	echo "[BUILD-DB][MESSAGE!] - A blast database was found but you want to rebuild it!"
	echo "[BUILD-DB][MESSAGE!] - building ${DB_FILE_NAME%.*}.db from ${DB_FILE_NAME}"
	FILES=""
	while read -r LINE;
	do	
		if [ -z "$FILES" ];
		then
			FILES="${PATH_GENOMES_DB}/${LINE%.*}.db"
		else
			FILES="$FILES ${PATH_GENOMES_DB}/${LINE%.*}.db"
		fi
		echo "[BUILD-DB][MESSAGE!] - Building ${LINE%.*}.db"
		if [ ! -f ${PATH_GENOMES_DB}/${LINE%.*}.db.nhr ] \
			|| [ ! -f ${PATH_GENOMES_DB}/${LINE%.*}.db.nin ] \
			|| [ ! -f ${PATH_GENOMES_DB}/${LINE%.*}.db.nsq ];
		then
			makeblastdb -in ${PATH_GENOMES_DB}/$LINE \
				-dbtype nucl \
				-out ${PATH_GENOMES_DB}/${LINE%.*}.db \
				-title ${LINE%.*}
		fi
	done < ${PATH_GENOMES_DB}/$DB_FILE_NAME
	blastdb_aliastool -title ${DB_FILE_NAME%.*} \
		-dbtype nucl \
		-dblist "$FILES" \
		-out ${PATH_GENOMES_DB}/${DB_FILE_NAME%.*}.db
	echo "[BUILD-DB][MESSAGE!] - ${DB_FILE_NAME%.*}.db alias database was created!"
	echo "[BUILD-DB][MESSAGE!] - Leaving build-db from useq-0.2!"
else
	# Build db
	echo "[BUILD-DB][MESSAGE!] - No blast database with name ${PATH_GENOMES_DB}/${DB_FILE_NAME%.*}.db was found"
	echo "[BUILD-DB][MESSAGE!] - building ${DB_FILE_NAME%.*}.db from ${DB_FILE_NAME}"
	FILES=""
	while read -r LINE;
	do	
		if [ -z "$FILES" ];
		then
			FILES="${PATH_GENOMES_DB}/${LINE%.*}.db"
		else
			FILES="$FILES ${PATH_GENOMES_DB}/${LINE%.*}.db"
		fi
		echo "[BUILD-DB][MESSAGE!] - Building ${LINE%.*}.db"
		if [ ! -f ${PATH_GENOMES_DB}/${LINE%.*}.db.nhr ] \
			|| [ ! -f ${PATH_GENOMES_DB}/${LINE%.*}.db.nin ] \
			|| [ ! -f ${PATH_GENOMES_DB}/${LINE%.*}.db.nsq ];
		then
			makeblastdb -in ${PATH_GENOMES_DB}/$LINE \
				-dbtype nucl \
				-out ${PATH_GENOMES_DB}/${LINE%.*}.db \
				-title ${LINE%.*}
		fi
	done < ${PATH_GENOMES_DB}/$DB_FILE_NAME
	blastdb_aliastool -title ${DB_FILE_NAME%.*} \
		-dbtype nucl \
		-dblist "$FILES" \
		-out ${PATH_GENOMES_DB}/${DB_FILE_NAME%.*}.db
	echo "[BUILD-DB][MESSAGE!] - ${DB_FILE_NAME%.*}.db alias database was created!"
	echo "[BUILD-DB][MESSAGE!] - Leaving build-db from useq-0.2!"
fi


