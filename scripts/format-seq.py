#!/usr/bin/env python2.7

def parsingArgs():
    """

    """
    from sys import argv, exit
    if len(argv) != 2:
        print "[ERROR!] - An argument is required, you passed " + len(argv) + " arguments!"
    input_file = argv[1]
    if input_file == "":
        print "[ERROR!] - Empty argument. A fasta file name is required!"
        exit(1)
    else:
        return input_file

def formating_the_god_damn_sequence(input_file):
    """

    """
    FHIN = open(input_file, "r")
    the_big_string = ""
    first_line = FHIN.readline()
    if first_line[0] == ">":
        the_big_string += first_line
    else:
        print "[ERROR!] - Fasta file does not begin with a header!"
        FHIN.close()
        return False
    
    for line in FHIN:
        line = line.strip("\n")
        if line[0] == ">":
            the_big_string += "\n" + line + "\n"
        else:
            the_big_string += line


    FHOUT = open(input_file + ".fmt", "w+")
    FHOUT.write(the_big_string)
    FHIN.close()
    FHOUT.close()

    return True

def main():
    """

    """
    input_file = parsingArgs()
    if formating_the_god_damn_sequence(input_file):
        print "[MESSAGE!] - Success!"
    else:
        print "[ERROR!] - Something went wrong!"

if __name__ == "__main__": main()
