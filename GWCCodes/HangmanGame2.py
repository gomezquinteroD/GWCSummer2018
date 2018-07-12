from random import *
random_words = ["python", "scratch", "algorithm", "comparison", "conditional", "syntax", "variable", "programming", "code"]
rand_word = randint(0,len(random_words)-1)

#currently does not work with words with multiple occurrences of one letter
print("Let's Play Hangman!\n")
real_word = False #is real word?
pick_word = input("Would you like to (1) generate a random word or (2) enter a word:")
if pick_word == "1":
    user_word = random_words[rand_word]
else:
    while real_word == False:
        user_word = input("Please enter a word: ")
        if user_word.isalpha():
            print("Thank you!")
            real_word = True
        else:
            print("That's not a word. Please try again.")
#word confirmed. continue
print("Guess the word now!")
guessed = False
tries = 0 # number of tries
guess_blanks = [] #print blanks of letters
all_guesses = []
for x in user_word:
    guess_blanks.append("_")
print("")
while guessed == False:
    print(guess_blanks)
    print("")
    print("You have guessed:", all_guesses)
    print("Number of failed attempts:", tries)
    print("")
    print("---------------------------------")
    letter_word = input("Would you like to guess a (1) letter or a (2) word? ")
    if letter_word == "1":
        guess = input("Enter a letter: ") #guessed letter
        if guess.isalpha():
            if len(guess) > 1:
                print("More than one letter!")
            else:
                found = False
                for all in range(0,len(user_word)-1):
                    #print("All is: ", all)
                    for x in range(all, len(user_word)):
                        letter = user_word[x]
                        #print("Letter is: ", letter)
                        if guess == letter:
                            #print("LETTER FOUND")
                            index_let = x
                            guess_blanks[x] = guess
                            all += 1
                            found = True
                all_guesses.append(guess)
                if found == True:
                    print("--Correct--")
                else:
                    print("--Letter not found in mystery word--")
                    tries += 1
                if "_" in guess_blanks:
                    continue
                else:
                    guessed = True
                    print("Congrats! You discovered the word:", user_word)
        else:
            print("That's not a letter! Try again")
    elif letter_word == "2":
        guess_word = input("Guess a word: ")
        if guess_word == user_word:
            guessed = True
            print("Congrats! You discovered the word:", user_word)
        else:
            print("Not quite! Try again.")
            tries += 1
