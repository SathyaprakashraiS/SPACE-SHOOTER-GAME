import pygame
import random
import time
pygame.init()
#(width,height)
screen=pygame.display.set_mode((800,600))
running=True

pygame.display.set_caption("A GAME")
icon=pygame.image.load('sEnemy.png')
bg=pygame.image.load("BG2.png")
pygame.display.set_icon(icon)

playerimg=pygame.image.load("sPlayer0.png")
enemyimg=pygame.image.load("sEnemy0.png")
bulletimg=pygame.image.load("sBullet.png")

playerx=300
playery=400
enemyx=random.randint(2,798)
enemyy=random.randint(2,598)
bulletx=300
bullety=367
bulletxarray=[]
bulletyarray=[]
bulletbool=False
cooldown=0

coins=0
font=pygame.font.Font('freesansbold.ttf',32)
textx=10
texty=10

def scoreboard(x,y):
	score=font.render("SCORE:"+str(coins),True,(255,255,255))
	screen.blit(score,(x,y))

def bodyboundary(objimg,posx,posy):
	if(posx>=750):
		posx=750
		posy=posy
		screen.blit(objimg,(posx,posy))
	elif(posx<=2):
		posx=2
		posy=posy
		screen.blit(playerimg,(posx,posy))
	else:
		screen.blit(playerimg,(posx,posy))
	return posx,posy
def player(playerx,playery):
	if(playerx>=750):
		playerx=750
		playery=playery
		screen.blit(playerimg,(playerx,playery))
	elif(playerx<=2):
		playerx=2
		playery=playery
		screen.blit(playerimg,(playerx,playery))
	else:
		screen.blit(playerimg,(playerx,playery))
	return playerx,playery
def enemy(playerx,playery):
	if(playerx>=750):
		playerx=750
		playery=playery
		screen.blit(enemyimg,(playerx,playery))
	elif(playerx<=2):
		playerx=2
		playery=playery
		screen.blit(enemyimg,(playerx,playery))
	elif():
		pass
	else:
		screen.blit(enemyimg,(playerx,playery))

def bullet(bulletxpos,bulletypos):
	if(bulletypos>=595):
		return bulletxpos,bulletypos,False
	if(bulletypos<=10):
		return bulletxpos,bulletypos,False
	else:
		screen.blit(bulletimg,(bulletxpos,bulletypos))
		bulletypos-=1
		return bulletxpos,bulletypos,True

while running:
	screen.fill((255,255,255))
	screen.blit(bg,(0,0))
	for event in pygame.event.get():
		if event.type== pygame.QUIT:
			running=False

	for i in range(len(bulletxarray)):
		if(bulletxarray[i]==-1):
			pass
		else:
			tempbx,tempby,pon=bullet(bulletxarray[i],bulletyarray[i])
			if(pon==True):
				bulletxarray[i]=tempbx
				bulletyarray[i]=tempby
			else:
				#bulletxarray.pop(i)
				#bulletyarray.pop(i)
				bulletxarray[i]=-1
				bulletyarray[i]=-1
	playerx,playery=player(playerx,playery)
	enemy(enemyx,enemyx)
	cooldown+=1
	if event.type==pygame.KEYDOWN:
		if event.key==pygame.K_LEFT:
			print("press left")
			playerx-=0.3
			playery+=0
		if event.key==pygame.K_RIGHT:
			print("press right")
			playerx+=0.3
			playery+=0
		if (event.key==pygame.K_UP) and (cooldown>=100):
			print("press space")
			bulletx=playerx
			bullety=playery-33
			bulletxarray.append(bulletx)
			bulletyarray.append(bullety)
			screen.blit(bulletimg,(bulletx,bullety))
			bulletbool=True
			cooldown=0
	if event.type==pygame.KEYUP:
		if event.key==pygame.K_LEFT:
			print("lift left")
			playerx-=0
		if event.key==pygame.K_RIGHT:
			print("lift right")
			playerx-=0
	scoreboard(textx,texty)
	pygame.display.update()