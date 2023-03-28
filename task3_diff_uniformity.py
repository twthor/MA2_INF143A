# TASK 3
# Program to compute differential uniformity of a given (n,n)-function.
import sys

def read_lookup_table(lookup_table):
    with open(f"sample_data/{lookup_table}", "r") as file:
        return file.readlines()


def compute_du(dict_ff: dict) -> int:
    differential_uniformity = 0
    for a in dict_ff:
        if a != 000000:
            for b in dict_ff:
                numberOfPairs = 0
                for x in dict_ff:
                    if dict_ff[x] ^ dict_ff[x^a] == b:
                        numberOfPairs += 1
                if numberOfPairs > differential_uniformity:
                    differential_uniformity = numberOfPairs
    return differential_uniformity


def main():
    given_lookup_table = sys.argv[1]
    lookup_table = read_lookup_table(given_lookup_table)

    dict_ff = {}
    for line in lookup_table:
        num_x = int(line[0:6], 2) # keep it in binary format
        num_Fx = int(line[8:14], 2)
        dict_ff[num_x] = num_Fx

    # Differential uniformity printed to the terminal. No files. Referring to discord messages from Nikolay saying that its okey.
    print(compute_du(dict_ff))


if __name__=="__main__":
    main()