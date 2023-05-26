import random
from words import list_of_words

def get_word():
    word = random.choice(list_of_words)
    return word
   

def game_intro():
     print("""
    
 __ __   ____  ____    ____  ___ ___   ____  ____  
|  |  | /    ||    \  /    ||   |   | /    ||    \ 
|  |  ||  o  ||  _  ||   __|| _   _ ||  o  ||  _  |
|  _  ||     ||  |  ||  |  ||  \_/  ||     ||  |  |
|  |  ||  _  ||  |  ||  |_ ||   |   ||  _  ||  |  |
|  |  ||  |  ||  |  ||     ||   |   ||  |  ||  |  |
|__|__||__|__||__|__||___,_||___|___||__|__||__|__|
                                                   
    """)

     print('Welcome to Phils HangMan!\n')
     print('What is your name?\n \n')
     name = input('ENTER YOUR NAME:')
     print(f"\n Welcome, {name} \n")
     print('Please press Enter to start the game \n')


def start_game(word):
    word_completion = "_" * len(word)
    game_over = False
    guesses = []
    print("Starting Phils Hangman....")
    print("\n")
    print(word_completion)
    print(f"The word to guess: " + " ".join(list_of_words) + "\n")

    while not game_over:
      user_attempt = input(" Guess a letter:\n")
    


def display_hangman(lives):
    remaining_lives = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
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
    return remaining_lives

def main():
    """
    Runs the game functions
    """
    word = get_word()
    game_intro()
    start_game(word)

main()




