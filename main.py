################
# main.py      #
# S.Guillier.  #
# 18/10/2017   #
# S2A TFTRG    #
################
#Modules PyBoard
import pyb
import mpr121
#Modules externes
import os
import time
#Mes Modules
import Animat
import Background

animat = None
bg = None
timeStep = None

def init():
	global lcd, m, animat,bg,bg2,timeStep,dpBG,rdbg
	#Init PyBoard
	lcd = pyb.LCD('X')
	lcd.light(True)
	m = mpr121.MPR121(pyb.I2C(1, pyb.I2C.MASTER))
	dpBG=-4
	rdbg = 2
	#Addition jusqua valeur et retour 0
	timeStep = 0.3
	animat = Animat.create("player.txt",0)
	bg = Background.create("level1.txt")
	bg2 = Background.create("level2.txt")

def move():
	global dpBG,bg,bg2
	if dpBG <=127:
		dpBG= dpBG+6
	else:
		dpBG = 6
		bg = Background.create("level"+str(rdbg)+".txt")
		#rdbg = rdbg +1
		bg2 = Background.create("level"+str(rdbg)+".txt")
		
	Animat.jump(animat)
	ay = Animat.getY(animat)
	if ay==0:
		if dpBG >= 111:
			if Background.getChar(bg2, dpBG-111,30) == " ":
				Animat.setFalling(animat)
				Animat.fall(animat)
		elif Background.getChar(bg, 16+dpBG,30) == " ":
			Animat.setFalling(animat)
			Animat.fall(animat)
		if Background.getChar(bg2, dpBG-111, 30) == "#":			#Gere maintien sur platforme basse
			Animat.resetOnUpperPlatform(animat)
		elif Background.getChar(bg, 16+dpBG, 30) == "#":
			Animat.resetOnUpperPlatform(animat)

	if ay == 16:
		if dpBG >= 111:
			if Background.getChar(bg2,dpBG-111,14) == "#" and Animat.getFlyingMax(animat) == True:
				Animat.setOnUpperPlatform(animat)
				Animat.resetFlying(animat)
				Animat.onUpperPlatform(animat)
		elif Background.getChar(bg, 16+dpBG,14) == "#" and Animat.getFlyingMax(animat) == True:
			Animat.setOnUpperPlatform(animat)
			Animat.resetFlying(animat)
			Animat.onUpperPlatform(animat)		
	
	if ay == 16:
		if dpBG >=111:
			if Background.getChar(bg2, dpBG-111,14) == " " and Animat.getFlyingMax(animat) == True:
				Animat.resetOnUpperPlatform(animat)
				Animat.setFlying(animat)
				Animat.setFlyingMax(animat)
				Animat.jump(animat)								#Gere chute plateforme
		elif Background.getChar(bg, 16+dpBG, 14) == " " and Animat.getFlyingMax(animat)==True:
			Animat.resetOnUpperPlatform(animat)
			Animat.setFlying(animat)
			Animat.setFlyingMax(animat)
			Animat.jump(animat)	
			
def isData():
	pass

def interact():
	t = m.touch_status()
	if t & 1 and Animat.getY(animat) == 0:
		Animat.setFlying(animat)

def show():
	global dpBG
	lcd.fill(0)
	for y in range(len(bg["map"])):
		for x in range(dpBG,len(bg["map"][y])):
			if Background.getChar(bg,x,y) !=" ":
				lcd.pixel(x-dpBG,y,1)
				lcd.show()		
	
	for y in range(len(bg2["map"])):
		for x in range(0,dpBG):
			if Background.getChar(bg2,x,y) !=" ":
				lcd.pixel(x+128-dpBG,y,1)
				lcd.show()
				
	for y in range(len(animat["look"])):
		for x in range(len(animat["look"][y])):
			if Animat.getChar(animat, x, y) != " ":
				lcd.pixel(x,16+y-animat["y"],1)
				lcd.show()



def run():
	while 1:
		interact()
		move()
		show()
		time.sleep(timeStep)
		
		
def quitGame():
	pass
		

#########################################
init()
run()
quitGame()







#	lcd.pixel(127, 31, 1)          # draw the dot
#	lcd.show()                  # show the buffer
#def run():
#	lcd = pyb.LCD('X')
#	lcd.light(True)
#	m = mpr121.MPR121(pyb.I2C(1, pyb.I2C.MASTER))
#	a = dict()
#	a["look"] = []
#	myfile = open("level.txt","r")
#	chaine = myfile.read()
#	listeLignes = chaine.splitlines()
#	for line in listeLignes:
#		listeChar = list(line)
#		a["look"].append(listeChar)
#	myfile.close()
#	lcd.write(chaine)
#		
#run()