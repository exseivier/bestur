binary_path="/usr/bin"
python_lib="/usr/lib/python2.7"
source_path="scripts"

PYTHON := $(shell which python 2>/dev/null)
BOWTIE := $(shell which bowtie2 2>/dev/null)
SAMTOOLS := $(shell which samtools 2>/dev/null)
CUFFLINKS := $(shell which cufflinks 2>/dev/null)
BLAST := $(shell which blastn 2>/dev/null)

install: print_vars check_programs copy linking end

print_vars:
	@echo "[MESSAGE!] - Configuring your path system"
	@echo "[MESSAGE!] - Binaries path is $(binary_path)"
	@echo "[MESSAGE!] - Python libraries path is $(python_lib)"
	@echo "[MESSAGE!] - Source path is $(source_path)"

check_programs:
ifdef PYTHON
	@echo "[MESSAGE!] - Python... YES!"
else
	@echo "[ERROR!] - Python... NO!"
	@echo "[ERROR!] - Install Python from www.python.org"
	@echo "[ERROR!] - See instructions there"
	@exit 1
endif

ifdef BOWTIE
	@echo "[MESSAGE!] - Bowtie2... YES!"
else
	@echo "[ERROR!] - Bowtie2... NO!"
	@echo "[ERROR!] - Install Bowtie2 to continue"
	@exit 1
endif

ifdef SAMTOOLS
	@echo "[MESSAGE!] - Samtools... YES!"
else
	@echo "[ERROR!] - Samtools... NO!"
	@echo "[ERROR!] - Install samtools to continue"
	@exit 1
endif

ifdef CUFFLINKS
	@echo "[MESSAGE!] - Cufflinks... YES!"
else
	@echo "[ERROR!] - Cufflinks... NO"
	@echo "[ERROR!] - Install Cufflinks to continue"
	@exit 1
endif
ifdef BLAST
	@echo "[MESSAGE!] - BLAST... YES!"
else
	@echo "[ERROR!] - BLAST... NO!"
	@echo "[ERROR!] - Install BLASTn from from NCBI to continue"
	@exit 1
endif

copy: scripts/*.py scripts/*.sh
	@echo "[MESSAGE!] - Copying python libraries to $(python_lib)"
	@sudo cp scripts/dnaprocedures.py scripts/sequences.py $(python_lib)
#	@echo "[MESSAGE!] - Copying scripts to $(source_path)"
#	@cp scripts/*.sh scripts/split.py scripts/select-best-useqs.py scripts/format-seq.py $(source_path)


linking: copy $(source_path)/*.sh $(source_path)/*.py
	@echo "[MESSAGE!] - Linking executable scripts to binary path"
	@ln -s $(source_path)/useq_progressive2.sh $(binary_path)/useq_progressive2
	@ln -s $(source_path)/build-db.sh $(binary_path)/build-db
	@ln -s $(source_path)/split-genome.sh $(binary_path)/split-genome
	@ln -s $(source_path)/split.py $(binary_path)/split
	@ln -s $(source_path)/format-seq.py $(binary_path)/format-seq
	@ln -s $(source_path)/stats.py $(binary_path)/stats
	@ln -s $(source_path)/summarise.py $(binary_path)/summarise
	@ln -s $(source_path)/smy2gtf.py $(binary_path)/smy2gtf
	@ln -s $(source_path)/primers-summary.sh $(binary_path)/primers-summary
	@ln -s $(source_path)/p3input.py $(binary_path)/p3input
	@ln -s $(source_path)/gimme-the-primers2.sh $(binary_path)/gimme-the-primers
	@echo "[MESSAGE!] - Assigning exe permission"
	@chmod 755 $(source_path)/*

end: $(binary_path)/useq $(binary_path)/build-db $(binary_path)/split-genome $(binary_path)/split $(binary_path)/format-seq
	@echo "[MESSAGE!] - USEQ pipeline was installed correctly"
	@echo "[MESSAGE!] - Testing USEQ asking for help"
	@useq_progressive2 --help

clear:
	@echo "[MESSAGE!] - Cleaning useq installation"
	@echo "[MESSAGE!] - Unlinking executable scripts in binary path"
	@unlink $(binary_path)/useq_progressive2
	@unlink $(binary_path)/build-db
	@unlink $(binary_path)/split-genome
	@unlink $(binary_path)/split
	@unlink $(binary_path)/format-seq
	@unlink $(binary_path)/stats
	@unlink $(binary_path)/summarise
	@unlink $(binary_path)/smy2gtf
	@unlink $(binary_path)/primers-summary
	@unlink $(binary_path)/p3input
	@unlink $(binary_path)/gimme-the-primers

#	@rm $(python_lib)/dnaprocedures.py
#	@rm $(python_lib)/dnaprocedures.pyc
#	@rm $(python_lib)/sequences.py
#	@rm $(python_lib)/sequences.pyc
