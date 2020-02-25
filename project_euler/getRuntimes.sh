#!/bin/bash

# This script automatically adds the run time for each problem into the first line of every file
# IMPORTANT: My current computer has 'python3' set to execute python 3 code, change to 'python' as needed
list=$(ls *.py)
for i in $list; do
    # CHANGE 'python3' TO 'python' AS NEEDED (uncomment line below)
    # time=$(python $i | grep "seconds")
    time=$(python3 $i | grep "seconds")
    echo $i: $time
    time="# Runtime: $time"
    { printf '%s\n' "$time"; sed '1d' $i; } > tmp.txt && mv tmp.txt $i
done
