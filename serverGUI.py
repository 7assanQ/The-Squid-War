import tkinter as tk
import socket
import threading

name = ''
score = ''
clients = []
ip_input = ''

def destroySetUp(): 
    ip_input = HostIpInput.get() # to stor the ip from the user input
    HostIpInput.destroy() # remove the entery
    confirmBotton.destroy() # remove the button

    info = "Host Ip: " + ip_input + "\n     Leaderboard" # to show the ip and the text Leaderboard

    label1.configure(
        text = info,
        font = ("Arial", 30),
        fg = "white",
        bg = "#8b5500"
    ) # changeing the label to show the ip and the text Leaderboard

    label1.config(image=icon, compound="right") # to add the game icon next to the ip

    startServerThread()
    

def serverInit():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip_input, 9789)) 
    server.listen() # connect to a clinet
    while True: # if this while is removed the code will work for one client if not the program will be stuck
        client, _ = server.accept()
        clients.append(client)
        print("before creating thread for client")
        threading.Thread(target=receivingMessages, args=(client,)).start()
        print("thread created for client")

def receivingMessages(c): # to receive messages from client
    while True:
        try:
            print("before recieving a message")
            recivedText = c.recv(1024).decode() 
            reportText.insert("end", f"{recivedText}\n")
            updateLeaderboard()
            print("message recieved and leaderboard updated")
            if not recivedText:
                print("no message recived")
                break
        except:
            print("message exeption")
            break 
    print("out of message loop remove client")
    clients.remove(c)
    c.close()   
    print("connection closed with client") 

def startServerThread():
    threading.Thread(target=serverInit).start()
    
    
            
window = tk.Tk() # creating the window

window.title("The Squid War Leaderboard") # set window title
window.iconbitmap("assets/squid.ico") # set window icon
window.geometry("550x630") # set window size
window.configure(background = "#8b5500") # set window background

left_icon = tk.PhotoImage(file="assets/squidp.png")
icon = left_icon.subsample(7) # to resize the image

label1 = tk.Label(window, text="Enter Ip Adrress to Host:", compound="center") # create label 
label1.pack()

HostIpInput = tk.Entry(window) # create entry
HostIpInput.pack()

confirmBotton = tk.Button(
    window,
    text="Click",
    command=destroySetUp
    ) # create button to start the run the function destroySetUp when pressed
confirmBotton.pack()

leaderboardText = tk.Text(
    window,
    height = 10,
    width = 30,
    font = ("Arial", 20),
    bg = 'light yellow'
) # to add text field
leaderboardText.pack()

reportText = tk.Text(window,
    height = 10,
    width = 30,
    font = ("Arial", 10),
    bg = '#efba4d')
reportText.pack()

def readReportText(): # to get the names and scores from reportText
    text = reportText.get("1.0", "end-1c") # Get the text from reportText and split it into lines
    lines = text.split("\n")
    
    scores = {} # store the scores
    for line in lines:
        
        parts = line.split(":") # Split the line into name and score
        if len(parts) == 2:
            try: 
                name, score = parts[0], int(parts[1])  
            
                if name in scores: # Add the score to the dictionary
                    scores[name] = max(scores[name], score)
                else:
                    scores[name] = score
            except:
                pass     
   
    sortedScores = sorted(scores.items(), key=lambda x: x[1], reverse=True)  # Sort the scores in descending order
    return sortedScores # to reture the score to sortedScores in updateLeaderboard 

def updateLeaderboard(): #update the leaderboard with the new names and scores
    sortedScores = readReportText() # sortedScores from readReportText
    
    leaderboardText.delete("1.0", "end") # delete everything in the leaderboard
    for name, score in sortedScores:
        leaderboardText.insert("end", f"{name}: {score}\n") # add the new sorted names with scores 

window.mainloop() # start tkinter event loop
