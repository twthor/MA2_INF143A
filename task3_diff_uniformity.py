# TASK 3
# Program to compute differential uniformity of a given (n,n)-function.
import sys

def read_lookup_table(lookup_table):
    with open(f"sample_data/{lookup_table}", "r") as file:
        return file.read()

def compute_du():


def main():
    given_lookup_table = sys.argv[1]
    lookup_table = read_lookup_table(given_lookup_table)
    print(compute_du())


if __name__=="__main__":
    main()