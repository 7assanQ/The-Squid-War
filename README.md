# ** The Squid War Game **

- TheSquidWar.exe is the executable file. 
   - This is the single player full game.
   - No need to download any other files this file is the complete sigle player game.
   

- TheSquidWarMultiplayer.exe is the executable file.
   - This is the Multiplayer full game.
   - No need to download any other files this file is the complete Multiplayer game.
   - Need someone to run a server to host, so after entering the IP address in the game it will join the server.
   - TheSquidWarMultiplayer.exe will run as a single player game if the wrong IP address is enterd of if there is no server hosting the game (just enter any number in the IP address text field). 

![GameIcon](assets/squid.ico)

- TheSquidWarServer.exe is the executable file.
   - This is the server GUI for the game.
   - No need to download any other files this file is the complete server app for the game.
   - Run the app and enter the local IP address to host other players playing the game.

![ServerIcon](assets/squidServer.ico)


---


# Using the sorce code instead of the exe files

- This game is written in Python, so Python should be Installed. 
   Here is the link for installing Python [link to python](https://www.python.org/downloads/)
   Make sure to check the path box in the install wizard. Recommended to watch any tutorial on how to install python.  

- After installing Python an IDE is recommended to me used to read the source code, such as VScode
   Here is the link for installing VScode [VScode link](https://code.visualstudio.com/download)
   Recommended to watch any tutorial on how to install VScode and Python.
   
- After installing python and any IDE the following libraries need to be installed.   
   - Ursina library (game engine): in command prompt(cmd) write ```pip install ursina``` and click enter. wait for the library to be installed.
   - Tkinter, Threads, socket libraries come along when installing Python.    

** source code is provided in zip folders and in individual files **


---


# zip folders

 - gameV11.zip is just a quick way to download both game.py and the assets folder.
   - Just download this folder and extract it in VScode or any other IDE.
   - Once extracted it will show game.py and assets folder.
   - Run the code to play the game.


- gameV12.zip is just a quick way to download both gameWscore.py serverGUI.py and the assets folder.
   - Just download this folder and extract it in VScode or any other IDE.
   - Once extracted it will show 2 files -> gameWscore.py and serverGUI.py and 1 folder the assets folder.
   - Run serverGUI.py and enter the local IP address to host a game.
   
   - To get the IP address write ```ipconfig``` on Windows or ```ifconfig``` on linux in command prompt(cmd).
   
   - After setting up the server run gameWscore.py to joing the host server and play the game.
   - If a wrong IP address is provided in gameWscore.py it will try to connect to the host server, then the connection will fail and it is a single player game. have fun.


---


# individual files

- The Assets folder includes all the assests needed to run this game. include mp3, jpg, png, and ico.


- game.py is the source code for the single player game.
   - Need to also download the assets folder for it to run.
   - Place both the game.py and the assets folder in the same directory/folder.


- gameWscore.py is the source code for the multiplayer game.
   - Need to also download the assets folder for it to run.
   - Place both the gameWscore.py and the assets folder in the same directory/folder.
   - run gameWscore.py
   - Enter the IP address provided by the host to join the server. have fun playing the game.


- serverGUI.py is the source code for the server for hosting multiple players running gameWscore.py
   - Need to also download the assets folder for it to run.
   - Place both the serverGUI.py and the assets folder in the same directory/folder.
   - run serverGUI.py and enter the local IP address.

   - To get the IP address write ```ipconfig``` on Windows or ```ifconfig``` on Linux in command prompt(cmd).

   - Click the button and wait for players to join.
   - To join run gameWscore.py and make sure the assets folder in the same directory/folder and then enter the same IP address.

