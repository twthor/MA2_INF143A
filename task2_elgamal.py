# Elgamal digital signature scheme
from cipher import read_file, write_file, bits_to_bytes, bytes_to_bits
import sys
import math
import random

def pick_ephemeral_key(public_key: int) -> int:
    temp_key = random.randint(1, public_key-2)
    if math.gcd(temp_key, public_key-1) == 1:
        return temp_key
    return pick_ephemeral_key(public_key)

def main():
    # setup for Elgamal
    setup_arguments()
    # Separates the values from the parameters file
    public_key = int(parameters[0] + "" + parameters[1])
    generator = int(parameters[3])
    beta = int(parameters[5])

    # generates an ephemeral key:
    ephemeral_key = pick_ephemeral_key(public_key)

    # compute r:
    r = (generator**ephemeral_key) % public_key
    # compute s: # ephemeral key her skal være inverse
    eph_inverse = int(pow(ephemeral_key, -1, public_key-1))
    s = ((message - (private_key*r) % public_key-1) * eph_inverse) % (public_key-1)

    # formatting the output
    output_message = f"{r}\n{s}"

    with open(f"{out_file}.txt", "wb") as f:
       f.write(output_message.encode())

    test_output = read_file("task2_elgamal_output.txt").decode("utf-8")
    print(test_output)

    sample_output = read_file("sample_data/elg_output").decode("utf-8")
    print(sample_output)


def setup_arguments():
    global parameters
    parameters = sys.argv[1]
    parameters = read_file(f"sample_data/{parameters}").decode("utf-8")
    global private_key
    private_key = sys.argv[2]
    private_key = int(read_file(f"sample_data/{private_key}").decode("utf-8"))
    global message
    message = sys.argv[3]
    message = int(read_file(f"sample_data/{message}").decode("utf-8"))
    global out_file
    out_file = sys.argv[4]

if __name__=="__main__":
    main()