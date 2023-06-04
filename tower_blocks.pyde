

def setup():
    global gamestage, bg, block, angle, angleA, angleV, gravity, lineLen, lineOriginX, lineOriginY
    global blockX, blockY, blockW, blockH, climb, hide, blockFall, blockLanded, lives, score, maxScore, exitBtn, restartBtn
    global exitOver, restartOver
    
    exitOver = False
    restartOver = False
    
    size(500, 800)
    bg = loadImage("bg.png")
    block = loadImage("block.png")
    exitBtn = loadImage("exit.png")
    restartBtn = loadImage("restart.png")
    gamestage = 0
    angle = PI/4
    angleA = 0
    angleV = 0
    gravity = 1
    lineLen = 150
    lineOriginX = 250
    lineOriginY = -50
    climb = 0
    lives = 3
    score = 0
    maxScore = 0
    
    #blocks
    blockW = 150
    blockH = 110
    
    blockX = []
    blockY = []
    blockFall = False
    hide = 0
    
    blockX.append(175)
    blockY.append(690)
    
def draw():
    if(gamestage == 0):
        welcomePage()
    if(gamestage == 1):
        gamePlayPage()
    if(gamestage == 2):
        gameOverPage()


def gamePlayPage():
    ################# GAMEPLAY PAGE #################
    global angle, angleA, angleV, gravity, block, hide, blockFall, climb, score, maxscore, lives, gamestage
    image(bg, 0, 0, width, height)
    
    if(lives >0 ):
        #creating a swing motion of the Rope
        force = gravity * sin(angle)
        angleA = (-1 * force) / lineLen
        angleV += angleA
        angle += angleV
        yline = cos(angle) * lineLen 
        xline = sin(angle) * lineLen + lineOriginX
        stroke(0)
        strokeWeight(10)
        line(lineOriginX, lineOriginY, xline, yline)
        image(block, xline - blockW/2 + hide, yline, blockW, blockH)
        
        textAlign(LEFT)
        textSize(30)
        fill("#2c4757")
        text("Lives: " + str(lives), 10, 30)
        text("Score: " + str(score), 10, 60)
        
        for i in range (len(blockX)):
            image(block, blockX[i], blockY[i], blockW, blockH)
                
            if(blockFall == False and mousePressed == True):
                blockFall = True
                hide = width
                blockX.append(xline- blockW/2)                
                blockY.append(yline)
                    
            if(blockFall == True and blockY[len(blockY) - 1] < blockY[len(blockY)-2] - blockH):
                blockY[len(blockY)-1] +=3
                    
            # checks if a block fallen properly         
            elif(blockFall == True and (blockX[len(blockX)-1] < blockX[len(blockX)-2]-blockW/2 or blockX[len(blockX)-1]> blockX[len(blockX)-2] + blockW/2)):
                blockX[len(blockX)-1] = blockX[len(blockX)-2]
                blockY[len(blockY)-1] = blockY[len(blockY)-2] 
                lives -= 1
                blockFall = False
                hide = 0
            else:
                blockFall = False
                hide = 0
                
        #drags down the screen depending on the amount of blocks
        if(blockFall == False and blockY[len(blockX)-1] < 500):
            climb = 500-blockY[len(blockX)-1]
            score += int(climb)
            for i in range (len(blockY)):
                blockY[i] += climb
        else:
            climb = 0
                
            # deletes blocks out of screen
            if(blockY[i] > height):
                blockX.pop(i)
                blockY.pop(i)
    
    if(lives == 0):
        gamestage = 2
        gameOverPage()
    ################# GAMEPLAY PAGE #################  
    
  
def gameOverPage():
    ################# GAMEOVER PAGE #################
    global score, maxScore
    image(bg, 0, 0, width, height)
    if(score > maxScore):
        maxScore = score
    
    noStroke()
    textAlign(CENTER)
    
    fill("#2c4757")
    rect(25, 60, 450, 295 ,25)
    fill(255)
    textSize(100)
    text("GAME", 250, 170)
    text("OVER!", 250, 320)
    
    fill("#2c4757")
    rect(80, 375, 340, 120, 25)
    fill(255)
    textSize(50)
    text("Your record:" , 250, 430)
    text(str(maxScore), 250, 480)
    
    image(restartBtn, 70, 530, 150, 150)
    image(exitBtn, 270, 530, 150, 150)
    ################# GAMEOVER PAGE #################  
  
def welcomePage():
     ################# WELCOME PAGE #################
    image(bg, 0, 0, width, height)
    textAlign(LEFT)
    fill("#163540")
    textSize(120)
    text("BLOCKS", 10, 290)
    text("TOWER", 40, 120)
    fill("#2c4757")
    text("BLOCKS", 15, 295)
    text("TOWER", 45, 125)
    noStroke()
    rect(10, 320, 480, 225, 25)
    fill(255)
    textSize(50)
    text("Instructions:", 110, 375)
    textSize(20)
    text(" A swinging crane holds a section of a tower", 30, 430)
    text("above a platform. Click the mouse to drop it,", 30, 460)
    text("then try and stack the following pieces ", 30, 490)
    text("on top as neatly as you can.", 30, 520)
    fill("#62717e")
    rect(10, 590, 480, 80, 25)
    fill(255)
    textSize(30)
    text("Press any key to start the game", 25, 635)
    ################# WELCOME PAGE #################
    

def keyPressed():
    global gamestage
    #changing gamestages 
    if(gamestage == 0):
        gamestage = 1

def mousePressed():
    global gamestage, score, blockX, blockY, lives, blockFall, hide
    #finds out if the mouse is over the buttons 
    if((sqrt(sq(145-mouseX) + sq(605-mouseY)) < 150/2) and gamestage == 2):
        #resets the values for the new game
        score = 0
        lives = 3
        blockX = []
        blockY = []
        blockFall = False
        hide = 0
    
        blockX.append(175)
        blockY.append(690)
        #changes gamestages 
        gamestage = 1
        exitOver = True
        print(str(exitOver))
    if((sqrt(sq(345-mouseX) + sq(605-mouseY)) < 150/2) and gamestage == 2):
        exit()
        restartOver = True
        print(str(restartOver))
    
