##
experiment_name="evalue"

query="/path/to/query/genome.fna"

db="/path/to/database/database.txt"

declare -a laxo1=(1 -1 0 2)
declare -a laxo2=(1 -1 1 2)
declare -a moderate1=(3 -2 5 5)
declare -a moderate2=(5 -4 8 6)
declare -a moderate3=(5 -4 A 6)
declare -a hard1=(2 -7 2 4)
declare -a hard2=(2 -7 4 2)
declare -a hard3=(2 -5 2 4)
declare -a hard4=(2 -5 4 2)
declare -a names=(laxo1)
declare -A parameters=(\
	[laxo1]=${laxo1[@]} \
	[laxo2]=${laxo2[@]} \
	[moderate1]=${moderate1[@]} \
	[moderate2]=${moderate2[@]} \
	[moderate3]=${moderate3[@]}\
	[hard1]=${hard1[@]} \
	[hard2]=${hard2[@]}\
	[hard3]=${hard3[@]}\
	[hard4]=${hard4[@]})

declare -a window_size=(250)
declare -a identity=(10)
declare -a qcov=(30)
declare -a steps=(50)
declare -a min_frags_per_transfrag=(3)
declare -a overlap_radius=(50)
declare -a evalues=(100)

for name in ${names[@]};
do
	for size in ${window_size[@]};
	do
		for i in ${identity[@]};
		do
			for q in ${qcov[@]};
			do
				for step in ${steps[@]};
				do
					for minf in ${min_frags_per_transfrag[@]};
					do
						for overlap_r in ${overlap_radius[@]};
						do
							for evalue in ${evalues[@]};
							do
								p=${parameters[$name]}
								p1=$([ ${p:0:2} == "A" ] && echo 10 || echo ${p:0:2})
								p2=$([ ${p:2:2} == "A" ] && echo 10 || echo ${p:2:2})
								p3=$([ ${p:4:2} == "A" ] && echo 10 || echo ${p:4:2})
								p4=$([ ${p:6:2} == "A" ] && echo 10 || echo ${p:6:2})
								./useq_progressive2.sh --query $query --db $db --size $size --steps $step --task blastn --evalue $evalue --qcov $q --identity $i --reward $p1 --penalty $p2 --gopen $p3 --gext $p4 --min_frags_per_transfrag $minf --overlap_radius $overlap_r --experiment_name $experiment_name
							done
						done
					done
				done
			done
		done
	done
done


#/home/piruvato/projects/useq_progressive/query/Cauris.genome.fna
#/home/piruvato/projects/useq_progressive/dbase/NoCaur4.txt
