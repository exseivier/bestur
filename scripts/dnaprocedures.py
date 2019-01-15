########################################################################
#
#   Module DNAPROCEDURES
#       This module has functions inmplemented to make procedures
#       on dna sequence to perform sequence preprosessing to carry
#       out dna comparisions and identifying unique sequences in genome.
#
#   Author:     Javier Montalvo-Arredondo.

from sys import argv, exit
from sequences import SEQ_CONTAINER, SEQUENCE

def load(filename, sequence_type="dna"):
    """
        Loads the sequences from fasta file and stores them in
        a SEQ_CONTAINER object.
        Requires the fasta file name.
    """
    container = None
    FHIN = open(filename, "r")
    container = SEQ_CONTAINER(filename)
    for line in FHIN:
        line = line.strip("\n")
        if line[0] == ">":
            name = line[1:] # [WARNING!] - ">" sign from header was removed!
        else:
            seq = SEQUENCE(name, line, sequence_type)
            container.add_last([seq])
    FHIN.close()

    return container

def get_names(cont):
    """(SEQ_CONTAINER) -> ARRAY[STR]
    Takes a SEQ_CONTAINER object and returns an array with the names
    of the sequences in the order which are stroed in object.
    Requires:
        SEQ_CONTAINER object from sequences library.
    Example:
        names <- get_names(SEQ_CONTAINER).
    """

    length = cont.length()
    names = []
    for i in xrange(length):
        names.append(cont.next_at(i).name)

    return names

def get_lengths(cont):
    """(SEQ_CONTAINER) -> ARRAY[INT]
    Takes a SEQ_CONTAINER object and returns an array of integers of the
    length of every sequence stored in SEQ_CONTAINER.
    Requires:
        SEQ_CONTAINER object from sequences libary.
    Example:
        lengths = get_lengths(SEQ_CONTAINER).
    """

    length = cont.length()
    seq_lengths = []
    for i in xrange(length):
        seq_lengths.append(cont.next_at(i).length())

    return seq_lengths

def split_seqs(cont, size):
    """(SEQ_COTAINER, INT) -> SEQ_CONTAINER
    Takes a SEQ_CONTAINER object and for every stored sequence it split
    the seq string into L-k kmers of 'size' size: where L is the sequence
    length.
    Requires:
        SEQ_CONTAINER object from sequences library.
    Example:
        splited_seqs = split_seqs(SEQ_CONTAINER, 300).
        It resturns the splited sequences of 300 nt of size
        for every sequence stored at SEQ_CONTAINER.
    """
    splited_seqs_container = SEQ_CONTAINER(name="splited_sequences")
    total_seqs = cont.length()
    for i in xrange(total_seqs):
        seq_obj = cont.next_at(i)
        seq_len = seq_obj.length()
        seq_name = seq_obj.name
        # MAKING SHORT THE NAME ~
        seq_name = seq_name.split(" ")[0]
        seq_name = seq_name[:10] if len(seq_name) > 10 else seq_name
        # ~ 20190108 MODIFIED.
        sequence = seq_obj.sequence
        for j in xrange(seq_len-size+1):
            splited_seq_name = seq_name + "_f" + str(j)
            splited_seq = SEQUENCE(splited_seq_name, sequence[j:j+size], seq_obj.sequence_type)
            splited_seqs_container.add_last([splited_seq])

    return splited_seqs_container

def write_to_file(cont, format, filename):
    """(SEQ_CONTAINER, STR, STR) -> BOOL
    Takes the SEQ_CONTAINER object and wrties the sequences in a file in fasta format.
    Returns True if success; retruns Flase if not success.
    Raquires:
        SEQ_CONTAINER from sequences library.
    Examples:
        if write_to_file(SEQ_CONTAINER, "fasta", "output.fasta"):
            print "Success!"
        else:
            print "We have a situation!"
    """
    FHOUT = open(filename, "w+")
    total_seqs = cont.length()
    for i in xrange(total_seqs):
        seq_obj = cont.next_at(i)
        str_out = ">" + seq_obj.name + "|" + seq_obj.sequence_type + "\n" + seq_obj.sequence + "\n"
        try:
            FHOUT.write(str_out)
        except Exception:
            print "[ERROR!] - In writing to file!"
            FHOUT.close()
            return False
    FHOUT.close()

    return True

