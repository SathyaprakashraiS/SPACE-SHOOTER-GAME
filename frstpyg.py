import pygame
import random
import time
import os
import math
pygame.init()
#(width,height)
screen=pygame.display.set_mode((800,600))
running=True

gname="Space_shooteR"
gcatchy=""

pygame.display.set_caption("A GAME")
icon=pygame.image.load('sEnemy.png')
bg=pygame.image.load("BG2.png")
menuimg=pygame.image.load("D:/PYGAME/sprites/bgs/c1.png")
pygame.display.set_icon(icon)

playerimg=pygame.image.load("sPlayer0.png")
enemyimg=pygame.image.load("sEnemy0.png")
bulletimg=pygame.image.load("sBullet.png")

playerx=300
playery=400
#enemyx=random.randint(2,798)
#enemyy=random.randint(2,300)
#spawn enemy before 300 so player can hit him

e1x=[]
e1y=[]
e1turner=[]
e1spwaner=5
spawncooldown=5000

enemyx=20
enemyy=450
#enemyx=[]
#enemyy=[]
bulletx=300
bullety=367
bulletxarray=[]
bulletyarray=[]
bulletbool=False
cooldown=0
movespeed=1
coins=0

font=pygame.font.Font('freesansbold.ttf',32)
titlefont=pygame.font.Font('freesansbold.ttf',48)
menufonts=pygame.font.Font('freesansbold.ttf',32)
textx=10
texty=10

menu=True
game=False
credits=False
highscores=False
hit=False

mplayerx=200
mplayery=200
mangle=0

starttimer=0
highscorestimer=0
quittimer=0
selecttime=125
quitselecttime=250

bulletspeed=1.5
shipspeed=1

def title(x,y):
	gtitle=titlefont.render(gname,True,(255,255,255))
	screen.blit(gtitle,(x,y))
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
def menurotator(mplayerx,mplayery,mangle):
	mplayerimg=pygame.image.load("sPlayer0.png")
	mplayerimg=pygame.transform.rotate(mplayerimg,mangle)
	screen.blit(mplayerimg,(mplayerx,mplayery))
	ticker=random.randint(0,7)
	if(ticker==0):
		#N
		if():
			pass
		pass
	elif(ticker==1):
		#E
		pass
	elif(ticker==2):
		#W
		pass
	elif(ticker==3):
		#S
		pass
	elif(ticker==4):
		#SE
		pass
	elif(ticker==5):
		#NE
		pass
	elif(ticker==6):
		#NW
		pass
	elif(ticker==7):
		#SW
		pass
	return mplayerx,mplayery,mangle-1
def quitfunc():
	print("QUITTING...")
	time.sleep(1)
	os._exit(0)
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
def enemy(e1turner,e1x,e1y):
	if(e1turner!=0):
		if(e1turner==1):
			if(e1x>=765):
				e1turner=-1
				e1x-=1
				e1y+=20
				screen.blit(enemyimg,(e1x,e1y))
				return e1turner,e1x,e1y
			elif(e1x<=10):
				e1turner=1
				e1x+=1
				e1y+=20
				screen.blit(enemyimg,(e1x,e1y))
				return e1turner,e1x,e1y
			else:
				e1x+=1
				#e1y[i]+=20
				screen.blit(enemyimg,(e1x,e1y))
				return e1turner,e1x,e1y
		if(e1turner==-1):
			if(e1x>=765):
				e1turner=-1
				e1x-=1
				e1y+=20
				screen.blit(enemyimg,(e1x,e1y))
				return e1turner,e1x,e1y
			elif(e1x<=10):
				e1turner=1
				e1x+=1
				e1y+=20
				screen.blit(enemyimg,(e1x,e1y))
				return e1turner,e1x,e1y
			else:
				e1x-=1
				#e1y[i]+=20
				screen.blit(enemyimg,(e1x,e1y))
				return e1turner,e1x,e1y
	else:
		return e1turner,e1x,e1y

def bulletcollider(e1turner,eposx,eposy,bposx,bposy,hit):
	if(e1turner!=0):
		distance=math.sqrt(((bposx-eposx)*(bposx-eposx))+((bposy-eposy)*(bposy-eposy)))
		if(distance<=25):
			spawncooldown
			return 0,-1,-1,-1,-1,True
		else:
			return e1turner,eposx,eposy,bposx,bposy,False
	else:
		return e1turner,eposx,eposy,bposx,bposy,False

