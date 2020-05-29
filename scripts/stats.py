#!/usr/bin/env python2.7

from sys import argv, exit

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

    return seqs

def num_sequences(hash_table):
    """(HASH[STR:STR]) -> INT
        Returns the number of sequences allocated at hash_table
    """
    return len(hash_table)

def get_seqLen_array(hash_table):
    """

    """
    seqLen = []
    for head, seq in hash_table.iteritems():
        seqLen.append(len(seq))

    return seqLen

def mean(hash_table):
    """(HASH[STR:STR]) -> FLOAT
        Returns the mean of the lengths of all sequences allocated
        at hash_table
    """
    sum = 0.0
    for head, seq in hash_table.iteritems():
        sum += len(seq)
    if len(hash_table) == 0:
        mean = 0
    else:
        mean = sum/len(hash_table)

    return mean

def median(hash_table):
    """

    """
    seqLen = get_seqLen_array(hash_table)
    seqLen = sorted(seqLen, reverse=True)
    if len(seqLen) <= 0:
        median = 0
    elif len(seqLen) % 2 == 0:
        half = len(seqLen) / 2
        median = (seqLen[half-1] + seqLen[half])/2.0
    else:
        median = seqLen[len(seqLen) / 2]
    
    return median

def standard_deviation(hash_table):
    """

    """
    seqLen = get_seqLen_array(hash_table)
    m = mean(hash_table)
    n = len(seqLen)
    summ = 0
    for item in seqLen:
        summ += (item - m) ** 2
    try:
        var = summ / (n - 1)
        sd = var**(1.0/2.0)
        sde = sd / n**(1.0/2.0)
    except Exception:
        sd = 0
        sde = 0
    return (sd, sde)

def N50_up_down(hash_table):
    """

    """
    seqLen = get_seqLen_array(hash_table)
    seqLen = sorted(seqLen, reverse=True)
    if len(seqLen) == 0:
        return (0, 0)
    else: 
        total_nucl = 0
        for item in seqLen:
            total_nucl += item

        nucl_50perc = total_nucl / 2.0
        sum_nucl = 0
        contig_len_N50_up = 0
        contig_len_N50_down = 0
        for item in seqLen:
            sum_nucl += item
            if sum_nucl > nucl_50perc:
                contig_len_N50_down = item
                break
            elif sum_nucl == nucl_50perc:
                contig_len_N50_up = item
                break
            else:
                contig_len_N50_up = item

        return (contig_len_N50_up, contig_len_N50_down)

def L50(hash_table, N50):
    """

    """
    seqLen = get_seqLen_array(hash_table)
    seqLen = sorted(seqLen, reverse=True)
    if len(seqLen) == 0:
        return 0
    else:
        counter = 0
        for item in seqLen:
            if item >= N50:
                counter += 1
            else:
                break

        return counter

def quantiles(hash_table):
    """

    """
    seqLen = get_seqLen_array(hash_table)
    seqLen = sorted(seqLen)
    length = len(seqLen)
    if length == 0:
        return (0, 0, 0, 0, 0, 0)
    else:
        q10 = (length * 10) / 100
        q25 = (length * 25) / 100
        q75 = (length * 75) / 100
        q90 = (length * 90) / 100
        return (seqLen[0], seqLen[-1], seqLen[q10], seqLen[q25], seqLen[q75], seqLen[q90])

def main():
    """

    """
    input_file = argv[1]
    seqs = load(input_file)
    print "[STATS   ][MESSAGE!] - number of sequences = " + str(num_sequences(seqs))
    print "[STATS   ][MESSAGE!] - mean of sequences length = " + str(mean(seqs))
    print "[STATS   ][MESSAGE!] - median of sequences length = " + str(median(seqs))
    print "[STATS   ][MESSAGE!] - N50 up = " + str(N50_up_down(seqs)[0])
    print "[STATS   ][MESSAGE!] - N50 down = " + str(N50_up_down(seqs)[1])
    print "[STATS   ][MESSAGE!] - L50 = " + str(L50(seqs, N50_up_down(seqs)[1]))
    print "[STATS   ][MESSAGE!] - Minimum contig length = " + str(quantiles(seqs)[0])
    print "[STATS   ][MESSAGE!] - Interdecil 10 = " + str(quantiles(seqs)[2])
    print "[STATS   ][MESSAGE!] - Quartile 25 = " + str(quantiles(seqs)[3])
    print "[STATS   ][MESSAGE!] - Quartile 75 = " + str(quantiles(seqs)[4])
    print "[STATS   ][MESSAGE!] - Interdecil 90 = " + str(quantiles(seqs)[5])
    print "[STATS   ][MESSAGE!] - Maximum contig length = " + str(quantiles(seqs)[1])
    print "[STATS   ][MESSAGE!] - Standard deviation = " + str(standard_deviation(seqs)[0])
    print "[STATS   ][MESSAGE!] - Standard error of the mean = " + str(standard_deviation(seqs)[1])

if __name__ == "__main__": main()
