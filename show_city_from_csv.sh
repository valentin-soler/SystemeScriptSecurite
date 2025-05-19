#/bin/bash
awk -F',' 'NR>1 {print $3}' out.csv
