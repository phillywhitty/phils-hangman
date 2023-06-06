import random


def get_random_word():
    # Open the file "words.py" and read all the words into a list
    word_list = open("words.py", "r").read().split('\n')
    # Choose a random word from the list
    random_word = random.choice(word_list)
    # Convert the word to uppercase and return it
    return random_word.upper()
   

def game_intro():
    
    """
    Initial screen that requests and welcomes users
    """

    
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
        


def start_game():
    """
    Starts the game off asking the user to hit Enter to proceed
    """
    print("Press Enter to Start playing Phils-Hangman")

    start = False
    while not start:
      choice = input("\n")
      if choice == "":
         start = True
         number_of_lives = game_level()
         word = get_random_word()
         run_game(word, number_of_lives)

    else:
      print("Please enter to continue")     





def run_game(word, number_of_lives):
    """
    This function will run Phils-Hangman game.
    """

    word_to_guess = "_" * len(word)
    game_over = False
    guesses = []
    lives = number_of_lives
    print("\n")
    print(f"Remaining Lives: {lives}\n")
    print("The word to guess: " + " ".join(word_to_guess) + "\n")

    while not game_over and lives > 0:
        user_attempt = input("Guess a letter:\n ").upper()
        try:
            if len(user_attempt) > 1:
                raise ValueError(f"You can only guess 1 letter at a time. "
                                 f"You guessed {len(user_attempt)} letters.")
            elif not user_attempt.isalpha():
                raise ValueError(f"You can only guess letters."
                                 f"You guessed {user_attempt},which is not a letter.")
            elif len(user_attempt) == 1 and user_attempt.isalpha():
                if user_attempt in guesses:
                    raise ValueError(f""
                                     f"You have already guessed {user_attempt}.")
                elif user_attempt not in word:
                    
                    print(f""
                          f"{(user_attempt)} is not in the word.")
                    print(f"You Lose a Life!")
                    guesses.append(user_attempt)
                    lives -= 1
                else:
                    
                    print(f""
                          f"{user_attempt} is in the word. Great Stuff!")

                    guesses.append(user_attempt)
                    word_to_guess_list = list(word_to_guess)
                    indices = [i for i, letter in enumerate(word)
                               if letter == user_attempt]
                    for index in indices:
                        word_to_guess_list[index] = user_attempt
                        word_to_guess = "".join(word_to_guess_list)
                    if "_" not in word_to_guess:
                        game_over = True

        except ValueError as e_values:
            print(f"{e_values}.\n Please try again. :D\n")
            continue

        print(hangman_lives(lives))

        if lives > 0:
            print(f"Lives: {lives}\n")
            print("The word to guess: " + " ".join(word_to_guess) + "\n")
            print("Letters guessed: " + ", ".join(sorted(guesses)) + "\n")

    if game_over:
        print(f"You Won !")
    else:
        print(f"You Lost !! "
              f"The word you had to Guess was {word}")

    restart_game()

def restart_game():
    """
    This will give user the choice to restart Phils-Hangman or return to Game-Intro
    """
    
    game_restart = False

    while not game_restart:
        restart = input("Do You Want To Play Again :) ?"
                        "Please Type Y for Yes & N for No: ")
        try:
            restart = restart.upper()  
            if restart == "Y":
                game_restart = True
                start_game()
            elif restart == "N":
                game_restart = True
                print("\nReturning to Game-Intro...\n")
                main()
            else:
                raise ValueError("Invalid input. Please type either 'Y' or 'N' to make your choice. "
                                 f"You typed: {restart}")

        except ValueError as e:
            print("Try Again")
  



def game_level():
    """
    Sets game level/number of lives to 7
    """
    level = True
    while level:
       number_of_lives = 7
       return number_of_lives




def hangman_lives(lives):
    lives_left = [  # final state: head, torso, both arms, and both legs
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
    return lives_left[min(lives, len(lives_left) - 1)]

def main():
    """
    Runs the game functions
    """
    
    game_intro()
    start_game()
    word = get_random_word()
    run_game(word, number_of_lives)
   

main()




