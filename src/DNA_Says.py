## @mainpage Main
# @file DNA_Says.py
# @author Kareem Abdel Mesih
# @author John-Paul Dakran
# @author Shady Nessim
# @date 3/11/2016
# @brief This program is a modified remake of the famous Simon Says.
# @details This program is based upon the fundementals of the original game,
# however, it is modified to an extent to preserve originality.

import random, sys, time, pygame
from pygame.locals import *
## Holds the number of frames per second to be rendered
fps = 30

## Holds the width of the window
winWidth = 640

## Holds the height of the window
winHeight = 480

## Holds the number of seconds in which the game will timeout after
timeout  = 4

## Holds the number of milliseconds in which the program will delay its output by throughout the course of its execution
delay = 200

## Holds the RGB values of the color white
white        = (255, 255, 255)

## Holds the RGB values of the color black
black        = (  0,   0,   0)

## Holds the RGB values of the color grey
grey         = ( 40,  40,  40)

## Holds the RGB values of the color red
red          = (155,   0,   0)

## Holds the RGB values of the color orange
orange       = (255, 127,   0)

## Holds the RGB values of the color yellow
yellow       = (155, 155,   0)

## Holds the RGB values of the color green
green        = (  0, 155,   0)

## Holds the RGB values of the color blue
blue         = (  0,   0, 155)

## Holds the RGB values of the color indigo
indigo       = ( 75,   0, 130)

## Holds the RGB values of the color violet
violet       = (148,   0, 211)

## Holds the RGB values of the color bright red
brightRed    = (255,   0,   0)

## Holds the RGB values of the color bright orange
brightOrange = (255, 215,   0)

## Holds the RGB values of the color bright yellow
brightYellow = (255, 255,   0)

## Holds the RGB values of the color bright green
brightGreen  = (  0, 255,   0)

## Holds the RGB values of the color bright blue
brightBlue   = (  0,   0, 255)

## Holds the RGB values of the color bright indigo
brightIndigo = (138,  43, 226)

## Holds the RGB values of the color bright violet
brightViolet = (218, 112, 214)

## Holds the default/initial color of the background
bgColor      = grey


## @brief Initially called to set up the essential elements to run the program
#  @details Initializes Pygame along with Pygame's clock, all required font sizes,
#  the required sounds, and the main menu button in its set position.
#  It globalizes all those variables in order for other functions to utilize them as desired.
#  This function then proceeds to call the main menu function.
def main():
    global fpsClock, titleFont, modeFont, medFont, font, goBack, B3, C4, D4, E4, F4, Ab4, A4, B4, C5

    pygame.init()
    fpsClock  = pygame.time.Clock()
    titleFont = pygame.font.Font('freesansbold.ttf', 60)
    modeFont  = pygame.font.Font('freesansbold.ttf', 50)
    medFont   = pygame.font.Font('freesansbold.ttf', 32)
    font      = pygame.font.Font('freesansbold.ttf', 16)

    B3  = pygame.mixer.Sound('B3.ogg')
    C4  = pygame.mixer.Sound('C4.ogg')
    D4  = pygame.mixer.Sound('D4.ogg')
    E4  = pygame.mixer.Sound('E4.ogg')
    F4  = pygame.mixer.Sound('F4.ogg')
    Ab4 = pygame.mixer.Sound('Ab4.ogg')
    A4  = pygame.mixer.Sound('A4.ogg')
    B4  = pygame.mixer.Sound('B4.ogg')
    C5  = pygame.mixer.Sound('C5.ogg')

    goBack = pygame.Rect(20, 15, 55, 38)
    menu()


## @brief Sets up the displaying surface
#  @details Creates a window of a set width and height, and labels it.
#  All graphics can then be displayed on that window.
#  This function then globalizes that displaying surface in order for other functions to utilize it.
def setup():
    global screen
    
    screen = pygame.display.set_mode((winWidth, winHeight))
    screen.fill(grey)
    pygame.display.set_caption('DNA Says')


## @brief Updates the display
#  @details Using functions built in Pygame, the display gets updated whenever
#  this function is called.
def update():
    pygame.display.update()
    fpsClock.tick(fps)


