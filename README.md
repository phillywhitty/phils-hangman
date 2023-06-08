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
To understand the steps required in order to program the game, I created the below flowchart using [Canva](https://www.lucidchart.com/).  

<div align="center"><img src="/assets/images/hangman_flowchart.png" alt="hangman flow chart"></div>


## Features

### Welcome Screen

The welcome section serves as the initial screen presented to the end user upon loading the page.
It offers an introduction and includes an input field where the user can enter their name. 
Prior to proceeding, the inputted name is validated to ensure its accuracy and completeness.

<div align="center"><img src="/assets/images/welcome_screen_readme.png" alt="hangman welcome screen screenshot"></div>

### Enter User Name

The user is provided with an input field where they can enter their name. 
To validate the input, the user can press the enter button

<div><img src="/assets/images/enter_your_name.png" alt="enter your username screenshot"></div>

### Play


When a player successfully guesses the word within seven lives, they will be presented with an encouraging statement that says "Great Stuff!" 
Additionally, the user will be given the opportunity to decide whether they would like to play again.

<div><img src="/assets/images/game_start.png" alt="game start screenshot"></div>



### Player Wins

When a player guesses the word without losing more than 7 lives they will be propmted with a statement to say Great Stuff !
The user will be also asked if they wish to play again

<div><img src="/assets/images/you_won.png" alt="you won screenshot"></div>

### Player Loses
After a player loses, they will be informed that they have run out of lives, and the word to guess will be displayed.
Additionally, the user will be prompted to decide whether they would like to attempt the game again.


<div><img src="/assets/images/you_lost.png" alt="you lost screenshot"></div>


## **Future-Enhancements**
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
   

## Design

---

## Data Model



## Testing

## Validation

-   Pass Python script through ()
-   No errors found on run script file
<div><img src="" alt=""></div>

## General Testing

-   All errors fixed during testing

[Back to top](#table-of-contents)

---

## Bugs

 Bug Explanation:
 Previously, there was a bug in the code where it only accepted capital letters for the restart input.
 This meant that lowercase "y" and "n" would not trigger the desired behavior.

 Fix Explanation:
 To fix this bug, I modified the code to convert the restart input to uppercase using the `.upper()` method.
 This change allows for case-insensitive comparisons against "Y" and "N".
 Now, regardless of whether the user enters lowercase or uppercase "Y" or "N", the code will function correctly.

## Deployment

### Heroku

The app was deployed via Heroku and the live link can be found here [Battleships Game](https:/)

-   To deploy the project through Heroku, the following steps were taken:
-   Sign up / Log in to [Heroku](https://www.heroku.com/)
-   From the main Heroku Dashboard, press the 'New' button and then press on the 'Create New App' button.
-   Give the project a name (Needs to be a unique name) and then select the region that is suitable to you. After this is done, press on the 'Create App' button.
-   Once the app has been created, you will be redirected to the deploy section. Using the submenu at the top, press on the settings button.
-   Once on the settings page, scroll down a to the 'Config vars' section. Once located, press on the 'Reveal congfig vars' button. This will reveal the current config vars for the app. There should not be any vars configured beforehand.
-   In the KEY input field, input PORT in capital letters and in the VALUE field, input 8000. Then click on the 'Add' button. This needs to be done for the Code Institute template. If you are not using the CI template, you may not need to do this.
-   Next, you need to click on the 'Add buildpack' button below. This should trigger a popup. Select Python as your first buildpack and press on the 'save changes' button.
-   Repeat the above step but this time select Node.js as the buildpack. The order of the buildpacks is important. Python should be first and Node.js second. If you accidently do them in the wrong order, you can click on either buildpacks and drag them to put them in the correct order.
-   Next, you need to navigate to the deploy page which you can do from the submenu at the top of the page.
-   Once on the deploy page, look for the deployment method section and press on the Github logo. Once done, a small section should appear underneath. Click on the 'Connect to GitHub' button. On your first time doing this, you may be promted to follow some steps which you should do.
-   Once done, a 'Connect to GitHub section should appear. Here you will need to search for the repository you want to connect to. You can either type in the repository name in the input field and press search or you can just press search right away and a list of all your repositories should appear and you can press on the one you would like to connect to. Once you have have found the repository you would like to connect to, press on the 'Connect' button on the right hand side.
-   Now that your app has been connected to GitHub, double check the 'Choose a branch deploy' drop down menu is deploying the correct branch from your GitHub Repository. Once you are sure, you need to decide if you would like to enable automatic deploys via the 'Enable Automatic Deploys' button below or if you would like to deploy it manually everytime. The difference is, with automatic deploy, your app will be updated automatically everytime you push the changes in GitHub where as with manual deploy, you will need to go back to the deploy page everytime you want to update the app with the changes. I prefer for it to be automatically done but it is entirely upto you.
-   Once you have decided how you want the deploys to be, press on the deploy branch below. Heroku will now build the app for you. Once it has been completed, a 'Your App Was Successfully Deployed' message will appear with a link the live site.

<div><img src="/assets/images/remove-dependencies.jpg" alt="remove dependencies"></div>

[Back to top](#table-of-contents)

---

# Credits

-   Code Institute - [Code Institute](https://github.com/Code-Institute-Org/python-essentials-template)
-   I used Code Institute gitpod full template and Python Essentials in the Full Stack Development course.
-   W3 Schools - [W3 Schools](https://www.w3schools.com/)
-   README.md for the template - https://github.com/Code-Institute-Solutions/readme-template
-   Rory Patrick Sheridan README.md to help with structure content in my README.md - https://github.com/Ri-Dearg/horizon-photo/blob/master/README.md#page-elements
-   Rory Patrick Sheridan for his support throughout my mentor sessions.
-   Slack community
-   Code Institute Tutors.

[Back to top](#table-of-contents)

---

# Other Comments
