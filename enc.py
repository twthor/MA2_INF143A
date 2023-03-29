from cipher import read_file,\
    write_file, encrypt, decrypt, bits_to_bytes,\
    bytes_to_bits, XOR
import sys

"""Task 1 - block cipher"""
def main():
    file_in = sys.argv[1]
    input_data_bytes = read_file(f"sample_data/{file_in}")
    # convert data of the input file into bits:
    input_data_bits = bytes_to_bits(input_data_bytes)
    # Key
    key_file = sys.argv[2]
    key = read_file(f"sample_data/{key_file}")
    key = bytes_to_bits(key)
    # IV
    initial_vector_file = sys.argv[3]
    initial_vector = read_file(f"sample_data/{initial_vector_file}")
    initial_vector = bytes_to_bits(initial_vector)

    output_file = sys.argv[4]

    ciphertext = encrypt_file(input_data_bits, initial_vector, key, output_file)

    sample_ciphertext = bytes_to_bits(read_file("sample_data/moo_out"))

    # Just a test to see if encryption is correct
    # Need to convert to sets to be able to compare the content of lists.
    print(set(ciphertext)==set(sample_ciphertext))

def encrypt_file(input_data_bits: list, initial_vector: list, key: list, output_file: str) -> list:
    ciphertext = []
    for block in range(0, len(input_data_bits), 16):
        if block == 0:
            xor_with_first_p1 = XOR(initial_vector, input_data_bits[0:block+16])
            block_Cx = encrypt(xor_with_first_p1, key)
            ciphertext.extend(block_Cx)

        plaintext_x = input_data_bits[block:block+16]
        xor_block = XOR(plaintext_x, block_Cx) # next plaintext XOR-ed with previous encrypted block.
        block_Cx = encrypt(xor_block, key) # next encrypted block.
        ciphertext.extend(block_Cx)

    write_file(output_file, bits_to_bytes(ciphertext))
    return ciphertext

if __name__=="__main__":
    # how to run: python enc.py plaintext moo_key moo_iv output_file
    main()