## @brief Displays the instructions
#  @details Initializes the text box to hold the instructions text, 
#  giving it a set position. It then displays it on the screen.
#  @param instText The variable holding the instructions text.
def showInst(instText):
    instBox  = instText.get_rect()
    instBox.topleft = (10, winHeight - 25)
    screen.blit(instText, instBox)


## @brief Displays the main menu button text
#  @details Initializes the variable to hold the text, it then
#  initializes the text box to hold that text, giving it a set position.
#  It then displays it on the screen.
def showGoBack():
    goBackText = titleFont.render('<-', 1, white)
    goBackBox  = goBackText.get_rect()
    goBackBox.topleft = (20, 0)
    screen.blit(goBackText, goBackBox)


## @brief Displays the score
#  @details Initializes the variable to hold the text, it then
#  initializes the text box to hold that text, giving it a set position.
#  It then displays it on the screen.
#  @param score The variable holding the player's score.
def showScore(score):
    scoreText = font.render('Score: ' + str(score), 1, white)
    scoreBox = scoreText.get_rect()
    scoreBox.topleft = (570, 15)
    screen.blit(scoreText, scoreBox)


## @brief Displays the main menu
#  @details Calls setup() to create an empty window to use. It creates the buttons
#  giving them their sizes and positions. It then displays them on the screen, giving
#  them their colors. Then, it prepares the instructions text and calls showInst(instText)
#  to display it. In the same fashion, it prepares the main title along with the button
#  titles and displays them. Finally, it checks for user input to determine which function
#  to call to start the game. This depends on which button the user presses on.
#  It globalizes the variable that holds the mode in order for other functions to utilize it.
def menu():
    global mode

    setup()
    
    mRed    = pygame.Rect(110, 30,  200, 200)
    mGreen  = pygame.Rect(110, 250, 200, 200)
    mBlue   = pygame.Rect(330, 250, 200, 200)

    pygame.draw.rect(screen, red,    mRed)
    pygame.draw.rect(screen, green,  mGreen)
    pygame.draw.rect(screen, blue,   mBlue)

    instText = font.render('Pick a mode.', 1, white)
    showInst(instText)

    dnaText  = titleFont.render('DNA', 1, brightYellow)
    dnaBox   = dnaText.get_rect()
    dnaBox.topleft = (365, 75)
    screen.blit(dnaText, dnaBox)

    saysText = titleFont.render('SAYS', 1, brightYellow)
    saysBox  = saysText.get_rect()
    saysBox.topleft = (350, 135)
    screen.blit(saysText, saysBox)

    kareemText  = modeFont.render('Kareem', 1, white)
    kareemBox   = kareemText.get_rect()
    kareemBox.topleft = (115, 82)
    screen.blit(kareemText, kareemBox)

    saysText = modeFont.render('Says', 1, white)
    saysBox  = saysText.get_rect()
    saysBox.topleft = (150, 128)
    screen.blit(saysText, saysBox)

    jpText  = modeFont.render('JP', 1, white)
    jpBox   = jpText.get_rect()
    jpBox.topleft = (183, 307)
    screen.blit(jpText, jpBox)

    saysBox.topleft = (150, 353)
    screen.blit(saysText, saysBox)

    shadyText  = modeFont.render('Shady', 1, white)
    shadyBox   = shadyText.get_rect()
    shadyBox.topleft = (352, 307)
    screen.blit(shadyText, shadyBox)

    saysBox.topleft = (370, 353)
    screen.blit(saysText, saysBox)

    modeChosen = False
    while modeChosen == False:
        update()
        checkForQuit()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                if   mRed.collidepoint   (event.pos):
                    modeChosen = True
                    mode = "kareem"
                    kareem()
                elif mGreen.collidepoint (event.pos):
                    modeChosen = True
                    mode = "jp"
                    jp()
                elif mBlue.collidepoint  (event.pos):
                    modeChosen = True
                    mode = "shady"
                    shady()
                

