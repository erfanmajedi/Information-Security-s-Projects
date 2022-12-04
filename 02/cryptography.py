import os , secrets, binascii, pyaes, pbkdf2

# Getting the input which user choose Encryption or Decryption
choose_item = input("Encrypt Or Decrypt ? (Type E for encryption and D for Decryption)\n")

# In this function we decrypt the ciphertext
def steps_to_decryption() :
    
    # reading ciphertext from its file and print it
    with open('Encrypted Text.txt', 'rb') as encrypted_text_file : 
        ciphertext = encrypted_text_file.readline()
        ciphertext = binascii.unhexlify(ciphertext)
    print("ciphertext:", ciphertext)

    # reading Encrypted Key from its file and print it
    with open('Encrypted Key.txt', 'rb') as key_encrypted_file : 
        encrypted_key = key_encrypted_file.readline()
        encrypted_key = binascii.unhexlify(encrypted_key)
    print("Encrypted key: ", encrypted_key)

    # reading the initial vector from its file and print it 
    with open('initial vector.txt', 'r') as initial_vector_file : 
        iv = initial_vector_file.readline()
        # convert initial vector to integer
        iv = int(iv)
    print("Initial Vector: ", iv)

        #read_decrypt.close()

    #read_decrypt = str.encode(read_decrypt)
    #print(read_decrypt)
    
    # AES wit CTR mode
    AES_with_CTR_mode = pyaes.AESModeOfOperationCTR(encrypted_key, pyaes.Counter(iv))
    # decrypted the ciphertext
    decrypted = AES_with_CTR_mode.decrypt(ciphertext)
    # print the initial text which we started with
    print('The Initial Text is :', decrypted)


# In this function we create necessary files for created ciphertext, key and initial vector 
def write_file(ciphertext, password, iv) : 
    with open('Encrypted Text.txt', 'wb') as encrypted_file : 
        encrypted_file.write(ciphertext)
    encrypted_file.close()

    with open('Encrypted Key.txt', 'wb') as encrypted_key_file : 
        encrypted_key_file.write(password)
    encrypted_key_file.close()
    
    with open('initial vector.txt', 'w') as iv_file : 
        # convert initial vector to string 
        iv_file.write(str(iv))
    iv_file.close()

# In this function we encrypt the plaintext
def steps_to_encryption() : 
    
    # reading the key 
    with open('Key.txt', 'r') as key_file : 
        key = key_file.readline()

    # print(key)
    # generate a random salt in each code running
    salt = os.urandom(16)
    # adding the salt to the key
    key_ = pbkdf2.PBKDF2(key, salt).read(32)
    # printing the encryption key in hex
    print('AES encryption key:', binascii.hexlify(key_))

    # creating the initial vector
    iv = secrets.randbits(256)
    # opening the plaintext we want to encrypt
    with open('Code.txt', 'r') as code_file : 
        plaintext = code_file.readline()

    # using AES with CTR mode for encryption
    AES_with_CTR_mode = pyaes.AESModeOfOperationCTR(key_, pyaes.Counter(iv))
    ciphertext = AES_with_CTR_mode.encrypt(plaintext)
    print('ciphertext: ', ciphertext)
    print('Encrypted: ', binascii.hexlify(ciphertext))
    # pass the values to write_file function
    write_file(binascii.hexlify(ciphertext), binascii.hexlify(key_), iv)


# the conditions which was set in project description
if choose_item == 'E' : 
    steps_to_encryption()
if choose_item == 'D' : 
    steps_to_decryption()
