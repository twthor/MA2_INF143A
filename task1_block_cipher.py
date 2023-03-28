from cipher import read_file,\
    write_file, encrypt, decrypt, bits_to_bytes,\
    bytes_to_bits, XOR
import sys

def main():
    file_in = sys.argv[2]
    input_data_bytes = read_file(f"sample_data/{file_in}")
    # convert data of the input file into bits:
    input_data_bits = bytes_to_bits(input_data_bytes)
    # Key
    key_file = sys.argv[3]
    key = read_file(f"sample_data/{key_file}")
    key = bytes_to_bits(key)
    # IV
    initial_vector_file = sys.argv[4]
    initial_vector = read_file(f"sample_data/{initial_vector_file}")
    initial_vector = bytes_to_bits(initial_vector)

    output_file = sys.argv[5]

    # Argument is given by user as if he/she wants to encrypt or decrypt given file.
    desired_function = sys.argv[1]

    if desired_function == "enc":
        ciphertext = encrypt_file(input_data_bits, initial_vector, key, output_file)
    elif desired_function == "dec":
        plaintext = decrypt_file(input_data_bits, initial_vector, key, output_file)

    sample_ciphertext = bytes_to_bits(read_file("sample_data/moo_out"))

    # Decryption: # Just a test to see if encryption and decryption is correct.
    encrypted_file = read_file("task1_encrypted_file.txt")
    encrypted_file = bytes_to_bits(encrypted_file)
    plaintext_test = decrypt_file(encrypted_file, initial_vector, key, output_file)

    # Need to convert to sets to be able to compare the content of lists.
    print(set(plaintext_test)==set(input_data_bits))
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
    main()
