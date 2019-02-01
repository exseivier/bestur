#!/usr/bin/env bash

PATH_GENOMES_DB=$1
PATH_QUERY_GENOME=$2
SIZE=$3
THIS_PROCESS_PID=$RANDOM

if [ $PATH_GENOMES_DB == "--help" ];
then
	echo "USAGE"
	echo "useq [PATH_GENOMES_DB] [PATH_QUERY_GENOME] [SIZE]"
	exit 0
fi

# BUILDING INDEXES FROM DATABASE GENOMES
build-db $PATH_GENOMES_DB
# ASKING FOR THE PID OF THE LAST PROCESS SENT BY THIS BASH SESSION
#BUILD_PID=$(echo $!)
#echo $BUILD_PID
# TESTING IF PROCESS IS STILL RUNNING.
#TEST_BUILD_PID=$(jobs -p | grep "^$BUILD_PID$")

# SPLITTING GENOME INTO SMALL FRAGMENTS
split-genome $PATH_QUERY_GENOME $SIZE

# WAITING FOR BOTH PROCESSESS TO FINISH
#echo "[WARNING!] - Waiting for build-db & split-genome processess to finish"
#while [ ! -z $TEST_BUILD_PID ];
#do
#	sleep 10
#	TEST_BUILD_PID=$(jobs -p | grep "^$BUILD_PID$")
#	echo $TEST_BUILD_PID
#done
#echo "[MESSAGE] - build-db & split-genome processess finished"

# THE OUTPUT FILES FROM BUILD-DB AND SPLIT-GENOME ARE HARDCODED HERE.
# NAMES OF THESE FILES ARE [] AND [] RESPECTIVELY AND THEY MUST BE IN THE
# SAME FOLDER WERE THIS SCRIPT WAS LAUNCHED.

# MAPPING WITH BOWTIE2
echo -e "\e[102m[MESSAGE!] - Mapping splited query genome sequences at build.db\e[0m"
bowtie2 -x ${PATH_GENOMES_DB}/build.db -fU $(dirname ${PATH_QUERY_GENOME})/splited-genome.fas -S mapped.${THIS_PROCESS_PID}.sam
# MAPPING OUTPUT FILENAME WAS HARDCODED ALSO (mapped.${THIS_PROCESS_PID}.sam)

# SAM <==> BAM & SELECT THOSE UNMAPPED READS
echo "[MESSAGE!] - Selecting unmapped reads"
samtools view -bS -f 4 -T $PATH_QUERY_GENOME -o unmapped.${THIS_PROCESS_PID}.bam mapped.${THIS_PROCESS_PID}.sam 

# BAM <==> FASTA.
echo "[MESSAGE!] - BAM <==> FASTA"
samtools fasta --reference ${PATH_QUERY_GENOME} unmapped.${THIS_PROCESS_PID}.bam > unmapped.${THIS_PROCESS_PID}.fas

# MAPPING UNMAPPED REDAS TO REFERENCE GENOME.
echo "[MESSAGE!] - Mapping unmapped reads to reference genome"
bowtie2-build -f $PATH_QUERY_GENOME $PATH_QUERY_GENOME
bowtie2 -x ${PATH_QUERY_GENOME} -fU unmapped.${THIS_PROCESS_PID}.fas -S unique.${THIS_PROCESS_PID}.sam

#	[TESTING] -  [OK]

echo "[MESSAGE!] - SAM <==> sorted BAM"
samtools view -bS -T ${PATH_QUERY_GENOME} -o unique.${THIS_PROCESS_PID}.bam unique.${THIS_PROCESS_PID}.sam
samtools sort -O BAM -o unique.${THIS_PROCESS_PID}.sort.bam --reference ${PATH_QUERY_GENOME} unique.${THIS_PROCESS_PID}.bam
samtools index unique.${THIS_PROCESS_PID}.sort.bam unique.${THIS_PROCESS_PID}.sort.bai

echo "[MESSAGE!] - Assembling unique reads"
[ -d "cuff_out.${THIS_PROCESS_PID}" ] || mkdir cuff_out.${THIS_PROCESS_PID}
cufflinks -o cuff_out.${THIS_PROCESS_PID} unique.${THIS_PROCESS_PID}.sort.bam

echo "[MESSAGE!] - Extracting exons from gtf"

gffread cuff_out.${THIS_PROCESS_PID}/transcripts.gtf -w cuff_out.${THIS_PROCESS_PID}/exons.fa -g $PATH_QUERY_GENOME

echo "[MESSAGE!] - Calculating MFE"

[ -d RNAfold.${THIS_PROCESS_PID} ] || mkdir RNAfold.${THIS_PROCESS_PID}
RNAfold -i cuff_out.${THIS_PROCESS_PID}/exons.fa --noPS --noLP -d2 -p > RNAfold.${THIS_PROCESS_PID}/exons.MFE.txt

echo "[MESSAGE!] - Selecting BEST unique regions"
select-best-useqs RNAfold.${THIS_PROCESS_PID}/exons.MFE.txt best.useqs.txt

echo "[MESSAGE!] - Cleaning the mess"
rm *.ps

