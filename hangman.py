#5. hangman 
import random
from words import word_list

def get_word():
    word=random.choice(word_list)
    return word.upper()

def play(word):
    word_completion="_"*len(word)
    guessed=False
    guessed_letters=[]
    guessed_words=[]
    tries=6
    print("Let's begin!")
    print(display_hangman(tries))
    print(word_completion)
    print()

    while not guessed and tries>0:
        guess=input("Please enter your guess: ").upper()
        if len(guess)==1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter ", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -=1
                guessed_letters.append(guess)

            else:
                print("Congratulations!",guess, "is in the word")
                guessed_letters.append(guess)     
                word_as_list=list(word_completion)
                for i in range(len(word)):
                    if word[i]==guess:
                        word_as_list[i]=guess
                    word_completion="".join(word_as_list)

                    if "_" not in word_completion:
                        guessed=True           




        elif len(guess)==len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Yo already guesseed the word", guess)
            elif guess !=word:
                print(guess, "is not the word")   
                tries -=1
                guessed_words.append(guess) 
            else:
                guessed=True
                word_completion=word    

        else:
            print("Not a valid guess.")    
        print(display_hangman(tries))

        print(word_completion)
        print()
    if guessed:
        print("Congrats, you guessed the word! You win!")    
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")    

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]



def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()