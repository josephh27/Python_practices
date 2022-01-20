MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}



#def encrypt(message):
#    encrypted = ""
#    for letter in message:
#        if letter != " ":
#            encrypted += MORSE_CODE_DICT[letter] + " "
#        else:
#            encrypted += " "
#    print(encrypted)


#def decrypt(message):
#    message += " "
#    citext = ""
#    decrypted = ""
#    for letter in message:        
#        if letter != " ":
#            citext += letter
#            space = 0
#        else:
#            space += 1          
#            if space == 1:
#                decrypted += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
#                citext = ""
#            else:
#                decrypted += " "
          
#    print(decrypted)

#if __name__ == "__main__":
#    the_message = input("Input the message to be encrypted: ")
#    encrypt(the_message.upper())
#    the_message1 = input("Input the morse code to be decrypted: ")
#    decrypt(the_message1)




