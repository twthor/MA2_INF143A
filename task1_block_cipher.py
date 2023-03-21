from cipher import read_file,\
    write_file, encrypt, decrypt, bits_to_bytes,\
    bytes_to_bits, XOR

def main():
    file_in = input("Write the path of the file you want to encrypt: ")
    input_data_bytes = read_file(file_in)
    # convert data of the input file into bits:
    input_data_bits = bytes_to_bits(input_data_bytes)
    # IV
    initial_vector = read_file("sample_data/moo_iv")
    initial_vector = bytes_to_bits(initial_vector)
    # Key
    key = read_file("sample_data/moo_key")
    key = bytes_to_bits(key)

    encrypt_file(input_data_bits, initial_vector, key)

def encrypt_file(input_data_bits: list, initial_vector: list, key: list):
    ciphertext = ""
    for block in range(0, len(input_data_bits), 16):
        if block == 0:
            xor_with_first_p1 = XOR(initial_vector, input_data_bits[0:block])
            block_Cx = encrypt(xor_with_first_p1, key)
            ciphertext += block_Cx
        plaintext_x = input_data_bits[block:block+16]
        xor_block = XOR(plaintext_x, block_Cx)
        block_Cx = encrypt(xor_block, key)
        ciphertext += block_Cx
    write_file("task1_encrypted_file.txt", bits_to_bytes(ciphertext))

def decrypt_file(encrypted_file, initial_vector: list, key: list):
    final_plaintext = ""
    for block in range(len(encrypted_file), 0, 16):
        # edge case:
        if block-32 == 0:
            block_Cx = encrypted_file[block-16:block]
            next_block = encrypted_file[block-32:block-16]
            plaintext = XOR(decrypt(block_Cx, key), next_block)
            final_plaintext += plaintext

        block_Cx = encrypted_file[block-16:block]
        next_block = encrypted_file[block-32:block-16]
        plaintext = XOR(decrypt(block_Cx, key), next_block)
        final_plaintext += plaintext
    write_file("task1_decrypted_file.txt", bits_to_bytes(final_plaintext))

if __name__=="__main__":
    main()