def bullet(bulletxpos,bulletypos):
	if(bulletypos>=595):
		return bulletxpos,bulletypos,False
	if(bulletypos<=10):
		return bulletxpos,bulletypos,False
	else:
		screen.blit(bulletimg,(bulletxpos,bulletypos))
		bulletypos-=bulletspeed
		return bulletxpos,bulletypos,True
priority=[0,0,0,0]
double=False
stopper=0
while running:
	if(menu):
		mousepos=pygame.mouse.get_pos()
		screen.fill((255,255,255))
		screen.blit(menuimg,(0,0))
		for event in pygame.event.get():
			if event.type== pygame.QUIT:
				running=False
		title(230,100)
		#pygame.draw.rect(screen,(R,G,B),[xpos,ypos,width,height])
		pygame.draw.rect(screen,(0,0,0),[340,290,125,50])
		start=font.render('START' , True , (255,255,255))
		pygame.draw.rect(screen,(0,0,0),[290,340,240,50])
		viewscore=font.render('HIGH SCORES' , True , (255,255,255))
		pygame.draw.rect(screen,(0,0,0),[350,390,100,50])
		quit=font.render('QUIT' , True , (255,255,255))
		print(mousepos[0],mousepos[1])
		if(330<=mousepos[0]<=450 and 280<=mousepos[1]<=330):
			pygame.draw.rect(screen,(100,100,100),[340,290,125,50])
			starttimer+=1
			highscorestimer=0
			quittimer=0
			if(starttimer>selecttime):
				menu=False
				game=True
			'''
			for event in pygame.event.get():
				if(330<=mousepos[0]<=450 and 280<=mousepos[1]<=330 and event.type==pygame.MOUSEBUTTONDOWN):
					menu=False
					game=True
			'''
		elif(280<=mousepos[0]<=500 and 330<=mousepos[1]<=380):
			pygame.draw.rect(screen,(100,100,100),[290,340,240,50])
			highscorestimer+=1
			starttimer=0
			quittimer=0
		elif(340<=mousepos[0]<=550 and 380<=mousepos[1]<=430):
			pygame.draw.rect(screen,(100,100,100),[350,390,100,50])
			quittimer+=1
			starttimer=0
			highscorestimer=0
			if(quittimer>quitselecttime):
				pygame.quit()
				quitfunc()
			'''
			for event in pygame.event.get():
				if(340<=mousepos[0]<=550 and 380<=mousepos[1]<=430 and event.type==pygame.MOUSEBUTTONDOWN):
					pygame.quit()
			'''
		#else:
			#pygame.draw.rect(screen,(100,100,100),[340,290,125,50])
		screen.blit(start,(350,300))
		screen.blit(viewscore,(300,350))
		screen.blit(quit,(360,400))

		mplayerx,mplayery,mangle=menurotator(mousepos[0]-10,mousepos[1]-15,mangle)
		'''
		for event in pygame.event.get():
			if event.type== pygame.QUIT:
				running=False
			elif event.type==pygame.MOUSEBUTTONDOWN:
				if(340<=mousepos[0]<=550 and 380<=mousepos[1]<=430):
					pygame.quit()
				elif(330<=mousepos[0]<=450 and 280<=mousepos[1]<=330):
					menu=False
					game=True
		'''

		pygame.display.update()
	#[left,right,up,down]
	elif(game):
		spawncooldown+=1
		print(priority,double)
		keys=pygame.key.get_pressed()
		screen.fill((255,255,255))
		screen.blit(bg,(0,0))
		if(e1spwaner>0 and spawncooldown>=1000):
			spawncooldown=0
			e1spwaner-=1
			spawnerx=random.randint(20,300)
			#spawnery=random.randint(2,300)
			spawnery=10
			e1x.append(spawnerx)
			e1y.append(spawnery)
			temp=random.randint(0,5)
			if((temp%2)==0):
				e1turner.append(1)
			else:
				e1turner.append(-1)
		for i in range(len(e1x)):
			print(e1turner[i],e1x[i],e1y[i])
			e1turner[i],e1x[i],e1y[i]=enemy(e1turner[i],e1x[i],e1y[i])
			'''
			if(e1turner[i]!=0):
				if(e1x[i]>=790):
					e1turner[i]=-1
					e1x[i]-=1
					e1y[i]+=20
					screen.blit(enemyimg,(e1x[i],e1y[i]))
				elif(e1x[i]<=10):
					e1turner[i]=1
					e1x[i]+=1
					e1y[i]+=20
					screen.blit(enemyimg,(e1x[i],e1y[i]))
				elif(e1turner[i]==1):
					e1x[i]+=1
					#e1y[i]+=20
					screen.blit(enemyimg,(e1x[i],e1y[i]))
				elif(e1turner[i]==-1):
					e1x[i]-=1
					#e1y[i]+=20
					screen.blit(enemyimg,(e1x[i],e1y[i]))
			'''
		for event in pygame.event.get():
			if event.type== pygame.QUIT:
				running=False

		for i in range(len(e1x)):
			for j in range(len(bulletxarray)):
				e1turner[i],e1x[i],e1y[i],bulletxarray[j],bulletyarray[j],hit=bulletcollider(e1turner[i],e1x[i],e1y[i],bulletxarray[j],bulletyarray[j],hit)
				if(hit):
					e1spwaner+=1
					coins+=10
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
		#enemyx,enemyy=enemy(enemyx,enemyx)
		cooldown+=1
		if event.type==pygame.KEYDOWN:
			'''
			if keys[pygame.K_LEFT]:
				print("press left")
				playerx-=0.3
				playery+=0
			if keys[pygame.K_RIGHT]:
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
			'''
			if(keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]):
				print("both left and right")
				if(priority[0]==0 and priority[1]==1 and double==False):
					playerx-=shipspeed
					playery+=0
					priority=[0,0,0,0]
					priority[0]=1
					double=True
				elif(priority[0]==1 and priority[1]==0 and double==False):
					playerx+=shipspeed
					playery+=0
					priority=[0,0,0,0]
					priority[1]=1
					double=True
				elif(priority[0]==0 and priority[1]==1 and double==True):
					playerx-=shipspeed
					playery+=0
					double=True
				elif(priority[0]==1 and priority[1]==0 and double==True):
					playerx+=shipspeed
					playery+=0
					double=True
			elif(keys[pygame.K_LEFT]):
				print("only left")
				print("press left")
				playerx-=shipspeed
				playery+=0
				priority=[0,0,0,0]
				priority[0]=1
				double=False
			elif(keys[pygame.K_RIGHT]):
				print("only right")
				print("press right")
				playerx+=shipspeed
				playery+=0
				priority=[0,0,0,0]
				priority[1]=1
				double=False
			elif(keys[pygame.K_DOWN] ):
				print("only down")
				playerx+=0
				playery+=0
				priority=[0,0,0,0]
				priority[3]=1
				double=False
			#elif(keys[pygame.K_UP] and (cooldown>=100)):
			elif((keys[pygame.K_UP] and (cooldown>=100)) or (priority[2]==1 and (cooldown>=100) and double==True)):
				print("only up")
				print("press space")
				bulletx=playerx
				bullety=playery-33
				priority=[0,0,0,0]
				priority[3]=1
				bulletxarray.append(bulletx)
				bulletyarray.append(bullety)
				screen.blit(bulletimg,(bulletx,bullety))
				bulletbool=True
				cooldown=0
				double=True
			else:
				print("nothing")
				priority=[0,0,0,0]
		
		elif((priority[0]==1 and double==True) or (priority[1]==1 and double==True)):
			if(priority[0]==1 and double==True):
				playerx-=shipspeed
				playery+=0
				print("IN HERE 1")
			elif(priority[1]==1 and double==True):
				playerx+=shipspeed
				playery+=0
				print("IN HERE 2")

		'''		
		if event.type==pygame.KEYUP:
			if event.key==pygame.K_LEFT:
				print("lift left")
				playerx-=0
			if event.key==pygame.K_RIGHT:
				print("lift right")
				playerx-=0
		'''
		scoreboard(textx,texty)
		pygame.display.update()
	pygame.display.update()