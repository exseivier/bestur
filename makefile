binary_path="/usr/bin"
python_lib="/usr/lib/python2.7"
source_path="source"

PYTHON := $(shell which python 2>/dev/null)
BOWTIE := $(shell which bowtie2 2>/dev/null)
SAMTOOLS := $(shell which samtools 2>/dev/null)
CUFFLINKS := $(shell which cufflinks 2>/dev/null)
RNAFOLD := $(shell which RNAfold 2>/dev/null)

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
	@echo "[MESSAGE] - Bowtie2... YES!"
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
ifdef RNAfold
	@echo "[MESSAGE!] - RNAfold... YES!"
else
	@echo "[ERROR!] - RNAfold... NO!"
	@echo "[ERROR!] - Install RNAfold from Vienna Package to continue"
	@exit 1
endif

copy: scripts/*.py scripts/*.sh
	@echo "[MESSAGE!] - Copying python libraries to $(python_lib)"
	@cp scripts/dnaprocedures.py scripts/sequences.py $(python_lib)
	@echo "[MESSAGE!] - Copying scripts to $(source_path)"
	@cp scripts/*.sh scripts/split.py $(source_path)


linking: copy $(source_path)/*.sh $(source_path)/*.py
	@echo "[MESSAGE!] - Linking executable scripts to binary path"
	@ln -s $(source_path)/useq.sh $(binary_path)/useq
	@ln -s $(source_path)/build-db.sh $(binary_path)/build-db
	@ln -s $(source_path)/split-genome.sh $(binary_path)/split-genome
	@ln -s $(source_path)/split.py $(binary_path)/split
	@echo "[MESSAGE!] - Assigning exe permission"
	@chmod 755 $(source_path)/*

end: $(binary_path)/useq $(binary_path)/build-db $(binary_path)/split-genome $(binary_path)/split
	@echo "[MESSAGE!] - USEQ pipeline was installed correctly"
	@echo "[MESSAGE!] - Testing USEQ asking for help"
	@useq --help


