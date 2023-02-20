# The-Squid-War

- TheSquidWar.exe is the executable file. 
   - This is the single player full game.
   - No need to download any other files this file is the complete sigle player game.
   
   ![GameIcon](assets/squid.ico)


- gameV11.zip is just a quick way to download both game.py and the assets folder.
   - Just download this folder and extract it in VScode or any other IDE.
   - Once extracted it will show game.py and assets folder.
   - Run the code to play the game.


- gameV12.zip is just a quick way to download both gameWscore.py serverGUI.py and the assets folder.
   - Just download this folder and extract it in VScode or any other IDE.
   - Once extracted it will show 2 files -> gameWscore.py and serverGUI.py and 1 folder the assets folder.
   - Run serverGUI.py and enter the local IP address to host a game.
   
   - To get the IP address write ```ipconfig``` on windows or ```ifconfig``` on linux in command prompt(cmd).
   
   - After setting up the server run gameWscore.py to joing the host server and play the game.
   - If a wrong IP address is provided in gameWscore.py it will try to connect to the host server, then the connection will fail and it is a single player game. have fun.


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
