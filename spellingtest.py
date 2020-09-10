from gtts import gTTS
import time
import os
import vlc

def cls():
    os.system('cls')

def loadWords(fileName):
    with open(fileName) as infile:
        for line in infile:
            words.append(line.strip())

def enterWords(numberOfwords, listOfwords):
    for w in range(0, numberOfwords):
        addWord = str(input("Type word:")).lower().strip()
        listOfwords.append(addWord)

def writeFile(fileName, listOfwords):
    with open(fileName, "w") as f:
        for word in listOfwords:
            f.write("%s\n" % word)

def speakWord(wordTospeak):
    sayWord = gTTS(text=("The word to spell is "+wordTospeak), lang=language, slow=False)
    sayWord.save("sayword.mp3")
    p = vlc.MediaPlayer("sayword.mp3")
    p.play()

language = 'en'
words = []
spellCheck = True
testAgain = True

cls()
print("Press [1] to load a list of words from a file called words.txt, or...")
print("Press [2] to enter a list of words.")
print("- - - - - - - - - - - - - - - - - -")
while True:
    enterLoad = "Enter"
    reply = str(input(enterLoad+" [1] or [2]:")).lower().strip()
    if reply == "1":
        #call function to load words into a list from a file
        loadWords("words.txt")
        break
    elif reply == "2":
        numWords = int(input("Enter number of words to test:"))
        print("Begin to type words to test...\n")
        #call function to enter words into a list
        enterWords(numWords, words)
        #check if the user wants to write the list of words to a file
        writetoFile = "Do you want to write your word list to a file called words.txt?"
        while True:
            reply = str(input(writetoFile+" [y] or [n]:")).lower().strip()
            if reply == "y":
                writeFile("words.txt", words)
                break
            elif reply == "n":
                break
            else:
                print("...please select [y] or [n] only")
                continue
        break
    else:
        print("...please select [1] or [2] only")
        continue
cls()
print("Your list of words is:")
for w in range(len(words)):
    print(words[w])
time.sleep(5)

while testAgain:
    wordCount = 0
    cls()
    print("Get ready to spell your words...\n")
    time.sleep(1)
    print("Here come your words...\n")
    time.sleep(1)
    cls()

    for w in range(len(words)):
        wordCount += 1
        progress = round((wordCount/len(words)*100),0)
        print("Progress:", progress, "%...\n")
        spellCheck = True
        print("The word to spell is:")
        print(words[w])
        speakWord(words[w])
        wrongCount = 0
        time.sleep(2)
        cls()
        while spellCheck:
            if wrongCount == 2:
                print("Remember the word to spell is:")
                print(words[w])
                speakWord(words[w])
                wrongCount = 0
                time.sleep(1)
                cls()
            #ask the user to spell the word
            spellWord = input("Type the word:")
            if spellWord == words[w]:
                print("Correct :-)")
                spellCheck = False
                time.sleep(1)
                cls()
            else:
                print("Incorrect, try again...")
                wrongCount += 1
                time.sleep(1)
                cls()
    
    print("Well done, you finished your list of words!\n")
    while True:
        reply = input(str("Do you want to test your list again? [y] or [n]:")).lower().strip()
        if reply == "y":
            testAgain = True
            break
        elif reply == "n":
            testAgain = False
            break
        else:
            print("...please select [y] or [n] only")
            continue

cls()
print("You're done with testing today! Goodbye :-)")