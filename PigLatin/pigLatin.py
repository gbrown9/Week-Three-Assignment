_author_ = "Gabe Brown"

# Program - PigLatin
# CIS - 125
# Translates English to PigLatin


# Declare Vowels and find out how many letters in word
vowels = "aeiou"
Vowels = "AEIOU"
word = ""
pigWord = ""

# Get Input and find first letter
word = input("What is the English word that you would like to translate to PigLatin?")
firstLetter = word[0]


# Translate word to PigLatin
if firstLetter in vowels or firstLetter in Vowels:
  pigWord = word[0:len(word)] + "yay"
else:
  pigWord = word[1:len(word)] + firstLetter + "ay"
  
# Print out answer
print(word, "in PigLatin is:", pigWord)
    