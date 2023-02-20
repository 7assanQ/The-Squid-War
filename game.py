from ursina import *
from random import randint

window.title = "The Squid War" # title of the game, no idea why it is only working if it is before app = Ursina()
window.icon = "assets/squid.ico"

app = Ursina()

def update():   # update evry frame   

    global offset, run, score, gameOverCheck, info, splashSound, bloodShape, spawningDelay, checktime
    global speed1, speed2, colorPic, sizeing, shooting, bulletsLimit, level# using the veriables from outside this update function

    if run:     # run is set to true

        offset += time.dt * 0.1     # speed of backGround
        setattr(backGround, "texture_offset", (offset, 0)) # to move the backGround to the left

        player.y += held_keys['w'] * 8.5 * time.dt    # moving and rotating the player using w and s keys
        player.y -= held_keys['s'] * 8.5 * time.dt
        player.x += held_keys['d'] * 2 * time.dt
        player.x -= held_keys['a'] * 5 * time.dt

        rotate_up = held_keys['w'] * -10
        rotate_down = held_keys['s'] * 10

        if rotate_up != 0:
            player.rotation_z = rotate_up
        else:
            player.rotation_z = rotate_down  

        for monster in monsters:         # to move all monsters to the left
            monster.x -= random.randint(speed1, speed2) * time.dt

            kill = monster.intersects()  # to detect any intersectoin with monesters

            if len(bullets) >= bulletsLimit: # if the bullets list is full reload and clear list
                    shooting = False

            if (kill.entity in bullets) or (kill.entity == player) or (kill.entity == wall1):   # when the kill is tregered remove a monster from the list and the sky box 
                destroy(bullet) # i don't like this, it should destroy the bullet that hits the squid and not the last bullet

                bloodShape += random.randint(1, 2)   # to get a random number between 1, 2

                if bloodShape % 2 == 0:   # to chech if even blood 1 if odd blood 2
                    blood = Animation('assets/purpleBlood2',
                                        position = (monster.x, monster.y),
                                        scale = 4
                                        )
                    invoke(destroy, blood, delay = 0.3)
                else:    
                    blood2 = Animation('assets/purpleBlood',
                                        position = (monster.x, monster.y),
                                        scale = 5
                                        )
                    invoke(destroy, blood2, delay = 0.3)

                monster.color = color.red # turn color to res when killed
                monsters.remove(monster)
                invoke(destroy, monster, delay = 0.1) 
                score += 1
                text = 'Score: ' + str(score) + level  
                info.text = text
                splashSound += random.randint(1, 2)

                if score >= 400:            # all the levels and their conditions
                    speed1, speed2 = 16, 16
                    spawningDelay = 0.5
                    level = '\nLevel: 9'
                elif score >= 320:
                    speed1, speed2 = 13, 13
                    spawningDelay = 0.7
                    level = '\nLevel: 8'
                elif score >= 260:
                    speed1, speed2 = 12, 13
                    sizeing = 1
                    level = '\nLevel: 7'
                elif score >= 170:
                    spawningDelay = 0.6
                    speed1, speed2 = 10, 11
                    colorPic = color.red
                    level = '\nLevel: 6'
                elif score >= 130:
                    spawningDelay = 0.7
                    level = '\nLevel: 5'
                elif score >= 90:
                    sizeing = 1.5
                    speed1, speed2 = 9, 12
                    level = '\nLevel: 4'
                elif score >= 45:
                    sizeing = 1
                    spawningDelay = 0.85
                    speed1, speed2 = 8, 12
                    level = '\nLevel: 3'
                elif score >= 15:
                    spawningDelay = 1
                    speed1, speed2 = 8, 9 
                    level = '\nLevel: 2'     

                if splashSound % 2 == 0:   # to chech if even sound 1 if odd sound 2
                    Audio('assets/splash1.mp3', volume = 0.3)
                    Audio('assets/creatureHurt.mp3', volume = 0.1)
                else:    
                    Audio('assets/splash2.mp3', volume = 0.4)
                    Audio('assets/creatureHurt.mp3', volume = 0.1)

            dead = player.intersects()    
            
            if ((kill.entity == player) or (kill.entity == wall1) or (dead.entity == wall1) or  # player hit a squid or left wall, squid hit left wall  
                (dead.entity == wall2) or (dead.entity == wall3) or (dead.entity == wall4)):    # player hit top, right, bottom wall
                invoke(gameOver2, delay = 5 * time.dt)   # game over
                             
    checktime += 0.5 * time.dt  # to ceheck form if there is no squeds on the scene
    if checktime >= 7:  # sfter sometime
        if not monsters:       # spawn a monster if there are no monster in the mpnsters arrey 
            spawnAgain()
        checktime = 0                  

