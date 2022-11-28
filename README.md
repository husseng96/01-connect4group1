
# Connect 4 


Connect 4 implemented in Python using Pygame.

-----------------------------------------------------------------------------------------------------------------------------------------------------------
# Table of content
1. [ Descripition](https://github.com/cis3296f22/01-connect4group1/blob/main/README.md#descripition) 
2. [ How to play](https://github.com/cis3296f22/01-connect4group1/blob/main/README.md#--how-to-play)      
3. [ How to run](https://github.com/cis3296f22/01-connect4group1/blob/main/README.md#-how-to-run)
4. [How to contribute](https://github.com/cis3296f22/01-connect4group1/blob/main/README.md#how-to-contribute)
5. [License](https://github.com/cis3296f22/01-connect4group1/blob/main/README.md#license)


# Descripition 

This Connect 4 is a two-player game which has a GUI. It is a two-player game that prompts the user to play the classic game Connect 4 by selecting the column on which they want to place the pieces. On the board, either side can win by connecting its four pieces in a straight line horizontally, vertically, or diagonally. Each player will switch turns after dropping a chip and this will continue until someone gets four in a row or there is no more place to place chips.And the UI will provide feedback to the user on whose turn it is and who will win.


<img width="1284" alt="Screenshot 2022-11-26 at 8 19 25 AM" src="https://user-images.githubusercontent.com/64655186/204091031-45e3e8f1-46e7-4eb7-ac38-3f97b9da21d3.png">




# 🎮  How to Play

On the main menu,select the mode(one player or multi player)in which you want to play.Both modes need to set your name and then choose the color for chips you want before the game starts.When either player wins, the game screen is displayed and the player can choose whether to continue the game or exit or return to the main screen to play another mode.




# 💻 How to run


• Download the Python (https://www.python.org/downloads/) or download PyCharm (https://www.jetbrains.com/pycharm/download/#section=mac)

There is a little a bit different install packages between Python IDE and Pycham:

a.Using python IDE:

- Install the  necessary Libraries (NumPy Library, Pygame module,etc):https://www.askpython.com/python/examples/connect-four-game
  
   ```
   pip install numpy
   ```
   ``` 
   pip install PyGame
   ```
   ```
   pip install Button
   ```
   ```
   pip install constants
   ```
   ```
   pip install colour
   ```
   

  (If pip doesn't work, pip3 might work instead. Another way to install numpy and Pygame is to use PyCharm as your IDE and download the extensions through there. You're allowed to download these extensions when hovering over the numpy import statement in connect4.py and the Pygame statement in Button.py.)
  
 b. Using Pycharm:
  
  - go to File → settings → project → python interpreter and add install the package you want(ed:pygame,numpy)
  (https://www.geeksforgeeks.org/managing-packages-in-pycharm/)

  
  
 • Then,clone the repository(https://github.com/cis3296f22/01-connect4group1.git) to your Python IDE or PyCharm and then click “run” to run  your python file 
  
  
 • You will see the output on your Python IDE or Pycham.
 



# How to contribute
•	Any kinds of commits are welcomed.

•	Before making changes in the codes, pull the codes from the remote main branch to your local main branch.

•	If we try to push some changes, please use your  own remote branches other than main branch.

•	Do not merge your code to the remote main branch. Please suggest a pull request and be patient until the owner of this project merges it.

•Follow this project board to know the latest status of the project: https://trello.com/b/AbDVXGNK/connect-four-project-board

# License 
MIT License

Copyright (c) 2022 cis3296f22/connect4group1

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


