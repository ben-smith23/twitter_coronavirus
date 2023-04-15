#!/bin/bash

# set input and output paths
input_folder="./cs46hw/twitter_coronavirus"
output_folder="./cs46hw/twitter_coronavirus/outputs"

# loop over each file in the input folder
for input_path in ${input_folder}/*2020-*.zip; do
    # set output path for current file
    output_path="${output_folder}/$(basename ${input_path} .zip)"

    # run map.py command in the background using nohup and &
    nohup python map.py --input_path "${input_path}" --output_folder "${output_path}" > "${output_path}.log" 2>&1 &

    # print message
    echo "Started processing ${input_path}. Output will be saved to ${output_path}"
done
