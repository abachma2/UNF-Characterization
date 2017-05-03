#This script loops over all .inp files in the directory and runs them through SCALE

for f in *.inp
    do scalerte -m $f file 
done
