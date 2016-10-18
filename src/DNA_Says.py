#Team Number  : 10
#Team Name    : DNA
#Team Members : Kareem Abdel Mesih (abdelk2), John-Paul Dakran (dakranj), Shady Nessim (nessimss)
#This project is a reimplementation of the famous game "Simon Says"

import random, sys, time, pygame
from pygame.locals import *


#Global variables
fps          = 30
winWidth     = 680
winHeight    = 250
whiteWidth   = 50
whiteHeight  = 150
blackWidth   = 35
blackHeight  = 90
gap          = 3
timeout      = 4   #seconds
delay        = 200 #milliseconds

#Colors         R    G    B
brightRed    = (255,   0,   0)
white        = (255, 255, 255)
black        = (  0,   0,   0)
grey         = ( 40,  40,  40)
bgColor      = grey #starting background color

#Create white keys   X coord.                      Y coord.    Width       Height
keyA3  = pygame.Rect(1    * whiteWidth,            whiteWidth, whiteWidth, whiteHeight)
keyB3  = pygame.Rect(2    * whiteWidth + gap,      whiteWidth, whiteWidth, whiteHeight)
keyC4  = pygame.Rect(3    * whiteWidth + 2 * gap,  whiteWidth, whiteWidth, whiteHeight)
keyD4  = pygame.Rect(4    * whiteWidth + 3 * gap,  whiteWidth, whiteWidth, whiteHeight)
keyE4  = pygame.Rect(5    * whiteWidth + 4 * gap,  whiteWidth, whiteWidth, whiteHeight)
keyF4  = pygame.Rect(6    * whiteWidth + 5 * gap,  whiteWidth, whiteWidth, whiteHeight)
keyG4  = pygame.Rect(7    * whiteWidth + 6 * gap,  whiteWidth, whiteWidth, whiteHeight)
keyA4  = pygame.Rect(8    * whiteWidth + 7 * gap,  whiteWidth, whiteWidth, whiteHeight)
keyB4  = pygame.Rect(9    * whiteWidth + 8 * gap,  whiteWidth, whiteWidth, whiteHeight)
keyC5  = pygame.Rect(10   * whiteWidth + 9 * gap,  whiteWidth, whiteWidth, whiteHeight)
keyD5  = pygame.Rect(11   * whiteWidth + 10 * gap, whiteWidth, whiteWidth, whiteHeight)

#Create black keys
keyBb3 = pygame.Rect(1.5  * whiteWidth + 3 * gap,  whiteWidth, blackWidth, blackHeight)
keyDb4 = pygame.Rect(3.5  * whiteWidth + 5 * gap,  whiteWidth, blackWidth, blackHeight)
keyEb4 = pygame.Rect(4.5  * whiteWidth + 6 * gap,  whiteWidth, blackWidth, blackHeight)
keyGb4 = pygame.Rect(6.5  * whiteWidth + 8 * gap,  whiteWidth, blackWidth, blackHeight)
keyAb4 = pygame.Rect(7.5  * whiteWidth + 9 * gap,  whiteWidth, blackWidth, blackHeight)
keyBb4 = pygame.Rect(8.5  * whiteWidth + 10 * gap, whiteWidth, blackWidth, blackHeight)
keyDb5 = pygame.Rect(10.5 * whiteWidth + 12 * gap, whiteWidth, blackWidth, blackHeight)

