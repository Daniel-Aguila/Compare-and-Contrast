#Your goal is to write a Python function that takes a file handle as input and returns the most common words in the text file.
# Your program should first build a python dictionary that tracks the number of occurrences of every word in the book.
# Assume that words are separated by space. (Note: We did similar program in class).

#Test this with a program that takes a filename as input and prints:
from collections import Counter #Import modules
import collections #import collections overall - might be overdone
#5 most common words
#5 most common words of length greater than 5
#Your code should print the results from the 3 sample files provided with this classwork.

wordsDic = {} #This creates an empty dictionary
fanswers = open('/Users/danielaguila/Desktop/commonAnswers.txt', 'w')
def commonWords(fileName):
    f = open(fileName, "r", encoding="utf8", errors="ignore") #Sets the safety of the f.open()
    lines = f.readlines() #Will read the lines of the file
    for aline in lines: #Seperates every line
        words = aline.split() #Will split every line into words
        for i in words:
            i = i.strip().strip(".").strip(",").strip("/").strip("-").strip(":").strip(";")#Takes away special characters
            i = i.lower() #combines all the upper and lower cases as the same word
            if i in wordsDic.keys():
                wordsDic[i] = wordsDic[i] + 1 #increase how much we see it
            else:
                wordsDic[i] = 1

    fanswers.write("The five most common words for the file: " + fileName + " are:" + "\n") #formating
    fanswers.write("\n")
    for i in dict(Counter(wordsDic).most_common(5)): #print the 5 most common
        fanswers.write(i + ":" + str(wordsDic[i]) + "\n") #actually print it by formating, and also changing the value to a str so it can print
    fanswers.write("The five most common words above 5 letters: "+ fileName + " are:" + "\n")
    fanswers.write("\n")
    count = 1
    s = [(k, wordsDic[k]) for k in sorted(wordsDic, key=wordsDic.get, reverse=True)] #sets the dictionary from highest value to lowest
    for k, v in s: #finds keys,values
        if len(k) > 5: #proceeds to write the words greater than 5 letters
            fanswers.write(k + ":" + str(v) + "\n")
            count = count + 1 #adds a number if value is greater than 5
        if count > 5:
            break
    print("Done.")
    f.close()
#I use the file path because I didn't have them on the same package, otherwise I would have used Constitution.txt
#commonWords(input("Enter your directory here: ")) #It asks for the input directory in here

commonWords("/Users/danielaguila/Desktop/Constitution.txt")
commonWords("/Users/danielaguila/Desktop/a_tale_of_two_cities.txt")
commonWords("/Users/danielaguila/Desktop/twitter_data.txt")
fanswers.close() #close filestxt
#/Users/danielaguila/Desktop/Constitution.txt
#/Users/danielaguila/Desktop/a_tale_of_two_cities.txt
#/Users/danielaguila/Desktop/twitter_data.txt