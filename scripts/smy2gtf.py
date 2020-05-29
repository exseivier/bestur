#!/usr/bin/env python2.7

from sys import argv, exit

SMY=argv[1]
OUTPUT = ".".join(SMY.split(".")[:-1]) + ".gtf"
FHIN = open(SMY, "r")
FHOUT = open(OUTPUT, "w+")
the_big_string = ""
for line in FHIN:
    line = line.strip("\n")
    line = line.split("\t")
    contig_id   =   line[0]
    chr_name    =   line[1]
    l_coord     =   line[2]
    r_coord     =   line[3]
    penalty     =   line[4]
    l_seq       =   line[5]
    r_seq       =   line[6]
    prm_l_pos   =   line[7]
    prm_r_pos   =   line[8]
    prm_l_tm    =   line[9]
    prm_r_tm    =   line[10]
    amp_size    =   line[11]
    prm_l_coord =   int(l_coord) + int(prm_l_pos.split(",")[0])
    prm_r_coord =   int(l_coord) + int(prm_r_pos.split(",")[0])
    comments = "gene_id \"" + contig_id +\
                "\"; penalty \"" + penalty +\
                "\"; size \"" + amp_size +\
                "\"; l_seq \"" + l_seq +\
                "\"; r_seq \"" + r_seq +\
                "\"; prm_l_tm \"" + prm_l_tm +\
                "\"; prm_r_tm \"" + prm_r_tm
    the_big_string += "\t".join([chr_name, \
                                ".", \
                                contig_id, \
                                str(prm_l_coord), \
                                str(prm_r_coord), \
                                ".", ".", ".", \
                                comments]) + "\n"

FHOUT.write(the_big_string)
FHIN.close()
FHOUT.close()

