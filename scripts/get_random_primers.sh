#!/usr/bin/env bash

PATH_TO_FILE=$1
REPETITIONS=$2
SIZE=$3
MIN_RNAGE=$4
MAX_RANGE=$5
PATH_TO="${PATH_TO_FILE%/*}"

select-random-seqs $PATH_TO_FILE $REPETITIONS $SIZE
p3input 16 18 20 55 60 65 45 50 55 "${MIN_RNAGE}-${MAX_RANGE}" ${PATH_TO_FILE%.*}.${REPETITIONS}.${SIZE}.rnd
mv ${PATH_TO}/*.p3 .

for FILE in *.p3;
do
	primer3_core $FILE > ${FILE}.prm
done

primers-summary "." > primers.rnd.summary.txt
