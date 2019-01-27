import collections
from collections import  Counter

uniqueFile = open("/Users/danielaguila/Desktop/unique.txt",'w') #create a file on writing
fdic = {} #created 3 dictionary for each book, to later compare to
sdic = {}
tdic = {}
def findUnique():
    #Actually open the files and set the conditions to r, encoding and erros
    firstBook = open('/Users/danielaguila/Desktop/Constitution.txt', 'r', encoding="utf8", errors="ignore")
    secondBook = open('/Users/danielaguila/Desktop/a_tale_of_two_cities.txt', 'r', encoding="utf8", errors="ignore")
    thirdBook = open('/Users/danielaguila/Desktop/twitter_data.txt', 'r', encoding="utf8", errors="ignore")

    firstLines = firstBook.readlines() #This process is done 3 times on each book
    for firstline in firstLines: #Seperates every line
        fwords = firstline.split() #Will split every line into words
        for i in fwords: #Goes by every word on the first book
            i = i.strip().strip(".").strip(",").strip("/").strip("-").strip(":").strip(";") #Takes away these special characters. Not sure if you guys wanted acii special characters.
            i = i.lower() #This combines "States" and "states" as one word. (for every word that is like that)
            if i in fdic.keys():
                fdic[i] = fdic[i] + 1
            else:
                fdic[i] = 1
                #uniqueFile.write(i + " " + str(fdic[i])+"\n") #Prints all the words that only appear once in the first book
    secondlines = secondBook.readlines() #repeats
    #uniqueFile.write('=====================================================================')
    #uniqueFile.write("Third Book Words:\n")
    for secondline in secondlines: #Seperates every line
        swords = secondline.split() #Will split every line into words
        for x in swords:
            x = x.strip().strip(".").strip(",").strip("/").strip("-").strip(":").strip(";")
            x = x.lower()
            if x in sdic.keys():
                sdic[x] = sdic[x] + 1
            else:
                sdic[x] = 1
                #uniqueFile.write(x + " " + str(sdic[x])+"\n") #Prints all the words that only appearonce in the first book

    thirdlines = thirdBook.readlines()
    #uniqueFile.write('=====================================================================')
    #uniqueFile.write("Third Book Words:\n")
    for thirdline in thirdlines: #Seperates every line
        twords = thirdline.split() #Will split every line into words
        for z in twords:
            z = z.strip().strip(".").strip(",").strip("/").strip("-").strip(":").strip(";")
            z = z.lower()
            if z in tdic.keys():
                tdic[z] = tdic[z] + 1
            else:
                tdic[z] = 1
                #uniqueFile.write(z + " " + str(tdic[z])+"\n")
    f = 0 #Now we are going to set how many times we find a word that is not in the other books
    for i in fdic.keys(): #Goes through every word on the fdic dictionary
        if i not in sdic.keys() and i not in tdic.keys(): #If is not in the other dictionaries it ups the value by one
            f = f + 1
    percentage1 = (f*100)/(len(fdic.keys())) #We grab the number value (f) times 100(to get percentage_ than divinde by the number of words in the book, accordingly
    a = float("{0:.2f}".format(percentage1))
    uniqueFile.write("The First Book is: "+ str(a)+"% unique.\n")
    s = 0
    for x in sdic.keys():
        if x not in fdic.keys() and x not in tdic.keys():
            s = s + 1
    percentage2 = (s*100)/(len(sdic.keys()))
    g = float("{0:.2f}".format(percentage2))
    uniqueFile.write("The Second Book is: " + str(g)+"% unique.\n")
    t = 0
    for z in tdic.keys():
        if z not in fdic.keys() and z not in sdic.keys():
            t = t + 1
    percentage3 = (t*100)/(len(tdic.keys())) #Also we set len() because we measure the number of words here.
    a = float("{0:.2f}".format(percentage3)) #Format it to fit into two decimal spots
    uniqueFile.write("The Third Book is: " + str(a)+"% unique.\n") #Finally just write it on the txt file

    print("Program Completed.")
    firstBook.close()
    secondBook.close()
    thirdBook.close()
    uniqueFile.close()
#I called them books, because I started to think as them as books, so yeah...
findUnique()
#/Users/danielaguila/Desktop/Constitution.txt
#/Users/danielaguila/Desktop/a_tale_of_two_cities.txt
#/Users/danielaguila/Desktop/twitter_data.txt