## @brief Starts the mode Kareem Says
#  @details Calls setup() to create an empty window to use. It creates the keys
#  giving them their sizes and positions. It then displays them on the screen, giving
#  them their colors. Then, it prepares the song pattern and initializes all required variables.
#  It prepares the instructions text and calls showInst(instText)
#  to display it. In the same fashion, it prepares the title and displays it. It checks for quit
#  requests using checkForQuit(), displays the main menu button using showGoBack(), and displays
#  the score using showScore(score). It plays the elements that are contained in the pattern,
#  then checks for the user's input by detecting where the user clicks. If the user clicked the
#  correct button then that note is played and its key is highlighted temporarily, and the score is incremented. In the meantime,
#  the program appends the next note from the song to the pattern to be played, and the pattern is
#  played, and the cycle goes on. However, if the user clicks on the wrong key, the game will be over.
#  The game will also end if the user clicks on one correct key, and waits for more than four seconds,
#  assuming that there is more than one element in the last pattern played.
#  If the user clicks on the main menu button, the program will redirect them to the main menu.
#  All throughout, various methods are called and used to operate this mode accordingly.
#  Along with those methods, are various variables that aid in the organization and the execution
#  of this mode. It globalizes all variables in order for other functions to utilize it.
def kareem():
    global whiteWidth, blackWidth, goBack, keyA3, keyBb3, keyB3, keyC4, keyDb4, keyD4, keyEb4, keyE4, keyF4, keyGb4, keyG4, keyAb4, keyA4, keyBb4, keyB4, keyC5, keyDb5, keyD5
    setup()    
    
    whiteWidth   = 50
    whiteHeight  = 150
    blackWidth   = 35
    blackHeight  = 90
    xMargin      = 20
    yMargin      = 170
    gap          = 3

    #Create white keys   X coord.                                Y coord.    Width       Height
    keyA3  = pygame.Rect(1    * whiteWidth + 0  * gap - xMargin, yMargin, whiteWidth, whiteHeight)
    keyB3  = pygame.Rect(2    * whiteWidth + 1  * gap - xMargin, yMargin, whiteWidth, whiteHeight)
    keyC4  = pygame.Rect(3    * whiteWidth + 2  * gap - xMargin, yMargin, whiteWidth, whiteHeight)
    keyD4  = pygame.Rect(4    * whiteWidth + 3  * gap - xMargin, yMargin, whiteWidth, whiteHeight)
    keyE4  = pygame.Rect(5    * whiteWidth + 4  * gap - xMargin, yMargin, whiteWidth, whiteHeight)
    keyF4  = pygame.Rect(6    * whiteWidth + 5  * gap - xMargin, yMargin, whiteWidth, whiteHeight)
    keyG4  = pygame.Rect(7    * whiteWidth + 6  * gap - xMargin, yMargin, whiteWidth, whiteHeight)
    keyA4  = pygame.Rect(8    * whiteWidth + 7  * gap - xMargin, yMargin, whiteWidth, whiteHeight)
    keyB4  = pygame.Rect(9    * whiteWidth + 8  * gap - xMargin, yMargin, whiteWidth, whiteHeight)
    keyC5  = pygame.Rect(10   * whiteWidth + 9  * gap - xMargin, yMargin, whiteWidth, whiteHeight)
    keyD5  = pygame.Rect(11   * whiteWidth + 10 * gap - xMargin, yMargin, whiteWidth, whiteHeight)

    #Create black keys
    keyBb3 = pygame.Rect(1.5  * whiteWidth + 3  * gap - xMargin, yMargin, blackWidth, blackHeight)
    keyDb4 = pygame.Rect(3.5  * whiteWidth + 5  * gap - xMargin, yMargin, blackWidth, blackHeight)
    keyEb4 = pygame.Rect(4.5  * whiteWidth + 6  * gap - xMargin, yMargin, blackWidth, blackHeight)
    keyGb4 = pygame.Rect(6.5  * whiteWidth + 8  * gap - xMargin, yMargin, blackWidth, blackHeight)
    keyAb4 = pygame.Rect(7.5  * whiteWidth + 9  * gap - xMargin, yMargin, blackWidth, blackHeight)
    keyBb4 = pygame.Rect(8.5  * whiteWidth + 10 * gap - xMargin, yMargin, blackWidth, blackHeight)
    keyDb5 = pygame.Rect(10.5 * whiteWidth + 12 * gap - xMargin, yMargin, blackWidth, blackHeight)

    #Initializing variables required for a new game
    song = [keyC5, keyE4, keyE4, keyC5, keyC5, keyE4, keyE4, keyC5, keyC5, keyE4, keyF4, keyE4,
            keyD4, keyD4, keyD4, keyB4, keyB4, keyD4, keyD4, keyB4, keyB4, keyD4, keyE4, keyD4,
            keyC4, keyC4, keyC4, keyA4, keyA4, keyC4, keyC4, keyA4, keyA4, keyC4, keyD4, keyC4,
            keyB3, keyB3, keyB3, keyAb4, keyAb4, keyA4, keyB4, keyF4]
    
    noteIndex       = 0     #indexes the notes in the song array   
    pattern         = []    #holds the pattern to be checked
    currentStep     = 0     #the next note to be repeated
    lastClickTime   = 0     #timestamp of the player's last button push
    score           = 0     #stores the score
    waitingForInput = False #when false, the pattern is playing

    while True:
        clickedKey = None
        screen.fill(bgColor)
        drawKeys()

        instText = font.render('Match the pattern to learn a nice song.', 1, white)
        showInst(instText)

        titleText = titleFont.render('Kareem Says', 1, red)
        titleBox  = titleText.get_rect()
        titleBox.topleft = (130, 60)
        screen.blit(titleText, titleBox)

        showGoBack()
        showScore(score)
        checkForQuit()
        
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                if goBack.collidepoint   (event.pos): clickedKey = goBack
                elif keyB3.collidepoint  (event.pos): clickedKey = keyB3
                elif keyC4.collidepoint  (event.pos): clickedKey = keyC4
                elif keyD4.collidepoint  (event.pos): clickedKey = keyD4
                elif keyE4.collidepoint  (event.pos): clickedKey = keyE4
                elif keyF4.collidepoint  (event.pos): clickedKey = keyF4
                elif keyAb4.collidepoint (event.pos): clickedKey = keyAb4
                elif keyA4.collidepoint  (event.pos): clickedKey = keyA4
                elif keyB4.collidepoint  (event.pos): clickedKey = keyB4
                elif keyC5.collidepoint  (event.pos): clickedKey = keyC5
                else:                                clickedKey = keyDb5

        if not waitingForInput:
            #play the next note
            pygame.display.update()
            pygame.time.wait(1000)
            pattern.append(song[noteIndex])
            if noteIndex < 44: noteIndex += 1
            else: noteIndex = 0

            for key in pattern:
                flashKeyAnimation(key)
                pygame.time.wait(delay)
            waitingForInput = True
            
        else:
            #wait for the player input
            if   clickedKey and clickedKey == goBack: menu()
            elif clickedKey and clickedKey == pattern[currentStep]:
                #played the correct note
                flashKeyAnimation(clickedKey)
                currentStep  += 1
                lastClickTime = time.time()

                if currentStep == len(pattern):
                    #played the last note
                    changeBackgroundAnimation()
                    score += 1
                    waitingForInput = False
                    currentStep     = 0

            elif (clickedKey and clickedKey != pattern[currentStep]) or (currentStep != 0 and time.time() - timeout > lastClickTime):
                #played incorrect note or timed out
                gameOverAnimation()
                pattern         = []
                currentStep     = 0
                score           = 0
                waitingForInput = False
                noteIndex = 0
                pygame.time.wait(1000)
                changeBackgroundAnimation()
        update()