def gameOver():         # display a gameover text with the score. 
    global score, info4

    info4 = Text(
        text = "Game Over\nYour Score Is: " + str(score) + "\nPress R To Reload The Game",
        origin = (0,0),
        background = True 
        )       
    
def gameOver2():    
    global lives, run, gameOverCheck

    if lives == 1:          # reverced if statment it will execute the 3'rd condetion, then 2'nd, then first
        destroy(gear1)      # remove the gear icon from the scene  
        Audio('assets/gearHit1.mp3', volume = 4)
        lives -= 1          # not needed but it is needed in the other conditions, just counter for player lives

        run = False         # stop the game
        gameOverCheck = False   # to prevent pauseing and unpausing the game after losing 
        Audio('assets/explosion.mp3')
        invoke(Func(player.shake, duration = 2))    # effects shake, fade_out
        invoke(Func(player.fade_out, duration = 2))
        invoke(gameOver, delay = 2)     # wait then display gameover with score

        propeller.volume = 0            # set the plane audio to zero 
    elif lives == 2:    # same as the first if statement
        destroy(gear2)
        Audio('assets/gearHit1.mp3', volume = 4)
        lives -= 1
    elif lives == 3:    # same as the first if statement
        destroy(gear3)   
        Audio('assets/gearHit1.mp3', volume = 4)
        lives -= 1
        
def fire():
    global bullet

    if gunSound % 2 == 0:   # to chech if even sound 1 if odd sound 2
        Audio('assets/bullet1.mp3', volume = 1.2)
    else:    
        Audio('assets/bullet2.mp3', volume = 1.2)

    bullet = Entity(         
        y = player.y,
        x = player.x + 2.5,
        model ='cube',
        texture = 'assets/bullet',
        collider = 'box',
        ) # creating a bullet based on the player position

    bullet.animate_x(
        30,
        duration = 2,
        curve = curve.linear 
        ) # speed of bullet, acceleration of bullet. lower faster, linear motion of the bullet.

    bullets.append(bullet)   # add the bullet to the list of moving bullets
    invoke(destroy, bullet, delay = 1)   # delay time to destroy the bullets
    removebulitCounter()

def removebulitCounter():
    global bulitCounterList, indexcheck

    if len(bulitCounterList) != 0:   # if the bullet array is not empty
        destroy(bulitCounterList.pop())     # remove the last bullet added to the array and remove it from the scene
        indexcheck = 0      
        
def fireReload():
    global bullets, shooting, indexB, bulitCounterList, indexcheck, bulitCounterX, bulitCounterY

    bullets.clear() # clear the bulit list
    shooting = True # to be able to shoot again 
    bulitCounterList = [0]*bulletsLimit # reset the size of the bulits
    indexB = 0 # index for bullets array
    bulitCounterX = 0   # to go back to line one when showing bullets
    bulitCounterY = 8.3
    indexcheck = 0      #to keep checking when index 19 = 0
    for i in range(40):
        magazine()   

def magazine():     # reloading the magazine, handleing the array and the entity on scene
    global bulitCounter, bulitCounterX, bulitCounterY, gearLocation, indexB, indexcheck

    bulitCounter = Entity(
        model = 'cube',
        texture = 'assets/bullet',
        scale = 0.5,
        rotation_z = 270,
        x = gearLocation -0.5 + bulitCounterX , # to show under the gears
        y = bulitCounterY
    )

    bulitCounterList[indexB] = bulitCounter # add the bulits to the magazine
    indexB += 1                                  
    bulitCounterX += 0.2 

    if indexcheck == 0:      # only if still printing in the first line of bullits
        if bulitCounterList[19] != 0:  # after there are 20 in the first line
            bulitCounterX = 0
            bulitCounterY = 7.9 # print in the 2'd line
            indexcheck = 1     # to keep showing bullets in the 2'nd line, fireReload() will go back to the first line        

