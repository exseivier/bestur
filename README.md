![BESTur logo](/logo/BESTur_logo.png=100x)

# Introduction to BESTur
BLAST-Empowered Search Tool to find unique regions. It is a command pipeline I worte in Bash using bioinforatics armory such as: BLAST, Bowtie mapper, Cufflinks assembler, gffread tool, and custom scripts in python to glue the BESTur pipeline. This pipeline is useful to discover unique regions in a query genome (i.e. a pathogen genome). I defined unique region of a genome as a subsequence of it which is absent or is very dissimilar to all possible subsequences of other species genomes.

BESTur takes two files; one file is in fasta format and corresponds to the query genome, and the another file is in plain text format which contains the names of the BLAST-formatted genomes database. In the first step BESTur splits down the query genome in fragments of determined size with a sliding window (window size). The window takes a determined number of bases (step size) each time it cuts another fragment.

BESTur maps the query genome fragments (QGF) to all genomes from batabase with BLAST and keeps the unmapped query fragments (UQF). Then those UQFs are mapped to the reference genome (query genome) to assemble them with cufflinks once they are mapped. The ssequences of the assembled regions are extracted with gffread tool. At the end, the results are stored in a folder named cuff_out.PID where PID is the random selected porcess ID that is useful if several BESTur runs are executed in parallel.

# About requirements
I tested BESTur in a 64-bit-AMD-processor computer in GNU/Linux Debian distro operating system (version 9). I worte the pipeline main script in bash (version 4.4.12). I used the following bioinformatic armory to construct the pipeline: BLAST (2.8.1), Bowtie (2.3.5), Cufflinks (2.2.1), samtools (1.9) and gffread (from Cufflinks package). I also worte python scripts to glue the pipeline, and in this case I used the version 2.7.13. This pipeline uses two python libraries that shlould be installed in the python libaries path to be used in the scripts.

# Installation

To install this package. After download the package, decompress it and sotre it in a folder, then all the scripts in the scripts folder should be copied into the binary path or you can make symbolic links of the scripts from storage folder pathway to the binary path. This binary path should be updated in the PATH bash environment variable.

[Beta version of makefile is available]

To install this package using makefile. Decompress the project folder and go inside. Once in there type the following command.

sudo make install

This command will copy python libraries to /usr/lib/python2.7 path and will make link files in the path of the binaries /usr/bin to the scripts allocated in the scripts folder. You can change the paths modifying the variables binary_path and python_lib as follow.

~~~
sudo make binary_path=/custom/path/to/binaries python_lib=/user/python/lib install
~~~

In order to uninstall this pipeline just type either one of the following commands depending on how you installed it.

for default instalation.

~~~
sudo make clear
~~~

or for custom installation

~~~
sudo make binary_path=/custom/path/to/binaries python_lib=/user/python/lib clear
~~~

# Usage
useq_progressive2.sh [--query fasta] [--db txt_file] [--size int] [-steps int] [--task blast_task] [--evalue numeric] [--qcov numeric] [--identity numeric] [--reward int] [--penalty int] [--gopen int] [--gext int] [--min_frags_per_transfrag int] [--overlap_radius int] [--experiment_name alphanum]

### Options
~~~
--query ->                      Fasta file of the query genome.  
--db    ->                      Plain text file with the name of the fasta genomes of the database.  
--size  ->                      Window size in nucleotides.  
--steps ->                      Window step size in nucleotides.  
--task  ->                      Blastn task type. [blastn | megablast | discontiguous megablast].  
--evalue  ->                    Expected e-value cutoff.  
--qcov   ->                     Percentage of Query High Scoring Pairwise Segment coverage cutoff.  
--identity  ->                  Percentage of identity cutoff.  
--reward    ->                  Reward score for a succesful match between compared nucleotides in alignment.  
--penalty   ->                  Penalty score for a mismatch between compared nucleotides in alignment.  
--gopen     ->                  Penalty score for the gap existence.  
--gext      ->                  Penalty score for every nulceotide the gap extends.  
--min_frags_per_transfrag ->    Minimum number of fragments covering a query genome region to be considered in the assembling.  
--overlap_radius        ->      The minimum number of nucleotides of the gap between two separated islands of mapped fragments allowed to assembly them.  
--experiment_name       ->      Name of the experiment.  
~~~

Inside scripts folder there is a wrapper script called *launcher.sh*. In order to use it to execute BESTur, it is needed to change the path to candida genomes database (candidaDB) file and the path of the query genome (query) once this package is installed. Yo can modify and test different parameters changing the values of the variables inside this script.
