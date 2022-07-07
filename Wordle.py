file = open("words_file.txt","r")


def read_words(file):
   a=file.read().split()
   file2 = open("words_file.txt","w")
   for item in a:
        # write each item on a new line
        file2.write("%s\n" % item)

   # print(a)
   return a

wordsList = read_words(file)
#print(wordsList)