## @brief Starts the mode JP Says
#  @details Calls setup() to create an empty window to use. It creates the keys
#  giving them their sizes and positions. It then displays them on the screen, giving
#  them their colors. Then, it prepares the song pattern and initializes all required variables.
#  It prepares the instructions text and calls showInst(instText)
#  to display it. In the same fashion, it prepares the title and displays it. It checks for quit
#  requests using checkForQuit(), displays the main menu button using showGoBack(), and displays
#  the score using showScore(score). It plays the elements that are contained in the pattern,
#  then checks for the user's input by detecting where the user clicks. If the user clicked the
#  correct button then its sound is played and its key is highlighted temporarily, and the score is incremented. In the meantime,
#  the program appends a random element to the pattern to be played, and the pattern is
#  played, and the cycle goes on. However, if the user clicks on the wrong key, the game will be over.
#  The game will also end if the user clicks on one correct key, and waits for more than four seconds,
#  assuming that there is more than one element in the last pattern played.
#  If the user clicks on the main menu button, the program will redirect them to the main menu.
#  All throughout, various methods are called and used to operate this mode accordingly.
#  Along with those methods, are various variables that aid in the organization and the execution
#  of this mode. It globalizes all variables in order for other functions to utilize it.
def jp():
    global goBack, jWhite, jRed, jOrange, jYellow, jGreen, jBlue, jIndigo, jViolet, jBlack
    setup()
    
                          #X coord.      Y coord.      Wid  Hei
    jWhite  = pygame.Rect(150 + 0 * 120, 70 + 0 * 120, 100, 100)
    jRed    = pygame.Rect(150 + 1 * 120, 70 + 0 * 120, 100, 100)
    jOrange = pygame.Rect(150 + 2 * 120, 70 + 0 * 120, 100, 100)
    jYellow = pygame.Rect(150 + 0 * 120, 70 + 1 * 120, 100, 100)
    jGreen  = pygame.Rect(150 + 1 * 120, 70 + 1 * 120, 100, 100)
    jBlue   = pygame.Rect(150 + 2 * 120, 70 + 1 * 120, 100, 100)
    jIndigo = pygame.Rect(150 + 0 * 120, 70 + 2 * 120, 100, 100)
    jViolet = pygame.Rect(150 + 1 * 120, 70 + 2 * 120, 100, 100)
    jBlack  = pygame.Rect(150 + 2 * 120, 70 + 2 * 120, 100, 100)

 

    #Initializing variables required for a new game
    pattern         = []
    currentStep     = 0     #the next note to be repeated
    lastClickTime   = 0     #timestamp of the player's last button push
    score           = 0     #stores the score
    waitingForInput = False #when false, the pattern is playing

    #Main loop
    while True:
        clickedKey = None
        screen.fill(bgColor)
        drawKeys()

        instText = font.render('Match the pattern.', 1, white)
        showInst(instText)

        jpText = titleFont.render('JP', 1, green)
        jpBox  = jpText.get_rect()
        jpBox.topleft = (42, 190)
        screen.blit(jpText, jpBox)

        saysText = titleFont.render('Says', 1, green)
        saysBox  = saysText.get_rect()
        saysBox.topleft = (2, 235)
        screen.blit(saysText, saysBox)

        showGoBack()
        showScore(score)
        checkForQuit()
        
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                if   goBack.collidepoint  (event.pos): clickedKey = goBack
                elif jWhite.collidepoint  (event.pos): clickedKey = jWhite
                elif jRed.collidepoint    (event.pos): clickedKey = jRed
                elif jOrange.collidepoint (event.pos): clickedKey = jOrange
                elif jYellow.collidepoint (event.pos): clickedKey = jYellow
                elif jGreen.collidepoint  (event.pos): clickedKey = jGreen
                elif jBlue.collidepoint   (event.pos): clickedKey = jBlue
                elif jIndigo.collidepoint (event.pos): clickedKey = jIndigo
                elif jViolet.collidepoint (event.pos): clickedKey = jViolet
                elif jBlack.collidepoint  (event.pos): clickedKey = jBlack

        if not waitingForInput:
            #play the next note
            pygame.display.update()
            pygame.time.wait(1000)
            pattern.append(random.choice((jWhite,  jRed,    jOrange, jYellow, jGreen,  jBlue, jIndigo, jViolet, jBlack)))

            for key in pattern:
                flashKeyAnimation(key)
                pygame.time.wait(delay)
            waitingForInput = True
            
        else:
            #wait for the player input
            if   clickedKey and clickedKey == goBack: menu()
            elif clickedKey and clickedKey == pattern[currentStep]:
                #played the correct note
                flashKeyAnimation(clickedKey)
                currentStep  += 1
                lastClickTime = time.time()

                if currentStep == len(pattern):
                    #played the last note
                    changeBackgroundAnimation()
                    score += 1
                    waitingForInput = False
                    currentStep     = 0

            elif (clickedKey and clickedKey != pattern[currentStep]) or (currentStep != 0 and time.time() - timeout > lastClickTime):
                #played incorrect note or timed out
                gameOverAnimation()
                pattern         = []
                currentStep     = 0
                score           = 0
                waitingForInput = False
                pygame.time.wait(1000)
                changeBackgroundAnimation()
        update()


