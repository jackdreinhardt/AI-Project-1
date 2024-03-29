# Getting Started

## Dependencies

- python (version 3.7.1+). It may be possible to run the code in previous versions, however not all functionality is guaranteed. See https://www.python.org for download instructions if python is not installed.
- pygame (version 1.9.4+). It may be possible to run the code in previous versions, however not all functionality is guaranteed. The easiest way to download pygame is using pip, the python package manager. The command is as follows
 `pip install pygame`
 If this fails, see https://www.pygame.org/ for specific instructions on how to download the software.

## Running the Program

It is possible to run the game from an IDE, but it is recommended to use the command line/terminal to access all functionality. Enter the following command into the terminal to start the game with default settings.

`python app.py`

Arguments following this command are used to adjust the settings of the gameplay. They are listed below.

| argument |       function      | default | options              |
|:--------:|:-------------------:|:-------:|:--------------------:|
|  `-b`    | sets the board size | 16      | 6, 16                |
|  `-r`    | number of robots    | 4       | 1 - 4                |
|  `-p1`   | chooses player 1    | Thomas  | any character string |
|  `-p2`   | chooses player 2    | Nina    | any character string |

To choose an AI to play the game, use one of the following special names for `-p1` or `-p2`. If the argument does not match an AI algorithm, a human player will be created with the specified name.

|  name   |          AI          |
|:-------:|:--------------------:|
| bfs     | Breadth-first-search |
| dfs     | Depth-first-search   |
| a-star  | A-Star               |

Examples:
+ `python app.py -b 16 -r 4`
+ `python app.py -r 3 -b 6 -p1 bfs`
+ `python app.py -p1 Bob -p2 Alice`
+ `python app.py -b 6 -r 3 -p2 bfs -p3 dfs`


## Playing the Game

A graphical user interface was created to easily play the game. Most of the instructions are displayed on the bottom right of the screen, but specific instructions are listed here.
1. Choose a player to go first by clicking on the name of the player listed on the right hand side of the screen. This will highlight the selected player.
2. 
+ Human Player:
  Click on a robot to select it, and press the arrow keys to move the robot. Any robot can be selected and moved. The robot with the same color as the target must reach the target to advance the game. If the player cannot reach the target, press the escape button to advance the game.
+ AI player:
  The AI will begin looking for a solution to the problem immediately. Once it finds a solution, it will move the robots accordingly. If it cannot find a solution within 1 minute, it will stop looking.
3. Repeat steps 1-2 until a player reaches the specified number of points to win the game.






