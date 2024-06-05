


q1 = "Hello I am the song encryptor \n I will encrypt your password based on your favorite song \n Encrypt or Decrypt password?"
print(q1)
done = 0
while done == 0:
    choice = input("Please type your answer: ")
    if choice.upper() == "ENCRYPT":
       import encryption
       done = 1
    elif choice.upper() == "DECRYPT":
        import decryption
        done = 1