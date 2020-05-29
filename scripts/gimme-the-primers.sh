#!/usr/bin/env bash

CUFF_DIR=$1
RANGE_MIN=$2
RANGE_MAX=$3

echo "[PRIMERS ][MESSAGE!] - Searching for the best of the bests primers pair"
EXONS=${CUFF_DIR}/exons.fa
EXONS_FMT=${CUFF_DIR}/exons.fa.fmt
EXONS_L50=${CUFF_DIR}/exons.fa.fmt.l50
STATS=${CUFF_DIR}/useq.stats.txt
format-seq $EXONS
select-L50 $EXONS_FMT $STATS
p3input 16 18 20 55 60 65 45 50 55 "${RANGE_MIN}-${RANGE_MAX}" $EXONS_L50

for FILE in ${CUFF_DIR}/*.p3;
do
	primer3_core $FILE > ${FILE}.prm
done