## @brief Starts the mode Shady Says
#  @details Calls setup() to create an empty window to use. It creates the keys
#  giving them their sizes and positions. It then displays them on the screen, giving
#  them their colors. Then, it prepares the song pattern and initializes all required variables.
#  It prepares the instructions text and calls showInst(instText)
#  to display it. In the same fashion, it prepares the title and displays it. It checks for quit
#  requests using checkForQuit(), displays the main menu button using showGoBack(), and displays
#  the score using showScore(score). It plays the elements that are contained in the pattern,
#  then checks for the user's input by detecting where the user clicks. If the user clicked the
#  correct button then a random note is played and its key is highlighted temporarily, and the score is incremented. In the meantime,
#  the program appends a random element to the pattern to be played, and the pattern is
#  played, and the cycle goes on. However, if the user clicks on the wrong key, the game will be over.
#  The game will also end if the user clicks on one correct key, and waits for more than four seconds,
#  assuming that there is more than one element in the last pattern played.
#  If the user clicks on the main menu button, the program will redirect them to the main menu.
#  All throughout, various methods are called and used to operate this mode accordingly.
#  Along with those methods, are various variables that aid in the organization and the execution
#  of this mode. It globalizes all variables in order for other functions to utilize it.
def shady():
    global goBack, sRed, sYellow, sGreen, sBlue
    setup()
    
                          #x   y    wid  hei
    sRed    = pygame.Rect(110, 30,  200, 200)
    sYellow = pygame.Rect(330, 30,  200, 200)
    sGreen  = pygame.Rect(110, 250, 200, 200)
    sBlue   = pygame.Rect(330, 250, 200, 200)


    #Initializing variables required for a new game
    pattern         = []
    currentStep     = 0     #the next note to be repeated
    lastClickTime   = 0     #timestamp of the player's last button push
    score           = 0     #stores the score
    waitingForInput = False #when false, the pattern is playing

    #Main loop
    while True:
        clickedKey = None
        screen.fill(bgColor)
        drawKeys()

        instText = font.render('Match the pattern.', 1, white)
        showInst(instText)

        shadyText = medFont.render('Shady', 1, blue)
        shadyBox  = shadyText.get_rect()
        shadyBox.topleft = (2, 203)
        screen.blit(shadyText, shadyBox)

        saysText = medFont.render('Says', 1, blue)
        saysBox  = saysText.get_rect()
        saysBox.topleft = (12, 233)
        screen.blit(saysText, saysBox)

        showGoBack()
        showScore(score)
        checkForQuit()
        
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                if   goBack.collidepoint  (event.pos): clickedKey = goBack
                elif sRed.collidepoint    (event.pos): clickedKey = sRed
                elif sYellow.collidepoint (event.pos): clickedKey = sYellow
                elif sGreen.collidepoint  (event.pos): clickedKey = sGreen
                elif sBlue.collidepoint   (event.pos): clickedKey = sBlue

        if not waitingForInput:
            #play the next note
            pygame.display.update()
            pygame.time.wait(1000)
            pattern.append(random.choice((sRed, sYellow, sGreen,  sBlue)))

            for key in pattern:
                flashKeyAnimation(key)
                pygame.time.wait(delay)
            waitingForInput = True
            
        else:
            #wait for the player input
            if clickedKey and clickedKey == goBack:
                menu()
            
            elif clickedKey and clickedKey == pattern[currentStep]:
                #played the correct note
                flashKeyAnimation(clickedKey)
                currentStep  += 1
                lastClickTime = time.time()

                if currentStep == len(pattern):
                    #played the last note
                    changeBackgroundAnimation()
                    score += 1
                    waitingForInput = False
                    currentStep     = 0

            elif (clickedKey and clickedKey != pattern[currentStep]) or (currentStep != 0 and time.time() - timeout > lastClickTime):
                #played incorrect note or timed out
                gameOverAnimation()
                pattern         = []
                currentStep     = 0
                score           = 0
                waitingForInput = False
                pygame.time.wait(1000)
                changeBackgroundAnimation()
        update()
    

