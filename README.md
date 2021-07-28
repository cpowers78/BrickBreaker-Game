:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# Mind Breaker
## CS 110 Final Project
### Spring, 2020
### [Assignment Description](https://drive.google.com/open?id=1HLIk-539N9KiAAG1224NWpFyEl4RsPVBwtBZ9KbjicE)

https://github.com/bucs110/final-project-spring20-the-blue-team.git



### Team: The Blue Team
#### John Hagan, Caterina Powers, Noah Randman

***

## Project Description
Our project is a brick breaker/breakout type of game. When running the game, the initial start screen will appear with a start button. Once started, the game involves the user using the paddle/slider to move along the bottom of the screen, using the Left and Right arrow keys, or the A key for left and D key for right. You should attempt to hit the moving ball. The goal is to hit the ball with the slider and make it hit the all the bricks that are in the upper portion of the screen. Hitting the blocks will make them disappear. The game will be won once all the blocks are gone, or the game will be lost if the user missed hitting the ball with the slider three times, leading the ball to leave the screen and reset. If won a screen asking if you want to continue will appear, but if lost a GAME OVER screen will appear.
***    

## User Interface Design
* ![](assets/STARTSCREENCONCEPT.jpg)
    * This is a concept drawing of the start screen for when you first load the program. There is a start button which you click to start the game. Above the start button there is an image of a brain and above that is the title of the game "MIND BREAKER".
* ![](assets/MAINSCREENCONCEPT.jpg)
This is a concept drawing of the main screen where you play the game. It includes a controllable slider, as well as a moving ball which you attempt to bounce towards the blocks. These blocks will break once they are hit by the ball. The screen will be size 500 by 500.
* ![](assets/WINSCREENCONCEPT.jpg)
    * This is a concept drawing of the win screen which appears once you have won the game. It tells you you have won and then gives you the option to play the game again.
* ![](assets/LOSESCREENCONCEPT.jpg)
    * This is a concept drawing of the lose screen which appears if you lose the game. It merely says "GAME OVER".


* Screenshots of start screen, initial game, winning game screen, and game over losing game screen (in order):
    ![](assets/Startscreengui.jpg)
    ![](assets/gamegui.jpg)
    ![](assets/wingui.jpg)
    ![](assets/gameovergui.jpg)

***        

## Program Design
* Non-Standard libraries:

Pygame: https://www.pygame.org/docs/
- Used to create rectangles and images and sprites, also to program different events
- Perform different functions on the rectangles such as collisions and movement


* Class Interface Design
    * Class Diagram:
         ![class diagram](assets/CLASSDIAGRAM.jpg)
    * This does not need to be overly detailed, but should show how your code fits into the Model/View/Controller paradigm.
* Classes

Controller:
Responsible for creating the GUI and running through the different conditions in order to create the sequence of the game, also keeps track of the game state to ensure the correct screen and desired interface is present on the window

Ball:
Responsible for moving around the screen, has different methods to make sure it bounces off of the sides and does not leave the screen, is used in the controller to collide with block and slider rectangles

Slider:
Reponsible for remaining at the bottom of the screen and sliding back and forth as a result of the users desired input, will collide with the ball, is able to move off of the screen if the user inputs it to

Block:
Responsible for staying at the top of the screen, in the controller it will collide with the ball object and disappear after these collisions, the desired outcome is that all of the blocks are collided with

Gameover:
Responsible for all of the screens in the game besides while the game is running, helps to create sprites for the start screen, the game over screen, and the screen when the user wins the game

***

## Tasks and Responsibilities
* You must outline the team member roles and who was responsible for each class/method, both individual and collaborative.

### Software Lead - John Hagan

 Worked as integration specialist by making sure the code was DRY and was all working together and functioning. Also, ran and tested the code to ensure it was working. Kept code and files organized.

### Front End Specialist - Noah Randman

Front-end lead conducted significant research on creating the controller class. Created the init, mainloop, gameloop, and exit loop. Within the gameloop, added the QUIT event and keyboard events. However, Caterina, the Back End Specialist, led work on the object collision.

### Back End Specialist - Caterina Powers

Created the classes and their methods, created the class diagram, programmed the collisions and window parameters (ball bouncing throughout the screen) in the gameloop and created the startloop, lostgame, and wongame methods of the controller class

## Testing
* In order to test the code we ran the code and conducted all possible scenarios of the games functionality. I would run the code, by typing python3 main.py into terminal, then proceed to click the start button on the initial start screen GUI. I think tested out all possible scenarios for the game classes and functions. I would control the slider with both the left arrow and right arrow keys along with the A and D keys. While running the program and playing the game, I would hit the sides of the screen and the top of the screen with the ball to test if the ball did not go off the screen causing the game to be stuck. I tested the the scenarios of hitting the bricks, missing the ball multiple times. First I would win the game and use the slider to hit the ball and cause collisions with the bricks until all bricks were gone on the game screen GUI, which removed all of them from the sprite group. Once this would happen, it would lead to the "You Win! Continue?" GUI to appear with thumbs up and down images. I would click the thumbs down and it would lead the game to close. I would repeat this until I reappeared on the You Win GUI. This time I would click the thumbs down button, allowing the game to restart. To test if losing the game would work, I would simply go to the game screen GUI and proceed to allow the ball to leave the bottom of the screen 3 times, expecting the "GAME OVER" GUI to show, which it did. I would repeat this multiple times to ensure it was working.

* ATP

| Step                  | Procedure     | Expected Results  | Actual Results |
| ----------------------|:-------------:|:-----------------:|:-------------- |
|  1  | Run the game Program  | GUI window appears with Start Screen and button | GUI Start screen appears with start button |
|  2  | click Start button  | displays second GUI with game(ball, bricks, slider) | Correct GUI appears with moving ball, slider and bricks
|  3  | move slider using left and right arrow keys/ A and D keys to hit ball | ball bounces off slider, hits wall or brick | Slider moves in correct direction of keys, has collision with bricks or wall |
|  4  | Repeat moving slider until all bricks have been hit and are gone | "You Win! Continue?" GUI should appear with clickable thumbs up and down images | Correct GUI appears with images |
|  5  | Click the Thumbs down image on current GUI | GUI should close, game ends | The GUI closes and game is over |
|  6  | Run the game, repeat steps 1-4, then click thumbs up to replay game | Program should return to GUI with Start button | Game program returns to correct GUI, the start screen |
|  7  | Exit program, repeat steps 1 and 2, then allow ball to miss slider 3 times and go off screen | Should lead player to lose, "GAME OVER" GUI appears on screen | Game is lost and correct GUI appears on screen |
