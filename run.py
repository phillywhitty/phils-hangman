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
    word_blank = "_" * len(word)
    print(word_blank)




def main():
    """
    Runs the game functions
    """
    word = get_word()
    game_intro()
    start_game(word)

main()




