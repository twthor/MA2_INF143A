# Elgamal digital signature scheme
from cipher import read_file, write_file, bits_to_bytes, bytes_to_bits
import math, random, sys

def pick_ephemeral_key(public_key: int) -> int:
    """Verification of the elgamal digital signature scheme"""
    temp_key = random.randint(1, public_key-2)
    if math.gcd(temp_key, public_key-1) == 1:
        return temp_key
    return pick_ephemeral_key(public_key)

def verification(beta: int, r: int, s: int, p: int, g: int, x: int) -> bool:
    t = (pow(beta, r, p))*(pow(r, s, p)) % p
    return t == pow(g, x, p)

def main():
    # setup for Elgamal
    setup_arguments()
    # Separates the values from the parameters file
    p = int(parameters[0] + "" + parameters[1])
    generator = int(parameters[3])
    beta = int(parameters[5])
    assert beta == pow(generator, private_key, p)

    # generates an ephemeral key:
    ephemeral_key = pick_ephemeral_key(p)

    # compute r:
    r = pow(generator, ephemeral_key, p)

    # compute s:
    eph_inverse = pow(ephemeral_key, -1, p-1)
    s = ((message - (private_key*r)) * eph_inverse) % (p-1)

    # formatting the output
    output_message = f"{r}\n{s}"

    with open(f"{out_file}.txt", "wb") as f:
       f.write(output_message.encode())

    print(verification(beta, r, s, p, generator, message))


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