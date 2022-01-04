#!/bin/bash

if [ $# -ne 5 ]; then
	echo "Usage: ./yolo-data-processing.sh <image-input-dir> <out-path-prefix> <training-perc> <training-outfile> <test-outfile>"
	exit 1
fi

image_input_dir=$1
path_prefix=$2
training_perc=$3
training_outfile=$4
test_outfile=$5

rm -rf $training_outfile $test_outfile

files=$(ls ${image_input_dir}/*.png)
num_files=$(echo $files | wc -w)

let count=training_perc*num_files/100
let i=1

for f in $files; do
	if [ $i -le $count ]; then
		echo $path_prefix/$(basename $f) >> $training_outfile
	else
		echo $path_prefix/$(basename $f) >> $test_outfile
	fi
	let i=i+1
done