def main():
    global fpsClock, displaySurf, font, A3, Bb3, B3, C4, Db4, D4, Eb4, E4, F4, Gb4, G4, Ab4, A4, Bb4, B4, C5, Db5, D5

    #Initializing the game
    pygame.init()
    fpsClock    = pygame.time.Clock()
    displaySurf = pygame.display.set_mode((winWidth, winHeight))
    pygame.display.set_caption('DNA Says')

    font     = pygame.font.Font('freesansbold.ttf', 16)
    infoSurf = font.render('Match the pattern to learn a nice song.', 1, white)
    infoRect = infoSurf.get_rect()
    infoRect.topleft = (50, 220)

    #Store piano notes
    A3  = pygame.mixer.Sound('A3.ogg')
    Bb3 = pygame.mixer.Sound('Bb3.ogg')
    B3  = pygame.mixer.Sound('B3.ogg')
    C4  = pygame.mixer.Sound('C4.ogg')
    Db4 = pygame.mixer.Sound('Db4.ogg')
    D4  = pygame.mixer.Sound('D4.ogg')
    Eb4 = pygame.mixer.Sound('Eb4.ogg')
    E4  = pygame.mixer.Sound('E4.ogg')
    F4  = pygame.mixer.Sound('F4.ogg')
    Gb4 = pygame.mixer.Sound('Gb4.ogg')
    G4  = pygame.mixer.Sound('G4.ogg')
    Ab4 = pygame.mixer.Sound('Ab4.ogg')
    A4  = pygame.mixer.Sound('A4.ogg')
    Bb4 = pygame.mixer.Sound('Bb4.ogg')
    B4  = pygame.mixer.Sound('B4.ogg')
    C5  = pygame.mixer.Sound('C5.ogg')
    Db5 = pygame.mixer.Sound('Db5.ogg')
    D5  = pygame.mixer.Sound('D5.ogg')

    #Initializing variables required for a new game
    song            = [keyAb4, keyE4, keyE4, keyC5, keyC5, keyE4, keyE4, keyC5, keyC5, keyE4, keyF4, keyE4, keyD4, keyD4, keyD4, keyB4, keyB4, keyD4, keyD4, keyB4, keyB4, keyD4, keyE4, keyD4, keyC4, keyC4, keyC4, keyA4, keyA4, keyC4, keyC4, keyA4, keyA4, keyC4, keyD4, keyC4, keyB3, keyB3, keyB3, keyAb4, keyAb4, keyA4, keyB4, keyF4]
    pattern         = []
    currentStep     = 0     #the next note to be repeated
    noteIndex       = 0     #indexes the notes in the song array
    lastClickTime   = 0     #timestamp of the player's last button push
    score           = 0     #stores the score
    waitingForInput = False #when false, the pattern is playing

    #Main loop
    while True:
        clickedButton = None
        displaySurf.fill(bgColor)
        drawKeys()

        scoreSurf = font.render('Score: ' + str(score), 1, white)
        scoreRect = scoreSurf.get_rect()
        scoreRect.topleft = (570, 15)
        displaySurf.blit(scoreSurf, scoreRect)

        displaySurf.blit(infoSurf, infoRect)
        checkForQuit()
        
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                clickedButton  = getKeyClicked(mousex, mousey)

        if not waitingForInput:
            #play the next note
            pygame.display.update()
            pygame.time.wait(1000)
            pattern.append(song[noteIndex])
            noteIndex += 1
            
            for key in pattern:
                flashKeyAnimation(key)
                pygame.time.wait(delay)
            waitingForInput = True
        else:
            #wait for the player input
            if clickedButton and clickedButton == pattern[currentStep]:
                #played the correct note
                flashKeyAnimation(clickedButton)
                currentStep  += 1
                lastClickTime = time.time()

                if currentStep == len(pattern):
                    #played the last note
                    changeBackgroundAnimation()
                    score += 1
                    waitingForInput = False
                    currentStep     = 0

            elif (clickedButton and clickedButton != pattern[currentStep]) or (currentStep != 0 and time.time() - timeout > lastClickTime):
                #played incorrect note or timed out
                gameOverAnimation()
                pattern         = []
                currentStep     = 0
                noteIndex       = 0
                score           = 0
                waitingForInput = False
                pygame.time.wait(1000)
                changeBackgroundAnimation()

        pygame.display.update()
        fpsClock.tick(fps)


#Checks for quit requests
def checkForQuit():
    for event in pygame.event.get(QUIT):
        pygame.quit()
        sys.exit()

#Plays the appropriate sound and flashes the correct key
def flashKeyAnimation(key, animationSpeed=50):
    if key   == keyA3:
        sound = A3
        flashColor = brightRed
        rectangle  = keyA3

    elif key == keyBb3:
        sound = Bb3
        flashColor = brightRed
        rectangle  = keyBb3

    elif key == keyB3:
        sound = B3
        flashColor = brightRed
        rectangle  = keyB3
        
    elif key == keyC4:
        sound = C4
        flashColor = brightRed
        rectangle  = keyC4

    elif key == keyDb4:
        sound = Db4
        flashColor = brightRed
        rectangle  = keyDb4

    elif key == keyD4:
        sound = D4
        flashColor = brightRed
        rectangle  = keyD4

    elif key == keyEb4:
        sound = Eb4
        flashColor = brightRed
        rectangle  = keyEb4

    elif key == keyE4:
        sound = E4
        flashColor = brightRed
        rectangle  = keyE4

    elif key == keyF4:
        sound = F4
        flashColor = brightRed
        rectangle  = keyF4

    elif key == keyGb4:
        sound = Gb4
        flashColor = brightRed
        rectangle  = keyGb4

    elif key == keyG4:
        sound = G4
        flashColor = brightRed
        rectangle  = keyG4

    elif key == keyAb4:
        sound = Ab4
        flashColor = brightRed
        rectangle  = keyAb4

    elif key == keyA4:
        sound = A4
        flashColor = brightRed
        rectangle  = keyA4

    elif key == keyBb4:
        sound = Bb4
        flashColor = brightRed
        rectangle  = keyBb4

    elif key == keyB4:
        sound = B4
        flashColor = brightRed
        rectangle  = keyB4

    elif key == keyC5:
        sound = C5
        flashColor = brightRed
        rectangle  = keyC5

    elif key == keyDb5:
        sound = Db5
        flashColor = brightRed
        rectangle  = keyDb5

    elif key == keyD5:
        sound = D5
        flashColor = brightRed
        rectangle  = keyD5

    origSurf  = displaySurf.copy()
    if key != keyAb4:
        flashSurf = pygame.Surface((whiteWidth, 60))
    else:
        flashSurf = pygame.Surface((blackWidth, 36))
    flashSurf = flashSurf.convert_alpha()
    r, g, b   = brightRed
    sound.play()
    for start, end, step in ((0, 255, 1), (255, 0, -1)):
        for alpha in range(start, end, animationSpeed * step):
            checkForQuit()
            displaySurf.blit(origSurf, (0, 0))
            flashSurf.fill((r, g, b, alpha))
            if key != keyAb4:
                displaySurf.blit(flashSurf, (rectangle.x, rectangle.y+90))
            else:
                displaySurf.blit(flashSurf, (rectangle.x, rectangle.y+54))
            pygame.display.update()
            fpsClock.tick(fps)
    displaySurf.blit(origSurf, (0, 0))


