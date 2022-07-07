import random

#---------------------------------------------------
#Implement a function word_list() that reads the 5_letter_words.txt file and returns a list of the words in the file.
#---------------------------------------------------

file = open("words_file.txt","r")
def word_list(file):
   a=file.read().split()

   file2 = open("words_file.txt","w")

   for item in a:
        # write each item on a new line
        file2.write("%s\n" % item)

   # print(a)
   return a

fiveWordsList = word_list(file)
#print(fiveWordsList)





#---------------------------------------------------
#Implement a function random_word() that takes a list of words as a parameter and returns a random word from this list.
#---------------------------------------------------
def random_word(wordList):

   print(random.choice(wordList)) 
   
random_word(fiveWordsList)



