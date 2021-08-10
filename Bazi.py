import pygame,time,random,os

pygame.init()

Crash_Sound = pygame.mixer.Sound("lose-m.wav")
pygame.mixer.music.load("world-m.ogg")
carImg = pygame.image.load("Machine.png")

#Colors
White = (255,255,255)
Black = (0,0,0)
Red = (255,0,0)
Green = (0,255,0)
Blue = (0,0,255)
Yellow = (255,255,0)
Orange = (255,160,0)
Dark_Green = (0,200,0)
Dark_Red = (200,0,0)
Color_List = [Black,Red,Green,Blue,Yellow,Orange]
#Screen Sizes
screenWidth = 800
screenHeight = 600

gameScreen = pygame.display.set_mode((screenWidth,screenHeight))
gameCaption = pygame.display.set_caption("Be Mane Nakhori!")

clock = pygame.time.Clock()
carWidth = 48
carHeight = 80


def Exiting():
    pygame.quit()
    quit()

def Button(Msg,BtnX,BtnY,BtnW,BtnH,InAc,Ac,Action=None):
    Mouse = pygame.mouse.get_pos()
    Click = pygame.mouse.get_pressed()
    if BtnX + BtnW > Mouse[0] > BtnX and BtnY + BtnH > Mouse[1] > BtnY:
        pygame.draw.rect(gameScreen,Ac,(BtnX,BtnY,BtnW,BtnH))
        if Click[0] == 1 and Action != None:
            Action()
    else:
        pygame.draw.rect(gameScreen,InAc,(BtnX,BtnY,BtnW,BtnH))
    smallText = pygame.font.Font("freesansbold.ttf",21)
    textSurf,textRect = text_object(Msg,smallText,Black)
    textRect.center = ((BtnX +(BtnW)/2),(BtnY+(BtnH)/2))
    gameScreen.blit(textSurf,textRect)

def Game_Intro():
    Intro = True
    while Intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameScreen.fill(White)
        largeText = pygame.font.Font('freesansbold.ttf',80)
        TextSurf, TextRect = text_object("Bezan Berim Bazi!",largeText,Black)
        TextRect.center = ((screenWidth/2),(screenHeight/2))
        gameScreen.blit(TextSurf,TextRect)
        Button("Play!",150,450,100,50,Dark_Green,Green,Game_Running)
        Button("Quit",550,450,100,50,Dark_Red,Red,Exiting)
        pygame.display.update()

def Score(Counter):
    font = pygame.font.SysFont(None,25)
    text = font.render("Score : "+str(Counter),True,Black)
    gameScreen.blit(text,(0,0))

def Bombaroon(bomba_x,bomba_y,bomba_w,bomba_h,bomba_color):
    pygame.draw.rect(gameScreen,bomba_color,[bomba_x,bomba_y,bomba_w,bomba_h])

def Shoot(shoot_x,shoot_y,shoot_w,shoot_h,shoot_color):
    pygame.draw.rect(gameScreen,shoot_color,[shoot_x,shoot_y,shoot_w,shoot_h])

def blitCar(Car_x,Car_y):
    gameScreen.blit(carImg,(Car_x,Car_y))

def text_object(objText,objFont,objColor):
    textSurface = objFont.render(objText, True , objColor)
    return textSurface, textSurface.get_rect()

def BlitMsgInDis(blitText,blitColor,blitSize):
    largeText = pygame.font.Font("freesansbold.ttf",90)
    TextSurf, TextRect = text_object(blitText,largeText,blitColor)
    TextRect.center = ((screenWidth/2),(screenHeight/2))
    gameScreen.blit(TextSurf,TextRect)
    pygame.display.update()

def Win():
    BlitMsgInDis("! You Win !",Dark_Green,115)
    time.sleep(2)
    Game_Intro()

def Crash():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(Crash_Sound)
    BlitMsgInDis("You Crashed",Dark_Red,95)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        Button("Try Again",150,450,100,50,Dark_Green,Green,Game_Running)
        Button("Quit",550,450,100,50,Dark_Red,Red,Exiting)
        pygame.display.update()

def Game_Running():
    pygame.mixer.music.play(-1)
    Car_X,Car_Y = screenWidth*0.45 , screenHeight*0.8
    Car_X_Change = 0
    BombaroonStr_x = random.randrange(0,screenWidth)
    BombaroonStr_y = -600
    Bombaroon_Speed = 5
    Bombaroon_W = 100
    Bombaroon_H = 100
    Randco = random.randrange(0,6)
    Random_Color = Color_List[Randco]
    score = 0
    Shoot_Speed = 3
    gameExit = False
    while not(gameExit):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_LEFT:
                    Car_X_Change -= 5
                elif event.key == pygame.K_RIGHT:
                    Car_X_Change += 5
            if event.type == pygame.KEYUP:
                if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                    Car_X_Change = 0
        Car_X += Car_X_Change
        gameScreen.fill(White)
        Score(score)
        blitCar(Car_X,Car_Y)
        Bombaroon(BombaroonStr_x,BombaroonStr_y,Bombaroon_W,Bombaroon_H,Random_Color)
        BombaroonStr_y += Bombaroon_Speed
        if Car_X > screenWidth - carWidth or Car_X < 0:
            Crash()
        if BombaroonStr_y > screenHeight:
            BombaroonStr_y = 0 - Bombaroon_H
            BombaroonStr_x = random.randrange(0,screenWidth-100)
            Randco = random.randrange(0,5)
            Random_Color = Color_List[Randco]
            score += 1
            Bombaroon_Speed += 1
        elif score == 30:
            Win()
        if Car_Y < BombaroonStr_y + Bombaroon_H:
            if (Car_X > BombaroonStr_x and Car_X < BombaroonStr_x + Bombaroon_W) or Car_X + carWidth > BombaroonStr_x and Car_X + carWidth < BombaroonStr_x + Bombaroon_W:
                Crash()
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    Game_Intro()
    pygame.quit()
    quit()