## @brief Plays the appropriate sound and flashes the correct key
#  @details Depending on which mode is active, this function loads the correct
#  sound to play to a variable, and also the correct highlight to another variable.
#  For Kareem Says, it loads the correct note, and since all highlights in this mode
#  are bright red, it is set by default. The color of the key (white or black) is accomodated
#  by if statements to assure that the correct spot will light up. For JP Says, it again loads
#  the correct note and also the correct highlight depending on the color of the button that is passed.
#  For Shady Says, the sound is randomized every time and is stored in that sound
#  variable. The different button sizes are also accomodated in this function.
#  Finally, this function fades in and out of the highlight smoothly.
#  @param key The button that is pressed by either the computer or the user.
#  @param animationSpeed The speed at which that animation is played at.
def flashKeyAnimation(key, animationSpeed=50):
    if mode == "kareem":
        if   key == keyB3:  sound = B3 
        elif key == keyC4:  sound = C4
        elif key == keyD4:  sound = D4
        elif key == keyE4:  sound = E4
        elif key == keyF4:  sound = F4
        elif key == keyAb4: sound = Ab4
        elif key == keyA4:  sound = A4
        elif key == keyB4:  sound = B4
        else:               sound = C5
        highlight = brightRed

    elif mode == "jp":
        if   key == jWhite:
            sound     = B3
            highlight = black
        elif key == jRed:
            sound     = C4
            highlight = brightRed
        elif key == jOrange:
            sound     = D4
            highlight = brightOrange
        elif key == jYellow:
            sound     = E4
            highlight = brightYellow
        elif key == jGreen:
            sound     = F4
            highlight = brightGreen
        elif key == jBlue:
            sound     = Ab4
            highlight = brightBlue
        elif key == jIndigo:
            sound     = A4
            highlight = brightIndigo
        elif key == jViolet:
            sound     = B4
            highlight = brightViolet
        elif key == jBlack:
            sound     = C5
            highlight = white

    elif mode == "shady":
        if   key == sRed:
            highlight = brightRed
        elif key == sYellow:
            highlight = brightYellow
        elif key == sGreen:
            highlight = brightGreen
        elif key == sBlue:
            highlight = brightBlue
        sound = random.choice((C4, E4, A4, C5))

    r, g, b   = highlight
    origSurf   = screen.copy()
    if   mode == "kareem" and key != keyAb4: flashSurf = pygame.Surface((whiteWidth, 60))
    elif mode == "kareem" and key == keyAb4: flashSurf = pygame.Surface((blackWidth, 36))
    elif mode == "jp":                       flashSurf = pygame.Surface((100, 100))
    elif mode == "shady":                    flashSurf = pygame.Surface((200, 200))
    
    flashSurf = flashSurf.convert_alpha()
    sound.play()
    
    for start, end, step in ((0, 255, 1), (255, 0, -1)):
        for alpha in range(start, end, animationSpeed * step):
            checkForQuit()
            screen.blit(origSurf, (0, 0))
            flashSurf.fill((r, g, b, alpha))
            if   mode == "kareem" and key != keyAb4: screen.blit(flashSurf, (key.x, key.y+90))
            elif mode == "kareem" and key == keyAb4: screen.blit(flashSurf, (key.x, key.y+54))
            else:                                    screen.blit(flashSurf, key.topleft)
            update()
    screen.blit(origSurf, (0, 0))


