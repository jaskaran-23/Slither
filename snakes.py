import pygame
import time
import random
pygame.init()
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,225,0)
display_width=800
display_height=600

gamedisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Slither")

icon=pygame.image.load("apple.png")
pygame.display.set_icon(icon)

pygame.display.update()
img=pygame.image.load("snakehead.png")
appleimg=pygame.image.load("apple.png")

block_size=20
apple_size=50
clock=pygame.time.Clock()
FPS=10
direction="right"
smallfont=pygame.font.SysFont("comicsansms",25)          
medfont=pygame.font.SysFont("comicsansms",50)
largefont=pygame.font.SysFont("arial",75)

def pause():
    paused=True
    
    message_to_screen("Paused",red,-100,size="large")
    message_to_screen("Press C to continue or Q to quit.",black,25,"medium")
    pygame.display.update()
    while paused:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_c:
                    paused=False
                elif event.key==pygame.K_q:
                    pygame.quit()
                    quit()
        
        #gamedisplay.fill(white)
        message_to_screen("Paused",red,-100,size="large")
        message_to_screen("Press C to continue or Q to quit.",black,25,"medium")
        pygame.display.update()
        clock.tick(5)

def score(score):
    text=smallfont.render("Score: "+str(score),True,black)
    gamedisplay.blit(text,[0,0])

def randapplegen():
    randapplex=round(random.randrange(0,display_width-apple_size))#/10)*10.0
    randappley=round(random.randrange(0,display_height-apple_size))#/10)*10.0
    return randapplex,randappley
randapplex,randappley=randapplegen()

def intro():
    intro=True
    while intro ==True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_c:
                    intro=False
                if event.key==pygame.K_q:
                    pygame.quit()
                    quit()
                
        gamedisplay.fill(white)
        message_to_screen("Welcome to slither...",green,-100,"large")
        message_to_screen("Objective is to eat black apples :D",red,-10,"medium")
        message_to_screen("More apples you eat more points you get, yups...",black,40,"small")
        message_to_screen("All the best!!!",red,100,"medium")
        message_to_screen("Press C to play else Q to quit...",black,180,"medium")
        pygame.display.update()
        clock.tick(15)
        

def snake(block_size,snakelist):
    if direction=="right":
        head=img
    if direction=="left":
        head=pygame.transform.rotate(img,180)
    if direction=="up":
        head=pygame.transform.rotate(img,90)
    if direction=="down":
        head=pygame.transform.rotate(img,270)
    gamedisplay.blit(head,(snakelist[-1][0],snakelist[-1][1]))
    for xny in snakelist[:-1]:
        pygame.draw.rect(gamedisplay,green,[xny[0],xny[1],block_size,block_size])
def text_objects(text,color,size):
    if size=="small":
        textsurface=smallfont.render(text,True,color)
    if size=="medium":
        textsurface=medfont.render(text,True,color)
    if size=="large":
        textsurface=largefont.render(text,True,color)
    return textsurface,textsurface.get_rect()
    
def message_to_screen(msg,color,ydisp=0,size="small"):
   # screen_text=font.render(msg,True,color)
    #gamedisplay.blit(screen_text,[display_width/2,display_height/2])
   textsurface,textrect=text_objects(msg,color,size)
   textrect.center=(display_width/2),(display_height/2)+ydisp
   gamedisplay.blit(textsurface,textrect)
def gameLoop():
    global direction
    direction="right"
    snakelist=[]
    snakelength=1
    gameexit=False
    gameover=False
    lead_x=display_width/2
    lead_y=display_height/2
    lead_x_change=10
    lead_y_change=0
    randapplex=round(random.randrange(0,display_width-apple_size))#/10)*10.0
    randappley=round(random.randrange(0,display_height-apple_size))#/10)*10.0
    while not gameexit:
        while gameover==True:
            gamedisplay.fill(white)
            message_to_screen("Game over",red,-50,size="large")
            message_to_screen("Press c to play again else q to quit",black,50,size="medium")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    gameover=False
                    gameexit=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        gameexit=True
                        gameover=False
                    elif event.key==pygame.K_c:
                        gameLoop()
        for event in pygame.event.get():
            if event.type==pygame.QUIT: 
               gameexit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    direction="left"
                    lead_x_change=-block_size
                    lead_y_change=0
                elif event.key==pygame.K_RIGHT:
                    direction="right"
                    lead_x_change=block_size
                    lead_y_change=0
                elif event.key==pygame.K_DOWN:
                    direction="down"
                    lead_y_change=block_size
                    lead_x_change=0
                elif event.key==pygame.K_UP:
                    direction="up"
                    lead_y_change=-block_size
                    lead_x_change=0
                elif event.key==pygame.K_p:
                    pause()
                    
        if lead_x>=display_width or lead_x<=0 or lead_y>=display_height or lead_y<=0:
            gameover=True
        lead_x+=lead_x_change
        lead_y+=lead_y_change
        gamedisplay.fill(white)
        
        gamedisplay.blit(appleimg,(randapplex,randappley))
       # pygame.draw.rect(gamedisplay,red,[randapplex,randappley,apple_size,apple_size])
        snakehead=[]
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)
        if len(snakelist)>snakelength:
            del snakelist[0]
        for eachsegment in snakelist[:-1]:
            if eachsegment==snakehead:
                gameover=True
        snake(block_size,snakelist)
        score(snakelength*5-5)

        
        pygame.display.update()
        if lead_x>=randapplex and lead_x<=randapplex+apple_size or lead_x+block_size>=randapplex and lead_x+block_size<=randapplex+apple_size:
                     if lead_y>=randappley and lead_y<=randappley+apple_size or lead_y+block_size>=randappley and lead_y+block_size<=randappley+apple_size:
                         randapplex=round(random.randrange(0,display_width-apple_size))#/10)*10.0
                         randappley=round(random.randrange(0,display_height-apple_size))#/10)*10.0
                         snakelength+=2
                   
        clock.tick(FPS)
    message_to_screen("Congrats",red)
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    quit()
intro()
gameLoop()
