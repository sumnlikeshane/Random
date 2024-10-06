import random

# Dictionary of words
dic = {
    1: "beautiful", 2: "dreamy", 3: "attractive", 4: "perfect",
    5: "stunning", 6: "pretty", 7: "lovely", 8: "magnificent",
    9: "pulchritudinous", 10: "hot", 11: "dumb"
}

# Randomly pick a word from the dictionary
ran = random.randint(1, 11)
word = dic.get(ran)
length = len(word)
print(word)

n = 0

# Initial message and hidden word
print(f"The word you need to guess is a {length}-letter word:")
fword = "_" * length
print(fword)

# Game loop
while "_" in fword:
    print()
    print("================================================")
    guess = input("Guess a letter: ").lower()
    print("================================================")

    List_fword = list(fword)

    # Validate the input
    if len(guess) != 1:
        print("\nInvalid input. Please enter a single letter.")
    elif guess in word:
        print(f"\n{guess} is in the word and occurs {word.count(guess)} time/s")

        # Update fword to reveal the correct guesses
        # List_fword = list(fword)# Converting the string to a list #now this is muttable
        for i in word:
            
            if i == guess:
                List_fword[n] = guess
            n = n + 1 
        n=0
    
    else:
        print(f"{guess} is not in the word.")
    
    
    fword = ''.join(List_fword) # List_fword i not being called right

    print()
    print(fword)

# Winning message when the word is fully guessed

print("\n================================================")
print(f"Congratulations! You guessed the word: {fword}") 
print("================================================")
    
            
            
        
   
