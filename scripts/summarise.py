#!/usr/bin/env python2.7

from sys import argv, exit

def load_log(filename):
    """
        Loads the useq.log output file from useq pipeline
        Requires the useq.log file and path
    """
    LOG = {}
    FHIN = open(filename, "r")
    for line in FHIN:
        line = line.strip("\n")
        line = line.split("=")
        if line[0] == "PID":
            PID = line[1]
            LOG[PID] = {}
        elif line[0] == "DB Path":
            LOG[PID]["DB"] = line[1]
        elif line[0] == "QUERY":
            LOG[PID]["QUERY"] = line[1]
        elif line[0] == "WINDOW_SIZE":
            LOG[PID]["WINDOW_SIZE"] = line[1]
        elif line[0] == "STEPS":
            LOG[PID]["STEPS"] = line[1]
        elif line[0] == "TOTAL_SEQS":
            LOG[PID]["TOTAL_SEQS"] = line[1]
        elif line[0] == "COMMAND":
            LOG[PID]["COMMAND"] = line[1]
            command_line = line[1].split("\t")
            LOG[PID]["EVAL"] = command_line[3].split(" ")[1]
            LOG[PID]["IDENT"] = command_line[5].split(" ")[1]
            LOG[PID]["QCOV"] = command_line[8].split(" ")[1]
            LOG[PID]["TASK"] = command_line[9].split(" ")[1]
            LOG[PID]["REWARD"] = command_line[10].split(" ")[1]
            LOG[PID]["PENALTY"] = command_line[11].split(" ")[1]
            LOG[PID]["GOPEN"] = command_line[12].split(" ")[1]
            LOG[PID]["GEXT"] = command_line[13].split(" ")[1]
        elif line[0] == "UNMAPPED_SEQS":
            LOG[PID]["UNMAPPED_SEQS"] = line[1]
        elif line[0] == "MIN_FRAGS_PER_TRANSFRAG":
            LOG[PID]["MIN_FRAGS_PER_TRANSFRAG"] = line[1]
        elif line[0] == "OVERLAP_RADIUS":
            LOG[PID]["OVERLAP_RADIUS"] = line[1]
        elif line[0] == "EXPERIMENT_NAME":
            LOG[PID]["EXPERIMENT_NAME"] = line[1]
        elif line[0] == "Begin" or line[0] == "End" or line[0] == "":
            continue
        else:
            print "[SUMMARIS][ERROR!] - " + line[0] + " Damn load_log!"
            exit(1)

    FHIN.close()
    return LOG

def load_useq_output(filename):
    """
        Loads the useq statistics output from folders cuff.*
        Requires the name of a file containing the paths of the useq.stats.txt files
        for every analysis
    """
    STATS = {}
    useq_stats_files = []
    FHIN = open(filename, "r")
    for line in FHIN:
        line = line.strip("\n")
        FILE = line + "/useq.stats.txt"
        PID = line.split(".")[1]
        STATS[PID] = {}
        FHIN_stats = open(FILE, "r")
        for line_stats in FHIN_stats:
            line_stats = line_stats.strip("\n")
            line_stats = line_stats.split("-")[1]
            line_stats = line_stats.split("=")
            STATS[PID][line_stats[0]] = line_stats[1]

    return STATS
    FHIN.close()

def aggregate_and_write_to_file(log, stat):
    """
        Agregate data from both hash tables based on PID and
        writes them to a output file
        Requires the two hash table objects
    """
    PIDS = log.keys()
    the_big_string = "\t".join(["PID", "DB", "QUERY", \
                                "WINDOW_SIZE", "STEPS", \
                                "EVAL", "IDENT", "QCOV", \
                                "TASK", "REWARD", "PENALTY", \
                                "GOPEN", "GEXT", "MIN_FRAGS_PER_TRANSFRAG", \
                                "OVERLAP_RADIUS", "EXPERIMENT_NAME", \
                                "NoSEQS", "MEAN", "MEDIAN", \
                                "N50_UP", "N50_DOWN", "L50", "MIN_LEN", \
                                "I10", "Q25", "Q75", "I90", \
                                "MAX_LEN", "SD", "SDe", \
                                "UNMAPPED", "TOTAL_SEQS"]) + "\n"
    output_file = "log.stat.tdy"
    for PID in PIDS:
        the_big_string += "\t".join([str(PID),\
                                    log[PID]["DB"],\
                                    log[PID]["QUERY"],\
                                    str(log[PID]["WINDOW_SIZE"]),\
                                    str(log[PID]["STEPS"]),\
                                    str(log[PID]["EVAL"]),\
                                    str(log[PID]["IDENT"]),\
                                    str(log[PID]["QCOV"]),\
                                    log[PID]["TASK"],\
                                    str(log[PID]["REWARD"]),\
                                    str(log[PID]["PENALTY"]),\
                                    str(log[PID]["GOPEN"]),\
                                    str(log[PID]["GEXT"]),\
                                    str(log[PID]["MIN_FRAGS_PER_TRANSFRAG"]),\
                                    str(log[PID]["OVERLAP_RADIUS"]),\
                                    log[PID]["EXPERIMENT_NAME"],\
                                    str(stat[PID][" number of sequences "]),\
                                    str(stat[PID][" mean of sequences length "]),\
                                    str(stat[PID][" median of sequences length "]),\
                                    str(stat[PID][" N50 up "]),\
                                    str(stat[PID][" N50 down "]),\
                                    str(stat[PID][" L50 "]),\
                                    str(stat[PID][" Minimum contig length "]),\
                                    str(stat[PID][" Interdecil 10 "]),\
                                    str(stat[PID][" Quartile 25 "]),\
                                    str(stat[PID][" Quartile 75 "]),\
                                    str(stat[PID][" Interdecil 90 "]),\
                                    str(stat[PID][" Maximum contig length "]),\
                                    str(stat[PID][" Standard deviation "]),\
                                    str(stat[PID][" Standard error of the mean "]),\
                                    str(log[PID]["UNMAPPED_SEQS"]),\
                                    str(log[PID]["TOTAL_SEQS"])])\
                                    + "\n"
    
    ## NEXT
    FHOUT = open(output_file, "w+")
    FHOUT.write(the_big_string)
    FHOUT.close()

    return True
        
    
def main():
    """
        MAIN FUNCTION
    """
    filename = argv[1]
    filename_stats = argv[2]
    log = load_log(filename)
    stat = load_useq_output(filename_stats)
#    print stat
    if aggregate_and_write_to_file(log, stat):
        print "[SUMMARIS][MESSAGE!] - Success! A tidy table was stored in log.stat.tdy file"
    else:
        print "[SUMMARIS][ERROR!] - Problems in collapsing data, and/or in storing data"
        exit(1)

if __name__ == "__main__": main()

