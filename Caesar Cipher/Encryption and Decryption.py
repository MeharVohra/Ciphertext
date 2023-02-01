# ord() function to convert a character to an integer (ASCII value). 
# This function returns the Unicode code point of that character.
# Unicode is also an encoding technique that provides a unique number to a character. 
# While ASCII only encodes 128 characters, the current Unicode has more than 100,000 characters from hundreds of scripts.

# to get characters from their corresponding ASCII values use the chr() function.

# Do you want to (e)ncrypt or (d)ecrypt?
# > e
# Please enter the key (0 to 25) to use.
# > 4
# Enter the message to encrypt.
# > Meet me by the rose bushes tonight.
# QIIX QI FC XLI VSWI FYWLIW XSRMKLX.

# Do you want to (e)ncrypt or (d)ecrypt?
# > d
# Please enter the key (0 to 26) to use.
# > 4
# Enter the message to decrypt.
# > QIIX QI FC XLI VSWI FYWLIW XSRMKLX.
# MEET ME BY THE ROSE BUSHES TONIGHT.

#%%
# Take inputs from the user
e_or_d = input("Do you want to (e)ncrypt or (d)ecrypt?").lower()
key = input("Please enter the key (0 to 25) to use:")
message = input("Enter the message to encrypt:")

decrypted_message = []
encrypted_message = []

if key == "0":
    print(message)
elif key < "0" or key > "25":
    print("Key not acceptable!\nPlease enter the key (0 to 25) to use:")
else:
    if e_or_d == "e":
        # convert the string of message into a list
        message_list = message.split()
        print(message_list)

        for word in message_list:
            encrypted_word = ""

            for letter in word:
                # convert every character of each word to its ascii value
                ascii_value = ord(letter)
                # add the key (user input) to the ascii value
                encrypt = ascii_value + int(key)
                # convert the new ascii value back its character value
                back_to_letter = chr(encrypt)
                # add this character value to the empty encrypted_ word string variable that we created above
                encrypted_word += back_to_letter
            
            # append all the words to the empty encrypted_message list
            encrypted_message.append(encrypted_word)
        # convert the list back to string    
        encrypted_message = " ".join(encrypted_message)
        print("Encrypted message:\n", encrypted_message)   

    elif e_or_d == "d":    
        message_list = message.split()
        print(message_list)

        for word in message_list:
            decrypted_word = ""

            for letter in word:
                ascii_value = ord(letter)
                # since we want to decrypt the message, we will subtract the key from the ascii value
                decrypt = ascii_value - int(key)
                back_to_letter = chr(decrypt)
                decrypted_word += back_to_letter

            decrypted_message.append(decrypted_word)
        decrypted_message = " ".join(decrypted_message)
        print("Decrypted message:\n", decrypted_message)
   





# %%
