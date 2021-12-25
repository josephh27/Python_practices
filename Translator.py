#def translator(phrase1):
#    translation = ""
#    for letter in phrase1:
#        if letter in "AEIOUaeiou":
#            translation += "g"
#        else:
#            translation += letter
#    return translation

#print(translator(input("Enter the phrase: ")))
'''
middlekid


dasjdsjad
sdaks
'''

def translator(phrase2):
    translation = ""
    phrase2 = phrase2.split()
    for words in phrase2:
        if words.lower() == "okay" or words.lower() == "alright":
            if words.isupper():
                translation += "YEEHAW"
            else: 
                translation += "yeehaw "
        else:
            translation += words + " "
        
    return translation
  


        
print(translator(input("Enter the second phrase: ")))
















#def askPhrase():
#    thePhrase = input("Enter your desired phrase: ")
#    return thePhrase

#phrase = askPhrase()
#translator(phrase)


