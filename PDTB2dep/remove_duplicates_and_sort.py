# remove_duplicates_and_sort.py
# This script removes duplicates and sorts the data.

def remove_duplicates():
    hash_set = set()
    with open("mytemp.txt", 'r') as Ftemp, open("mytempp1.txt", 'w') as Ftemp1:
        for line in Ftemp:
            line = line.strip()
            if line not in hash_set:
                Ftemp1.write(line + "\n")
                hash_set.add(line)

def sort_and_output():
    with open("mytempp1.txt", 'r') as IN, open("mytempout.txt", 'w') as OUT:
        lines = [line.split() for line in IN]
        sorted_lines = sorted(lines, key=lambda x: (int(x[1]), -int(x[2])))
        for out in sorted_lines:
            OUT.write("\t".join(out) + "\n")

if __name__ == "__main__":
    remove_duplicates()
    sort_and_output()

