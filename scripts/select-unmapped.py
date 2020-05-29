#!/usr/bin/env python2.7

# /*
#   Selects the unmapped sequences from splited-genome.fas using
#   the gene ids of blast searching result.
#
#   Author:     Javier Montalvo-Arredondo
#   Version:    0.1
#   Contact:    buitrejma[at]gmail[dot]com
# */

from sys import argv, exit

def load(seqs_file, gids_file):
    """(STR) -> HASH[STR:STR]
        Loads the sequences from fasta file and stores them
        in a hash table using the header as hash table key,
        and the sequence as the value.
    """
    seqs = {}
    gids = []
    FHINSEQS = open(seqs_file, "r")
    FHINGIDS = open(gids_file, "r")
    for line in FHINSEQS:
        line = line.strip("\n")
        if line[0] == ">":
            name = line[1:]
            seqs[name] = ""
        else:
            seqs[name] += line

    for line in FHINGIDS:
        gids.append(line.strip("\n"))

    FHINSEQS.close()
    FHINGIDS.close()

    return (seqs, gids)

def select_unmapped(seqs, gids):
    """(HASH[STR:STR], ARRAY[STR]) -> HASH[STR:STR]
        Returns a hash table with sequences whose headers
        are not in gids array
    """
    print "[SELECT-U][MESSAGE!] - Running version progressive.\n"
    unmapped_seqs = {}
    for head, seq in seqs.iteritems():
        if head not in gids:
            unmapped_seqs[head] = seq
        # MODIEFIED BY Javier Montalvo 2020-04-24.
        else:
            gids.pop(gids.index(head))
        ##########################################

    return unmapped_seqs

def write_to_fasta(seqs, rand_pid):
    """(HASH[STR:STR]) -> BOOL
    Writes sequences stored in hash table to file in fasta format
    """
    the_big_string = ""
    
    for head, seq in seqs.iteritems():
        the_big_string += ">" + head + "\n" + seq + "\n"

    FHOUT = open("unmapped." + rand_pid + ".fas", "w+")
    FHOUT.write(the_big_string)
    FHOUT.close()

    return True

def main():
    """
        MAIN PROCEDURE
    """
    seqs_file = argv[1]
    gids_file = argv[2]
    rand_pid = argv[3]

    seqs, gids = load(seqs_file, gids_file)
    unmapped_seqs = select_unmapped(seqs, gids)
    if write_to_fasta(unmapped_seqs, rand_pid):
        print "[SELECT-U][MESSAGE!] - " + str(len(unmapped_seqs)) + " unmapped sequences were stored. Success!"

if __name__ == "__main__": main()
