import os,time 
tscores=[]
with open('scores.txt', encoding='utf8') as f:
	for line in f:
		if(line!='\n'):
			tscores.append(line[:-1])
		else:
			tscores.append(0)
coins=40
temp=0
def quitfunc():
	print(tscores)
	time.sleep(1)
	os._exit(0)
def reverser(q,coins,temp):
	for i in range(q+1,len(tscores)):
		try:
			thetemp=tscores[i]
			tscores[i]=temp
			temp=thetemp
		except:
			tscores[i]=temp
	'''
	for i in range(len(tscores)-1,q+1,-1):
		print(i,tscores[i])
		if(int(tscores[i-1])!=int(coins)):
			tscores[i]=tscores[i-1]
		if(int(tscores[i-1])==int(coins)):
			tscores[i]=temp
	'''
for i in range(len(tscores)):
	temp=0
	if(int(coins)>int(tscores[i])):
		temp=tscores[i]
		tscores[i]=coins
		reverser(i,coins,temp)
		quitfunc()
		'''
		try:
			thetemp=tscores[i+1]
			tscores[i+1]=temp
			temp=thetemp
			reverser(i,coins,temp)
			quitfunc()
		except:
			reverser(i,coins,temp)
			quitfunc()
		'''
