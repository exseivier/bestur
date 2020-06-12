# Introduction to BESTur
BLAST-Empowered Search Tool to find unique regions. It is a command pipeline I worte in Bash using bioinforatics armory such as: BLAST, Bowtie mapper, Cufflinks assembler, gffreads tool, and custom scripts in python to glue the BESTur pipeline. This pipeline is useful to discover unique regions in a query genome (i.e. a pathogen genome). I defined unique region of a genome as a subsequence of it which is absent or is very dissimilar to all possible subsequences of other species genomes.

BESTur takes two files; one file is in fasta format and corresponds to the query genome, and the another file is in plain text format which contains the names of the BLAST-formatted genomes database. In the first step BESTur splits down the query genome in fragments of determined size with a sliding window (window size). The window takes a determined number of bases (step size) each time it cuts another fragment.

BESTur maps the query genome fragments (QGF) to all genomes from batabase with BLAST and keeps the unmapped query fragments (UQF). Then those UQFs are mapped to the reference genome (query genome) to assemble them with cufflinks once they are mapped. The ssequences of the assembled regions are extracted with gffreads. At the end, the results are stored in a folder named cuff_out.PID where PID is the random selected porcess ID that is useful if several BESTur runs are executed in parallel.

# About requirements
