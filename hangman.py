import random

word_list = ['fatigued', 'excited', 'happy', 'tired', 'hungry', 'joyful']
word_string = random.choice(word_list)
word_length = len(word_string)
incorrect_guesses = 0
max_incorrect_guesses = 6
guessed_letters = []

def print_hangman():
    stages = [
        """
         --------
         |      |
         |      
         |     
         |     
         |    
         |
         --------
        """,
        """
         --------
         |      |
         |      O
         |     
         |     
         |     
         |
         --------
        """,
        """
         --------
         |      |
         |      O
         |      |
         |     
         |     
         |
         --------
        """,
        """
         --------
         |      |
         |      O
         |     /|
         |     
         |     
         |
         --------
        """,
        """
         --------
         |      |
         |      O
         |     /|\\
         |     
         |     
         |
         --------
        """,
        """
         --------
         |      |
         |      O
         |     /|\\
         |     / 
         |     
         |
         --------
        """,
        """
         --------
         |      |
         |      O
         |     /|\\
         |     / \\
         |     
         |
         --------
        """
    ]
    print(stages[incorrect_guesses])

def print_word():
    display_word = ['_'] * word_length
    for i, letter in enumerate(word_string):
        if letter in guessed_letters:
            display_word[i] = letter
    return display_word

def get_guess():
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Invalid input. Please enter a single alphabetic character.")

def main():
    global incorrect_guesses
    global guessed_letters

    print("Welcome to Hangman!")
    print_hangman()
    print(' '.join(print_word()))

    while '_' in print_word() and incorrect_guesses < max_incorrect_guesses:
        guess = get_guess()
        if guess in word_string:
            print(f"Correct! '{guess}' is in the word.")
            guessed_letters.append(guess)
            print(' '.join(print_word()))
        else:
            print(f"Sorry, there's no '{guess}' in the word.")
            incorrect_guesses += 1
            print_hangman()

    if '_' not in print_word():
        print("Congratulations, you've won!")
    else:
        print(f"Game over! The word was '{word_string}'.")

if __name__ == "__main__":
    main()



