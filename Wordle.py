file = open("words_file.txt","r")
# file = open("words_file.txt","w")

def read_words(file):
   a=file.read().split()

   print(a)
   return a


read_words(file)


