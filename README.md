# Phils Hangman

## **Overview**
Phils Hangman Python game has been developed to run within the Code Institute terminal on Heroku. 
This computerized rendition of the game holds nostalgic value as it recreates the enjoyable experience shared with friends during my school days.
For additional details on the game's rules and historical background, please refer to the provided link. [Wikipedia](https://en.wikipedia.org/wiki/Hangman_(game))

<div align="center"><img src="/assets/images/phils_hangman_cover.png" alt="hangman welcome screen"></div>

[Click here for the final deployed project](https://phils-hangman.herokuapp.com/)


## **Table of Contents**
* [**Phils Hangman**](#Phils Hangman)
  * [**Overview**](#overview)
  * [**Table of Contents**](#table-of-contents)    
* [**Planning Phase:**](#planning-phase)
  * [***User Stories:***](#user-stories)
  * [***Site Aims:***](#site-aims)
  * [***How Will This Be Achieved:***](#how-will-this-be-achieved)
  * [***Game Flow Chart:***](#game-flow-chart)
* [**Features**](#features)
  * [**Welcome Screen:**](#welcome-screen)
    * [**Enter User Name:**](#enter-user-name)
    * [**Play:**](#play)
    * [**Player Wins:**](#player-wins)
    * [**Player Loses:**](#player-loses)
* [**Future Features**](#future-features)
    * [***Diffuculty Levels:***](#diffculty-levels)
    * [***Improved Visuals:***](#improved-visuals)
    * [***Audio:***](#audio)
* [**Testing Phase**](#testing-phase)
* [**Libraries**](#libraries)
    * [***random:***](#random)
    * [***os:***](#os)
* [**Validation**](#validation)
* [**General Testing**](#general-testing)
* [**Bugs**](#bugs)            
* [**Deployment**](#deployment)
  * [***Heroku:***](#heroku)
* [**Credits**](#credits)
* [**Other Comments**](#other-comments)

# **Planning Phase:**
## ***User Stories:***
As a user, I want to be able to:
* Provide a clear and visually engaging interface that immediately communicates the essence of the game right from the beginning.
* Evoke nostalgia by recreating the experience of playing this game during school days, bringing back fond memories.
* Enable users to play a computerized version of hangman independently, allowing them to enjoy the game at their own pace and convenience.

## ***Site Aims:***
The site aims to:
1.Present a user-friendly interface that clearly conveys the nature of the game, eliminating the need for additional explanations from external sources.
1. Ensure prompt and suitable responses to all user inputs, fostering effective communication throughout the game.
1. Implement robust error handling mechanisms to prevent the program from crashing as a result of any erroneous user input.
1. Facilitate an enjoyable solo gaming experience for users, allowing them to fully immerse themselves in the hangman game loop without any hindrances
  
## ***How Will This Be Achieved:***

To accomplish the objectives outlined above, the website will incorporate the following features:
1. Present a visually appealing welcome screen featuring the game name rendered in ASCII art.
1. Implement robust user input handling to ensure that appropriate responses are provided for all user interactions.
1. Whenever the user's input deviates from the expected format, display an error message that informs them of their invalid entry and provides guidance on how to input the expected format.
1. Successfully replicate the original game of hangman by incorporating all of the above elements seamlessly.

## ***Game Flow Chart:***
To understand the steps required in order to program the game, I created the below flowchart using [Canva](https://www.canva.com/).  

<div align="center"><img src="/assets/images/hangman_flowchart.png" alt="hangman flow chart"></div>


# **Features**

## **Welcome Screen:**

The welcome section serves as the initial screen presented to the end user upon loading the page.
It offers an introduction and includes an input field where the user can enter their name. 
Prior to proceeding, the inputted name is validated to ensure its accuracy and completeness.

<div align="center"><img src="/assets/images/welcome_screen_readme.png" alt="hangman welcome screen screenshot"></div>

## **Enter User Name:**

The user is provided with an input field where they can enter their name. 
To validate the input, the user can press the enter button

<div><img src="/assets/images/enter_your_name.png" alt="enter your username screenshot"></div>

## **Play:**


When a player successfully guesses the word within seven lives, they will be presented with an encouraging statement that says "Great Stuff!" 
Additionally, the user will be given the opportunity to decide whether they would like to play again.

<div><img src="/assets/images/game_start.png" alt="game start screenshot"></div>



## **Player Wins:**

When a player guesses the word without losing more than 7 lives they will be propmted with a statement to say Great Stuff !
The user will be also asked if they wish to play again

<div><img src="/assets/images/you_won.png" alt="you won screenshot"></div>

## **Player Loses:**
After a player loses, they will be informed that they have run out of lives, and the word to guess will be displayed.
Additionally, the user will be prompted to decide whether they would like to attempt the game again.


<div><img src="/assets/images/you_lost.png" alt="you lost screenshot"></div>


## **Future Features**
Despite having grand aspirations for further enhancing this game, I faced the common reality of project deadlines. 
Regrettably, I had to prioritize and make compromises.
However, here are some noteworthy features that could have elevated my current project to new heights.

### ***Diffuculty Levels:***
  * I had plans to implement an enhanced gaming experience with customizable difficulty levels. 
    Players would have been able to select their preferred level of challenge at the beginning of the game, with options for easy, medium, and hard modes. 
    This would have allowed for a more tailored and engaging experience, accommodating players of different skill levels
  * Furthermore, expanding the word library would have provided a greater variety of words to match each difficulty level, enriching the gameplay and ensuring a satisfying experience for players. 
    Unfortunately, due to project constraints, these features couldn't be incorporated into the current version.
  
### ***Improved Visuals:***
   * To elevate the visual appeal of the game, I had plans to introduce colorful elements within the console using the external Colorama library. 
     This would have allowed for the integration of vibrant colors to enhance the user interface and make the gameplay more visually engaging.
   * Additionally, one of my aspirations for this project was to incorporate HTML and CSS to create an immersive background. 
     This would have involved leveraging web technologies to introduce captivating visuals, animations, and styling to the game.
  
### ***Audio:***   
   * I had envisioned the inclusion of sound effects to accompany key moments in the game. 
     Specifically, I planned to incorporate sound effects to signify when a player wins or loses the game
   

# **Testing Phase**

# **Libraries**
For this project to work, I required two imported libraries: -
### ***random:***
  * random used to generate a random word from my words.py file
### ***os:***
  * The os system is employed to enhance the user experience by clearing the console. This prevents the display of outdated data from previous rounds, ensuring a more organized and streamlined interface.

# **Validation**

-   Pass Python script through [CI Python Linter](https://pep8ci.herokuapp.com/)
-   No errors found on run script file
<div><img src="/assets/images/ci_python_linter" alt="ci python linter testing screenshot"></div>

# **General Testing**

-   I also ran googles lighthouse testing
<div><img src="/assets/images/lighthouse_testing" alt="lighthouse testing screenshot"></div>

# **Bugs**

 Bug Explanation:
 Previously, there was a bug in the code where it only accepted capital letters for the restart input.
 This meant that lowercase "y" and "n" would not trigger the desired behavior.

 Fix Explanation:
 To fix this bug, I modified the code to convert the restart input to uppercase using the `.upper()` method.
 This change allows for case-insensitive comparisons against "Y" and "N".
 Now, regardless of whether the user enters lowercase or uppercase "Y" or "N", the code will function correctly.

# **Deployment**

# **Heroku**

The app was deployed via Heroku and the live link can be found here [Phils Hangman](https://phils-hangman.herokuapp.com/)

- To deploy the project through Heroku, the following steps were taken:
- Sign up/log in to Heroku.
- Create a new app with a unique name and select the region.
- Access the app's settings and reveal the config vars.
- Add a config var with the key 'PORT' and the value '8000'.
- Add Python as the first buildpack and Node.js as the second buildpack.
- Connect the app to your GitHub repository.
- Choose the branch to deploy and decide on automatic or manual deploys.
- Click 'Deploy Branch' to build the app.
- After successful deployment, a link to the live site will be provided.

# **Credits**

-   Code Institute - [Code Institute](https://github.com/Code-Institute-Org/python-essentials-template)
-   I used Code Institute gitpod full template and Python Essentials in the Full Stack Development course.
-   W3 Schools - [W3 Schools](https://www.w3schools.com/)
-   README.md for the template - https://github.com/Code-Institute-Solutions/readme-template
-   Rory Patrick Sheridan README.md to help with structure content in my README.md - https://github.com/Ri-Dearg/horizon-photo/blob/master/README.md#page-elements
-   Rory Patrick Sheridan for his support throughout my mentor sessions.
-   Slack community
-   Code Institute Tutors.
-   A YouTube video tutorial serves as the foundation for developing my game, providing valuable guidance and instructions. https://www.youtube.com/watch?v=m4nEnsavl6w

# **Other Comments**
I initially embarked on developing a battleship game, but soon realized that it wasn't a perfect fit for me.
As it was a game I didn't play much during my younger years, my personal interest in it was lacking. 
However, this project has been an incredible learning experience for me, and it has deepened my understanding of Python and also Javascript when I reflect on my previous project. 
Although work commitments led me to request an extension for my deadline, I remain hopeful that I will
revisit this project in the future to incorporate the exciting features I mentioned earlier.