#Draws the keys on the screen
def drawKeys():
    #Drawing white keys first
    pygame.draw.rect(displaySurf, white,  keyA3)
    pygame.draw.rect(displaySurf, white,  keyB3)
    pygame.draw.rect(displaySurf, white,  keyC4)
    pygame.draw.rect(displaySurf, white,  keyD4)
    pygame.draw.rect(displaySurf, white,  keyE4)
    pygame.draw.rect(displaySurf, white,  keyF4)
    pygame.draw.rect(displaySurf, white,  keyG4)
    pygame.draw.rect(displaySurf, white,  keyA4)
    pygame.draw.rect(displaySurf, white,  keyB4)
    pygame.draw.rect(displaySurf, white,  keyC5)
    pygame.draw.rect(displaySurf, white,  keyD5)

    #Drawing black keys after to be on top
    pygame.draw.rect(displaySurf, black,  keyBb3)
    pygame.draw.rect(displaySurf, black,  keyDb4)
    pygame.draw.rect(displaySurf, black,  keyEb4)
    pygame.draw.rect(displaySurf, black,  keyGb4)
    pygame.draw.rect(displaySurf, black,  keyAb4)
    pygame.draw.rect(displaySurf, black,  keyBb4)
    pygame.draw.rect(displaySurf, black,  keyDb5)
    

#Changes the background color smoothly
def changeBackgroundAnimation(animationSpeed=40):
    global bgColor
    newBgColor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    newBgSurf = pygame.Surface((winWidth, winHeight))
    newBgSurf = newBgSurf.convert_alpha()
    r, g, b = newBgColor
    for alpha in range(0, 255, animationSpeed):
        checkForQuit()
        displaySurf.fill(bgColor)

        newBgSurf.fill((r, g, b, alpha))
        displaySurf.blit(newBgSurf, (0, 0))

        drawKeys() #redraw the keys on top of the tint

        pygame.display.update()
        fpsClock.tick(fps)
    bgColor = newBgColor


#Plays the main chord and flashes the screen
def gameOverAnimation(color=white, animationSpeed=50):
    origSurf  = displaySurf.copy()
    flashSurf = pygame.Surface(displaySurf.get_size())
    flashSurf = flashSurf.convert_alpha()
    pattern   = []
    C4.play()
    E4.play()
    A4.play()
    C5.play()
    r, g, b   = color

    #Flashes the screen 3 times
    for i in range(3):
        for start, end, step in ((0, 255, 1), (255, 0, -1)):
            for alpha in range(start, end, animationSpeed * step):
                checkForQuit()
                flashSurf.fill((r, g, b, alpha))
                displaySurf.blit(origSurf, (0, 0))
                displaySurf.blit(flashSurf, (0, 0))
                drawKeys()
                pygame.display.update()
                fpsClock.tick(fps)


#Returns the key that the player last clicked
def getKeyClicked(x, y):
    
    if   keyA3.collidepoint((x, y)):
        return keyA3
    
    elif keyBb3.collidepoint((x, y)):
        return keyBb3

    elif keyB3.collidepoint((x, y)):
        return keyB3

    elif keyC4.collidepoint((x, y)):
        return keyC4

    elif keyDb4.collidepoint((x, y)):
        return keyDb4

    elif keyD4.collidepoint((x, y)):
        return keyD4

    elif keyEb4.collidepoint((x, y)):
        return keyEb4

    elif keyE4.collidepoint((x, y)):
        return keyE4

    elif keyF4.collidepoint((x, y)):
        return keyF4

    elif keyGb4.collidepoint((x, y)):
        return keyGb4

    elif keyG4.collidepoint((x, y)):
        return keyG4

    elif keyAb4.collidepoint((x, y)):
        return keyAb4

    elif keyA4.collidepoint((x, y)):
        return keyA4

    elif keyBb4.collidepoint((x, y)):
        return keyBb4

    elif keyB4.collidepoint((x, y)):
        return keyB4

    elif keyC5.collidepoint((x, y)):
        return keyC5

    elif keyDb5.collidepoint((x, y)):
        return keyDb5

    elif keyD5.collidepoint((x, y)):
        return keyD5
    
    return None


if __name__ == '__main__':
    main()
