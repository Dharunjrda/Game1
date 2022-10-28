import random
WORDS = ("python", "jumble", "easy", "difficult", "answer", "photographer", "javascript", "programmer")
word = random.choice(WORDS)
correct = word
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
print("\n\n========== Jumble Word Game ===========")
print("\nUnscramble the letters to make a word.\n\nPress the enter to submit.")
print ("\nThe jumble is:", jumble)
guess = input("\nYour guess: ")
guess = guess.lower()
while (guess != correct) and (guess != ""):
    print ("Sorry that's not it.")
    guess = input("Your guess: ")
    guess = guess.lower
if guess == correct :
    print ("That's it! You guessed right! \n")
print ("Thanks for playing.")
input("\n\nPress the enter key to exit.")
