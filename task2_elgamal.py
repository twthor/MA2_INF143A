# Elgamal digital signature scheme
from cipher import read_file, write_file, bits_to_bytes, bytes_to_bits
import sys
def main():
    # setup for elgamal
    setup_elgamal()





def setup_elgamal():
    global parameters
    parameters = sys.argv[1]
    parameters = read_file(f"sample_data/{parameters}").decode("utf-8")
    global private_key
    private_key = sys.argv[2]
    private_key = read_file(f"sample_data/{private_key}").decode("utf-8")
    global message
    message = sys.argv[3]
    message = read_file(f"sample_data/{message}").decode("utf-8")
    global out_file
    out_file = sys.argv[4]
    # Denne biten må flyttes ned etter hvert.
    output_file = write_file(f"sample_data/{out_file}", "hei")
    # output file skal ha r på første linje, så s på andre linje.
    # signature (r, s).

if __name__=="__main__":
    main()