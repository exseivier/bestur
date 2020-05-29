#!/usr/bin/env python2.7

from sys import argv, exit

def parsingArgs():
    """

    """

    min_size    =   argv[1]
    opt_size    =   argv[2]
    max_size    =   argv[3]
    min_tm      =   argv[4]
    opt_tm      =   argv[5]
    max_tm      =   argv[6]
    min_gc      =   argv[7]
    opt_gc      =   argv[8]
    max_gc      =   argv[9]
    prod_size   =   argv[10]
    input_file  =   argv[11]

    return (min_size, opt_size, max_size, min_tm, opt_tm, max_tm, min_gc, opt_gc, max_gc, prod_size, input_file)

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
            name = line[1:]
            seqs[name] = ""
        else:
            seqs[name] += line

    FHINSEQS.close()
    
    return (seqs)


def main():
    """

    """
    min_size, \
    opt_size, \
    max_size, \
    min_tm, \
    opt_tm, \
    max_tm, \
    min_gc, \
    opt_gc, \
    max_gc, \
    prod_size, \
    input_file = parsingArgs()
    seqs = load(input_file)
    counter = 0
    for head, seq in seqs.iteritems():
        FHOUT = open(input_file + "." + str(counter) + ".p3", "w+")
        the_big_string = "SEQUENCE_ID=" + head + "\n" \
                        + "SEQUENCE_TEMPLATE=" + seq + "\n" \
                        + "PRIMER_TASK=generic" + "\n" \
                        + "PRIMER_PICK_LEFT_PRIMER=1" + "\n" \
                        + "PRIMER_PICK_INTERNAL_OLIGO=0" + "\n" \
                        + "PRIMER_PICK_RIGHT_PRIMER=1" + "\n" \
                        + "PRIMER_MIN_SIZE=" + str(min_size) + "\n" \
                        + "PRIMER_OPT_SIZE=" + str(opt_size) + "\n" \
                        + "PRIMER_MAX_SIZE=" + str(max_size) + "\n" \
                        + "PRIMER_GC_CLAMP=3" + "\n" \
                        + "PRIMER_MIN_TM=" + str(min_tm) + "\n" \
                        + "PRIMER_OPT_TM=" + str(opt_tm) + "\n" \
                        + "PRIMER_MAX_TM=" + str(max_tm) + "\n" \
                        + "PRIMER_MIN_GC=" + str(min_gc) + "\n" \
                        + "PRIMER_OPT_GC=" + str(opt_gc) + "\n" \
                        + "PRIMER_MAX_GC=" + str(max_gc) + "\n" \
                        + "PRIMER_PRODUCT_SIZE_RANGE=" + str(prod_size) + "\n" \
                        + "PRIMER_EXPLAIN_FLAG=1" + "\n" \
                        + "="
        FHOUT.write(the_big_string)
        FHOUT.close()

        counter += 1

if __name__ == "__main__": main()
    
