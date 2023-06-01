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
    word_completion = "_" * len(word)
    game_over = False
    guesses = []
    lives = num_lives
    print("Starting Phils Hangman....")
    print("\n")
    
    print(f"The word to guess: " + " ".join(word_completion) + "\n")

    while not game_over and lives > 0:
        user_attempt = input(" Guess a letter:\n").upper()
        try:
            if len(user_attempt) > 1:
               raise ValueError(f"You can only guess 1 letter at a time")

            elif not user_attempt.isalpha():
               raise ValueError(f"You can only guess letters")   

            elif len(user_attempt) == 1 and user_attempt.isalpha():
               if user_attempt in guesses:
                  raise ValueError(f"You have already guessed {(user_attempt)}")

               elif user_attempt not in word:

                  print (f"{(user_attempt)} is not in the word.")

                  guesses.append(user_attempt)  
                  lives -= 1       
    
            else:

               print(f"{(user_attempt)} is in the word. Great Stuff!")

               guesses.append(user_attempt)
               word_completion_list = list(word_completion)
               indices = [i for i, letter in enumerate(word)
                        if letter == user_attempt]
               for index in indices:
                  word_completion_list[index] = user_attempt
                  word_completion = "".join(word_completion_list)
               if "_" not in word_completion:
                  game_over = True 

        except ValueError as e:

         print(f"{e}.\n Please try again.  \n")
         continue 

         print(hangman_lives(lives))

         if lives > 0:
               print(f"Lives: {lives}\n")
               print(f"The word to guess: " + " ".join(word_completion) + "\n")
               print(f"Letters guessed: " + ", ".join(sorted(guesses)) + "\n")

    if game_over:
       print(f"Congratulations! YOU WON !")
    else:
       print(f"The word you had to Guess was {word}")

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
    return lives_left(lives)

def main():
    """
    Runs the game functions
    """
    
    game_intro()
    start_game()
    word = get_random_word()
    run_game(word, num_lives)
   

main()