def reloadGame():
    global run, pause, check, spawningDelay, checktime, speed1, speed2, colorPic, sizeing, gearLocation, shooting, bulletsLimit 
    global bulitCounterX, bulitCounterY, lives, gameOverCheck, gunSound, splashSound, bloodShape, indexB, indexcheck, score, level
    global monsters, gears, bullets, bulitCounterList, gear0, gear1, gear2, gear3, info3, info, player, wall1, wall2, wall3, wall4
    global bullet, bulitCounter, backGround, offset, blood, monster, player0, info2

    # reset all variables ------
    run = False      # run boolean veriable, to only run the game when true using the update function
    pause = True # boolean for pausing the game
    check = True # boolean to Start the game
    spawningDelay = 2 # spped of monsters
    checktime = 0 # chinking the empty monsters list
    speed1, speed2, = 5, 8 # speed of monstere
    colorPic = None # color of monsters
    sizeing = 2 # size of sqid
    gearLocation = -11.5 # posion x of gear
    shooting = True # for the gun reload
    bulletsLimit = 40 # number of bullets
    bulitCounterX = 0
    bulitCounterY = 8.3
    lives = 3 # if 0 means game over
    gameOverCheck = True # boolean to end the game and prevent the pause
    gunSound = 0    # viriable for gun sound
    splashSound = 0 # for the moster kill sound
    bloodShape = 0   # for boold shapes 1 and 2
    indexB = 0 # for bulits in array
    indexcheck = 0 # for bullit array check
    score = 0   
    level = '\nLevel: 1'
    # reset all variables ------

    # reset options text ------
    info3 = Text('Press S To Start The Game\nPress P To Pause And Unpause\nPress R To Reload The Game', origin = (0,0))
    info3.background = True
    # reset options text ------

    # remove pause message if reset on pause ------
    destroy(info2) 
    # remove pause message if reset on pause ------

    # remove gameover message -----
    destroy(info4)
    # remove gameover message -----

    # reset score and level ------
    text = 'Score: ' + str(score) + level  
    info.text = text
    # reset score and level ------

    #remove squids from the scene -----
    for i in range(len(monsters)): # destroy the remaining monesters   
        destroy(monsters.pop())
    #remove squids from the scene -----


    # reset all arrays -----
    monsters = []   
    gears = []      
    bullets = []    
    # reset all arrays -----

    # restart bullets ------
    for i in range(len(bulitCounterList)): # destroy the remaining bullets in the magazine   
        destroy(bulitCounterList.pop())     

    bulitCounterList = [0]*bulletsLimit   # reset the list

    for i in range(40):   
        magazine()
    # restart bullets ------

    # reset player ------
    destroy(player)
    player = duplicate(player0, x = -12) 
    # reset player ------

    # reset gears -------
    destroy(gear1)      
    destroy(gear2)
    destroy(gear3)
    gear1 = duplicate(gear0, x = gearLocation, y = 9.2)
    gear2 = duplicate(gear1, x = gearLocation + 1)
    gear3 = duplicate(gear1, x = gearLocation + 2)
    # reset gears -------



def input(key):       # user input from keyboard
    global gunSound, run, pause, info2, info3, check, bullets # using the veriables from outside this input function

    gunSound += random.randint(1, 2)   # to get a random number between 1, 2

    if key == 'r': # reset/reload the game
        reloadGame()

    if key == 'escape':
        quit()    

    if key == 'p':
        if pause and not check and gameOverCheck:   # to be able to pause the game only after starting it and befor the game over
            run = False
            pause = False
            info2 = Text('PAUSE\nPress P To Pause And Unpause\nPress R to Reload The Game', origin = (0,0))
            info2.background = True 
        elif not pause and not check and gameOverCheck:
            run = True
            pause = True  
            destroy(info2) 

    if key == 's':          # to only press s once 
        if check:
            run = True
            destroy(info3) # remove the starting message
            destroy(info5) # remove the name of the game from the scene
            destroy(startSquid) # remove the icon in the middle of the scene
            check = False  # do not go back to it is key s is pressed
            invoke(newMonster, delay = 1)   # spawn a squid
            propeller.volume = 1       # start the sound of the plane

    if run: 
        if key == 'space':
            if shooting:  # if the key space is pressed while the game is running and there are bullets in the magazine
                fire() # handle the shooting
                if len(bullets) >= bulletsLimit: # wait for reloding
                    invoke(fireReload, delay = 47 * time.dt)
                    
blood = Animation('assets/purpleBlood',
                    position = (1.5, -1.5),
                    color = color.black,
                    scale = 80) # using same texture for fadeout

invoke(Func(blood.fade_out, duration = 2)) # fadeout scene at the start

Audio('assets/backgourdMusic.mp3',
        volume = 0.2,
        loop = True)  # Audio for the background

propeller = Audio('assets/propellerPlane1.mp3',
                    volume = 0,
                    loop = True
                    ) # Audio for the plane at 0 volume to wiat when key s is pressed to start the audio

