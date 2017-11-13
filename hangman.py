import sys
print "Welcome to Hangman"

# Getting a random word 
from random_words import RandomWords
rw = RandomWords()
word = rw.random_word()
print word

# creating an empty word
guessed = ""
for c in word:
	guessed=guessed+"_"

# Set the number of guesses
noOfGuess=10

# Output to the user
print "Your Word is -->"
for c in guessed:
	print c,
print
print "No of alloted guesses {0} ".format(noOfGuess)

while (noOfGuess > 0):
	print "Enter your Character. You have {0} guesses remaining. ".format(noOfGuess) 
	ch=input()
	if ch in word:
			i=word.index(ch)
			guessed=guessed[:i]+ch+guessed[i+1:]
			word = word[:i] + '_' + word[i+1:]
			print guessed
			if '_' not in guessed:
				print "Congratulations! You Won"
				break 
	else:
			print "Wrong Guess"
			noOfGuess=noOfGuess-1

if noOfGuess==0:
	print "Sorry you lose" 

print "End Game. Thank you for playing" 