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

    plaintext = decrypt_file(input_data_bits, initial_vector, key, output_file)

    sample_plaintext = bytes_to_bits(read_file("sample_data/moo_in"))

    # Need to convert to sets to be able to compare the content of lists.
    print(set(plaintext)==set(sample_plaintext))


def decrypt_file(encrypted_file, initial_vector: list, key: list, output_file: str) -> list:
    final_plaintext = []
    for block in range(len(encrypted_file), 0, -16):
        # edge case:
        if block == 16:
            block_Cx = encrypted_file[block-16:block]
            plaintext = XOR(decrypt(block_Cx, key), initial_vector)
            final_plaintext.extend(plaintext)
        else:
            block_Cx = encrypted_file[block-16:block]
            next_block = encrypted_file[block-32:block-16]
            plaintext = XOR(decrypt(block_Cx, key), next_block)
            final_plaintext.extend(plaintext)
    # Maybe have to reverse final_plaintext
    write_file(output_file, bits_to_bytes(final_plaintext))
    return final_plaintext

if __name__=="__main__":
    # how to run: python dec.py ciphertext moo_key moo_iv output_file
    main()
