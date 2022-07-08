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
   

#print(fiveWordsList)





#[2]---------------------------------------------------
#Implement a function random_word() that takes a list of words as a parameter and returns a random word from this list.
#---------------------------------------------------

def random_word(wordList):
   return random.choice(wordList)



# print(randomWord)



#[3]---------------------------------------------------
#Implement a function is_real_word() that takes two parameters, a guess and a word list and returns True if the word is in the word list and False otherwise.
#---------------------------------------------------



def is_real_word(guessWord,wordList):
   if guessWord in wordList:
      return True

   else:
       return False


#yourGuessedWord = input('Guess a word: ')




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


# print(showStr)
# print(yourGuessedWord)

 

# [5]---------------------------
# Implement a function next_guess() that takes a word list as a parameter. 
# The function asks the user for a guess, converts the guess to lower case and checks if the guess is in the word list. If this is the case, 
# the guess is returned. Otherwise, the function asks the user for another guess.
#-------------------------------


def next_guess(fiveWordsList):
  
  
   while(1):
      yourGuessedWord = input('Please enter a guess:')
      yourGuessedWord = yourGuessedWord.lower()
      print(yourGuessedWord)
      if yourGuessedWord in fiveWordsList:
         return yourGuessedWord
      else:
         print("That's not a real word!")    

     

   
      
   
#[6]-------------------------------------
def play():
  
   c=5
   fiveWordsList = word_list(file)
   randomWord = random_word(fiveWordsList)

   guessedWord=next_guess(fiveWordsList)
   show =check_guess(guessedWord, randomWord)
   print(show)
   isGuessTrue = is_real_word(guessedWord,fiveWordsList)

   if(isGuessTrue):
      while(c!=0):
         if(guessedWord == randomWord ):
            print('You won!')
            return

         guessedWord=input('Please enter a guess:')
         show =check_guess(guessedWord, randomWord)
         print(show)

         c=c-1
         if(c==0):
            print('You lost!')
            print('The word was:',randomWord)
        
   
 
play()

   
   
   

   
 
 