## @brief Draws the buttons on the screen
#  @details Depending on which mode is active, this function either draws
#  the piano keys for Kareem Says, nine buttons for JP says, or four buttons
#  for Shady Says. It also draws the main menu button in all modes.
def drawKeys():
    if mode == "kareem":
        pygame.draw.rect(screen, white,  keyA3)
        pygame.draw.rect(screen, white,  keyB3)
        pygame.draw.rect(screen, white,  keyC4)
        pygame.draw.rect(screen, white,  keyD4)
        pygame.draw.rect(screen, white,  keyE4)
        pygame.draw.rect(screen, white,  keyF4)
        pygame.draw.rect(screen, white,  keyG4)
        pygame.draw.rect(screen, white,  keyA4)
        pygame.draw.rect(screen, white,  keyB4)
        pygame.draw.rect(screen, white,  keyC5)
        pygame.draw.rect(screen, white,  keyD5)
        pygame.draw.rect(screen, black,  keyBb3)
        pygame.draw.rect(screen, black,  keyDb4)
        pygame.draw.rect(screen, black,  keyEb4)
        pygame.draw.rect(screen, black,  keyGb4)
        pygame.draw.rect(screen, black,  keyAb4)
        pygame.draw.rect(screen, black,  keyBb4)
        pygame.draw.rect(screen, black,  keyDb5)

    elif mode == "jp":
        pygame.draw.rect(screen, white,  jWhite)
        pygame.draw.rect(screen, red,    jRed)
        pygame.draw.rect(screen, orange, jOrange)
        pygame.draw.rect(screen, yellow, jYellow)
        pygame.draw.rect(screen, green,  jGreen)
        pygame.draw.rect(screen, blue,   jBlue)
        pygame.draw.rect(screen, indigo, jIndigo)
        pygame.draw.rect(screen, violet, jViolet)
        pygame.draw.rect(screen, black,  jBlack)

    elif mode == "shady":
        pygame.draw.rect(screen, red,    sRed)
        pygame.draw.rect(screen, yellow, sYellow)
        pygame.draw.rect(screen, green,  sGreen)
        pygame.draw.rect(screen, blue,   sBlue)
        
    pygame.draw.rect(screen, grey,  goBack)


