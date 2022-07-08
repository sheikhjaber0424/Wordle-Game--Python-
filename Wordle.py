import random

#[1]---------------------------------------------------
#Implement a function word_list() that reads the 5_letter_words.txt file and returns a list of the words in the file.
#---------------------------------------------------

file = open("words_file.txt","r")
def word_list(file):
   a = file.read().split()

   file2 = open("words_file.txt","w")

   for item in a:
        # write each item on a new line
        file2.write("%s\n" % item)

   # print(a)
   return a

fiveWordsList = word_list(file)
#print(fiveWordsList)





#[2]---------------------------------------------------
#Implement a function random_word() that takes a list of words as a parameter and returns a random word from this list.
#---------------------------------------------------

def random_word(wordList):
   return random.choice(wordList)



randomWord = random_word(fiveWordsList)

print(randomWord)



#[3]---------------------------------------------------
#Implement a function is_real_word() that takes two parameters, a guess and a word list and returns True if the word is in the word list and False otherwise.
#---------------------------------------------------



def is_real_word(guessWord,wordList):
   if guessWord in wordList:
      return True

   else:
       return False


yourGuessedWord = input('Guess a word: ')
isGuessTrue = is_real_word(yourGuessedWord,fiveWordsList)



# [4]---------------------------
# Implement a function check_guess()that takes two parameters. 
# The first is the guessed word and the second is the word the user has to find. 
# check_guess() returns a string containing the following characters: 
# ---------------------------


def check_guess(yourGuessedWord, randomWord):
   show = []
   dup = []
   for i in range(len(yourGuessedWord)):
    

      if yourGuessedWord[i] in randomWord:

         if yourGuessedWord[i]==randomWord[i]:
            if yourGuessedWord.count(yourGuessedWord[i])>1 and yourGuessedWord[i] in dup:
               show.append('_')                    
            else:
               show.append('X')
               dup.append(yourGuessedWord[i]) 



         if yourGuessedWord[i]!=randomWord[i]:
            if yourGuessedWord.count(yourGuessedWord[i])>1 and yourGuessedWord[i] in dup:
               show.append('_')                    
            else:
               show.append('O')
               dup.append(yourGuessedWord[i])      

            

      if yourGuessedWord[i] not in randomWord:
         show.append('_')
      

   

   return show

showStr = check_guess(yourGuessedWord,randomWord)
print(showStr)
print(yourGuessedWord)

 

# [5]---------------------------
# Implement a function next_guess() that takes a word list as a parameter. 
# The function asks the user for a guess, converts the guess to lower case and checks if the guess is in the word list. If this is the case, 
# the guess is returned. Otherwise, the function asks the user for another guess.
#-------------------------------


def next_guess(fiveWordsList ):
   inp = input('Please enter a guess:')
   
   while(1):
      print(inp)
      if inp in fiveWordsList:
         break
      else:
         inp = input('Please enter a guess:')  


next_guess(fiveWordsList)