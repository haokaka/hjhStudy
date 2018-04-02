#! /bin/bash


for ((k=1; k<=8; k++))
do
	if [ $k -le 4 ]
	then 
		nets=3
	elif [ $k -le 6 ]
	then
		nets=2
	elif [ $k -eq 7]
	then
		nets=4
	else
		nets=5
	fi
	temp=10
	for((i = 1; i <= 7; i++))
	do
		eval=`echo "scale=7; 1/($temp)" | bc`
		temp=10*$temp
		mkdir ./testdata/dataset$k/evalue$eval
		for((j=1; j < 10; j++))
		do
			apha=`echo "scale=1; $j/10" | bc`
			echo dataset$k evalue=$eval alpha=$apha
			mkdir ./testdata/dataset$k/evalue$eval/alpha$apha
			path="./testdata/dataset$k"
		./NetCoffee2 -inputnet $path/dataset$k"_nets.txt" -inputbit $path/dataset$k"_seqsim.txt" -evalue $eval -alph $apha -output $path/evalue$eval/alpha$apha/Result -numnet $nets 	
		done
	done
done
