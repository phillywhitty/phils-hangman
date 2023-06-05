import random


def get_random_word():
    
    random_word = random.choice(open("words.py", "r").read().split('\n'))
    return random_word.upper()
   

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
        


def start_game():

    print("Press 1 to Start playing Phils-Hangman")

    start = False
    while not start:
      choice = input("\n")
      if choice == "1":
         start = True
         num_lives = select_game_level()
         word = get_random_word()
         run_game(word, num_lives)

    else:
      print("Please select 1 to continue")     





def run_game(word, num_lives):
    """
    Runs the Hang-Hangman game.
    Hang-Hangman is based around the YouTube video
    https://www.youtube.com/watch?v=m4nEnsavl6w
    """
    word_to_guess = "_" * len(word)
    game_over = False
    guesses = []
    lives = num_lives
    print("\n")
    print(f"Lives: {lives}\n")
    print("The word to guess: " + " ".join(word_to_guess) + "\n")

    while not game_over and lives > 0:
        user_try = input("Guess a letter:\n ").upper()
        try:
            if len(user_try) > 1:
                raise ValueError(f""
                                 f"You can only guess 1 letter at a time. "
                                 f"You guessed {len(user_try)} letter.")
            elif not user_try.isalpha():
                raise ValueError(f""
                                 f"You can only guess letters."
                                 f"You guessed {user_try},is not a letter.")
            elif len(user_try) == 1 and user_try.isalpha():
                if user_try in guesses:
                    raise ValueError(f""
                                     f"You have already guessed {user_try}.")
                elif user_try not in word:
                    
                    print(f""
                          f"{(user_try)} is not in the word.")
                    print(f"Sorry You Lose a Life!")
                    guesses.append(user_try)
                    lives -= 1
                else:
                    
                    print(f""
                          f"{user_try} is in the word. Well done!")

                    guesses.append(user_try)
                    word_to_guess_list = list(word_to_guess)
                    indices = [i for i, letter in enumerate(word)
                               if letter == user_try]
                    for index in indices:
                        word_to_guess_list[index] = user_try
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
        print(f"Congratulations! YOU WON !")
    else:
        print(f"Sorry :( You Loose !! "
              f"The word you had to Guess was {word}")

    restart_game()

def restart_game():
    
    game_restart = False

    while not game_restart:
        restart = input(f"Would You Like To Play Again :) ?"
                        f"Please Type Y for Yes & N for No: ")
        try:
            if restart == "Y":
                game_restart = True
                start_game()
            elif restart == "N":
                game_restart = True
                print("\n")
                main()
            else:
                raise ValueError(f"Please type either Y or N,"
                                 f"to make your Choice.You typed{(restart)}")

        except ValueError as e:
            print(" Please Try Again")
  



def select_game_level():

   level = True
   while level:
      num_lives = 7
      return num_lives








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
    run_game(word, num_lives)
   

main()