run = False      # run boolean veriable, to only run the game when true using the update function
pause = True # boolean for pausing the game
check = True # boolean to Start the game
spawningDelay = 2 # spped of monsters
checktime = 0 # chinking the empty monsters list
speed1, speed2, = 5, 8 # speed of monstere
colorPic = None # color of monsters
sizeing = 2 # size of sqid
gearLocation = -11.5 # posion x of gear
shooting = True # for the gun reload
bulletsLimit = 40 # number of bullets
bulitCounterX = 0
bulitCounterY = 8.3
lives = 3 # if 0 means game over
gameOverCheck = True # boolean to end the game and prevent the pause
gunSound = 0    # viriable for gun sound
splashSound = 0 # for the moster kill sound
bloodShape = 0   # for boold shapes 1 and 2
indexB = 0 # for bulits in array
indexcheck = 0 # for bullit array check
score = 0   
level = '\nLevel: 1'

window.borderless = False              # Show a border
window.exit_button.visible = False      # Do not show the in-game red X that loses the window
window.fps_counter.enabled = True       # Show the FPS (Frames per second) counter
window.size = (1550, 850)
window.center_on_screen()

player0 = Entity(
    texture = 'assets/plane',
    collider = 'box',
    model = 'cube',
    scale = 2.5,
    y = 0,           
    x = -32         
    )  # player

player = duplicate(
    player0,           
    x = -12         
    )  # start on the left position
    

bullet = Entity()       # bullets being shot from the plane
bulitCounter = Entity() # bullets under the gears to show the magazine

Sky()                   # sky box
camera.orthographic = True
camera.fov = 20

offset = 0      # backGround offset veriable

backGround = Entity(                 
    model = 'quad',
    texture = 'assets/Cartoon-Sky-Game',
    scale = (50, 21),         
    x = 5,
    z = 1
    )   # background, size of the backGround (x,y)

monster = Entity(      
    model = 'cube',
    texture = 'assets/cthulhu',
    collider = 'box',
    scale = 1.6,
    x = 20,
    y = -10
    )   # a monster positioned outside the sky box to the right side

wall1 = Entity(      
    model = 'cube',
    texture = 'white_cube',
    collider = 'box',
    color = color.red,
    scale = (3, 25),
    x = -23,
    y = 0
    )   # a wall positioned on the left

wall2 = duplicate(  
    wall1,     
    x = 32,
    y = 0
    )    # a wall positioned on the right

wall3 = duplicate(  
    wall1,      
    scale = (58, 2),
    x = 5,
    y = 15
    )   # a wall positioned on the top

wall4 = duplicate(
    wall3,      
    y = -15
    )    # a wall positioned on the bottom
           
monsters = []           # list of monsters
gears = []      # list of geart for the lives
bullets = []    # list of bullets on scene
bulitCounterList = [0]*bulletsLimit   # list of magazine

gear0 = Entity(      
    model = 'cube',
    texture = 'assets/gear',
    scale = 1,
    x = -30,
    y = 0
    )   # gear

gear1 = duplicate(
    gear0,     
    x = gearLocation,
    y = 9.2
    )   # gear 1 on the top

gear2 = duplicate(
    gear1,     
    x = gearLocation + 1
    )   # gear 2 on the top

gear3 = duplicate(
    gear1,      
    x = gearLocation + 2
    )   # gear 3 on the top

startSquid = Entity(      
    model = 'cube',
    texture = 'assets/squidp',
    scale = 7,
    x = 0,
    y = 1,
    background = color.red
    )   # game icon when game starts


for i in range(40):  # to show the bullets in the magazine for the first time when the game is launched
    magazine() 

def newMonster():       # generating new mosters
    global run, spawningDelay

    # spawning more squids on the scene
    squid = duplicate(   
        monster,
        color = colorPic,
        scale = sizeing,
        y = random.randint(-6, 6)       
    )   # to get a random y postion for the new monster

    monsters.append(squid)                 # add to the monsters array   

    if run: # to pause spawning monsters
        invoke(newMonster, delay = spawningDelay)     
                   
def spawnAgain():
    if not monsters:  # spawn new squid if there is non on the scene
        newMonster()

Text.size = 0.05    
Text.default_resolution = 1080 * Text.size
info = Text('Score: ' + str(score) + '   '+ level)        # desplayed text 
info.x = -0.88      # position of text
info.y = 0.47
info.background = True  
info.visible = True        # Do not show this text

info3 = Text('Press S To Start The Game\nPress P To Pause And Unpause\nPress R To Reload The Game', origin = (0,2))
info3.background = True



info5 = Text('The Squid War', origin = (0,-7))
info5.background = True

info2 = Text()   #without it reset won't work, this is quick fix for it
info4 = Text()
destroy(info2)
destroy(info4)


app.run() # starting the game