# Introduction to BESTur
BLAST-Empowered Search Tool to find unique regions. It is a command pipeline I worte in Bash using bioinforatics armory such as: BLAST, Bowtie mapper, Cufflinks assembler, gffread tool, and custom scripts in python to glue the BESTur pipeline. This pipeline is useful to discover unique regions in a query genome (i.e. a pathogen genome). I defined unique region of a genome as a subsequence of it which is absent or is very dissimilar to all possible subsequences of other species genomes.

BESTur takes two files; one file is in fasta format and corresponds to the query genome, and the another file is in plain text format which contains the names of the BLAST-formatted genomes database. In the first step BESTur splits down the query genome in fragments of determined size with a sliding window (window size). The window takes a determined number of bases (step size) each time it cuts another fragment.

BESTur maps the query genome fragments (QGF) to all genomes from batabase with BLAST and keeps the unmapped query fragments (UQF). Then those UQFs are mapped to the reference genome (query genome) to assemble them with cufflinks once they are mapped. The ssequences of the assembled regions are extracted with gffread tool. At the end, the results are stored in a folder named cuff_out.PID where PID is the random selected porcess ID that is useful if several BESTur runs are executed in parallel.

# About requirements
I tested BESTur in a 64-bit-AMD-processor computer in GNU/Linux Debian distro operating system (version 9). I worte the pipeline main script in bash (version 4.4.12). I used the following bioinformatic armory to construct the pipeline: BLAST (2.8.1), Bowtie (2.3.5), Cufflinks (2.2.1), and gffread (from Cufflinks package). I also worte python scripts to glue the pipeline, and in this case I used the version 2.7.13. This pipeline uses two python libraries that shlould be installed in the python libaries path to be used in the scripts.

# Usage
