# preprocess_input.py
# This script preprocesses the input file by splitting nodes and writing to a temporary file.

import sys

def split_possible_multi_nodes(tmpspan, Ftemp, hash_set):
    if ";" in tmpspan:
        array = tmpspan.split(";")
        for item in array:
            a, b = map(int, item.split(".."))
            Ftemp.write(f"{item}\t{a}\t{b}\t{abs(a-b)}\n")
            hash_set.add(item)
    else:
        a, b = map(int, tmpspan.split(".."))
        Ftemp.write(f"{tmpspan}\t{a}\t{b}\t{abs(a-b)}\n")
        hash_set.add(tmpspan)

def preprocess_input_file(input_file):
    with open(input_file, 'r') as F, open("mytemp.txt", 'w') as Ftemp:
        for line in F:
            line = line.strip()
            array = line.split('|')
            tmpNode = array[14].strip()
            split_possible_multi_nodes(tmpNode, Ftemp, set())
            tmpNode = array[20].strip()
            split_possible_multi_nodes(tmpNode, Ftemp, set())

if __name__ == "__main__":
    input_file = sys.argv[1]
    preprocess_input_file(input_file)

