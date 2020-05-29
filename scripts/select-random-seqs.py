#!/usr/bin/env python2.7
from sys import argv
from random import randrange as RG

def load(seqs_file):
    """(STR) -> HASH[STR:STR]
        Loads the sequences from fasta file and stores them
        in a hash table using the header as hash table key,
        and the sequence as the value.
    """
    seqs = {}
    FHINSEQS = open(seqs_file, "r")

    for line in FHINSEQS:
        line = line.strip("\n")
        if line[0] == ">":
            name = line[1:] #   HEADER DECAPPED!
            seqs[name] = ""
        else:
            seqs[name] += line

    FHINSEQS.close()
    
    return seqs


def get_random_chr_and_position(seqs):
    """(HASH[STR:STR]) -> INT, INT
    Returns a random chromosome and a random position inside that chromosome,
    and returns the name of that chromosome and the random position.

    """
    total_chrs = len(seqs)
    seqsLen = {}
    seqsIdx = {}
    counter = 0
    for head, seq in seqs.iteritems():
        seqsLen[head] = len(seq)
        seqsIdx[counter] = head
        counter += 1
    
    chr_num = RG(0, total_chrs)
    chr_pos = RG(0, seqsLen[seqsIdx[chr_num]])
    chr_name = seqsIdx[chr_num]

    return (chr_name, chr_pos)

def extract_seq(seqs, chr_name, chr_pos, size):
    """(HASH[STR:STR], INT, INT, INT) -> STR
    Returns a DNA string extracted from chr_num chromosome at chr_pos position
    """
    return seqs[chr_name][chr_pos : chr_pos + size]

def main():
    """
        MAIN FUNCTION
    """
    fasta_file = argv[1]
    repetitions = int(argv[2])
    size = int(argv[3])
    the_big_string = ""

    seqs = load(fasta_file)
    
    FHOUT = open(".".join(fasta_file.split(".")[:-1]) + "." + str(repetitions) + "." + str(size) + ".rnd", "w+")
    while repetitions > 0:
        chr_name, chr_pos = get_random_chr_and_position(seqs)
        the_big_string = the_big_string + ">" + chr_name + "|" + str(chr_pos) + "\n" + extract_seq(seqs, chr_name, chr_pos, size) + "\n"
        repetitions -= 1

    FHOUT.write(the_big_string)
    FHOUT.close()

if __name__ == "__main__": main()
