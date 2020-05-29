#!/usr/bin/env python2.7

from sys import argv, exit
def parsingArgs():
    """

    """
    input_file = argv[1]
    stat_file = argv[2]

    return (input_file, stat_file)

def load(seqs_file, stats_file):
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
            name = line[1:]
            seqs[name] = ""
        else:
            seqs[name] += line

    FHINSEQS.close()
    
    FHINSTAT = open(stats_file, "r")
    for line in FHINSTAT:
        line = line.strip("\n")
        line = line.split("-")[1]
        line = line.split("=")
        if line[0].strip(" ") == "N50 down":
            N50d = line[1].strip(" ")
            N50d = float(N50d)
            print N50d
            break

    return (seqs, N50d)

def select_L50(seqs, N50d):
    """

    """
    biggest_seqs={}
    for head, seq in seqs.iteritems():
        if len(seq) >= N50d:
            biggest_seqs[head] = seq
        else:
            continue
    return biggest_seqs

def write_to_file(seqs, input_file):
    """

    """
    the_big_string = ""
    for head, seq in seqs.iteritems():
        the_big_string += ">" + head + "\n" + seq + "\n"
    
    try:
        FHOUT = open(input_file + ".l50", "w+")
        FHOUT.write(the_big_string)
    except Exception:
        print "[SELECT-L][ERROR!] - Fatal error in writing to file."
        FHOUT.close()
        return False

    FHOUT.close()
    return True

def main():
    """

    """
    input_file, stat_file = parsingArgs()
    seqs, N50d = load(input_file, stat_file)
    contigs_l50 = select_L50(seqs, N50d)
    if write_to_file(contigs_l50, input_file):
        print "[SELECT-L][MESSAGE!] - " + str(len(contigs_l50)) + " sequences were stored in file. Success!"
    else:
        print "[SELECT-L][ERROR!] - An error has occurred!"

if __name__ == "__main__": main()