## @brief Changes the background color smoothly
#  @details It generates appropriate random RGB values that will be translated
#  into the new background color. It creates a temporary displaying surface,
#  that will be used to smoothly fade from the old color to the new one on the
#  original displaying surface. This is accomplished using a for loop, and then
#  redrawing the buttons on top of that new tint using drawKeys(), then updating
#  the display using update(). Lastly, this function globalizes the variable holding
#  the new background color in order for other functions to untilize it.
#  @param animationSpeed The speed at which that animation is played at.
def changeBackgroundAnimation(animationSpeed=40):
    global bgColor
    newBgColor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    newBgSurf = pygame.Surface((winWidth, winHeight))
    newBgSurf = newBgSurf.convert_alpha()
    r, g, b = newBgColor
    
    for alpha in range(0, 255, animationSpeed):
        checkForQuit()
        screen.fill(bgColor)
        newBgSurf.fill((r, g, b, alpha))
        screen.blit(newBgSurf, (0, 0))
        drawKeys()
        update()
    bgColor = newBgColor


## @brief Plays the animation associated with incorrect user input
#  @details It plays a C chord while flashing the screen three times
#  to indicate that the game is over.
#  @param color The color of the flash.
#  @param animationSpeed The speed at which that animation is played at.
def gameOverAnimation(color=white, animationSpeed=50):
    origSurf  = screen.copy()
    flashSurf = pygame.Surface(screen.get_size())
    flashSurf = flashSurf.convert_alpha()
    pattern   = []
    C4.play()
    E4.play()
    A4.play()
    C5.play()
    r, g, b   = color

    for i in range(3):
        for start, end, step in ((0, 255, 1), (255, 0, -1)):
            for alpha in range(start, end, animationSpeed * step):
                checkForQuit()
                flashSurf.fill((r, g, b, alpha))
                screen.blit(origSurf,  (0, 0))
                screen.blit(flashSurf, (0, 0))
                drawKeys()
                update()


## @brief Checks for quit requests
#  @details Quits the program at anytime upon the user's request.
def checkForQuit():
    for event in pygame.event.get(QUIT):
        pygame.quit()
        sys.exit()

if __name__ == '__main__': main()
