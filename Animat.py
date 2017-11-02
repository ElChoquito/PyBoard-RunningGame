#!/usr/bin/python

import pyb
lcd = pyb.LCD('X')

def test():
	lcd.write("ATest")
	
def create(filename,y):
	a = dict()
	a["look"] = []
	a["y"] = y
	a["flying"] = False
	a["onUpperPlatform"] = False
	a["flyingMax"] = False
	a["falling"]= False
	a["score"] = 0
	myfile = open(filename)
	chaine = myfile.read()
	listeLignes = chaine.splitlines()
	for line in listeLignes:
		listeChar = list(line)
		a["look"].append(listeChar)
	myfile.close()
	return a


def getChar(a,x,y):
	return (a["look"][y][x])

def getY(a):
	return a["y"]
def setY(a,b):
	a["y"] = b
	
def getFlying(a):
	return a["flying"]
def setFlying(a):
	a["flying"] = True
def resetFlying(a):
	a["flying"] = False

def getOnUpperPlatform(a):
	return a["onUpperPlatform"]
def setOnUpperPlatform(a):
	a["onUpperPlatform"] = True
def resetOnUpperPlatform(a):
	a["onUpperPlatform"] = False

def setFalling(a): 
	a["falling"] = True
def getFalling(a):
	return a["falling"]
def resetFalling(a):
	a["falling"] = False

def getFlyingMax(a):
	return a["flyingMax"]
def setFlyingMax(a):
	a["flyingMax"] = True
def resetFlyingMax(a):
	a["flyingMax"] = False
	
	
def show(a):
	for y in range(len(a["look"])):
		for x in range(len(a["look"][y])):
			if getChar(a, x, y) != " ":
				lcd.pixel(x,8+y+getY(a),1)
				lcd.show()


def jump(a):
	if getFlying(a) == True and getOnUpperPlatform(a)==True:
				resetFlyingMax(a)
				resetOnUpperPlatform(a)
	if getFlying(a) == True and getFlyingMax(a) == False and getY(a) !=18 and getOnUpperPlatform(a) == False:
		setY(a,getY(a)+4)
	if getY(a) == 20:
		setFlyingMax(a)
	if getFlying(a) == True and getFlyingMax(a) == True and getY(a) !=0:
		setY(a,getY(a)-2)
	if getY(a) == 0:
		resetFlying(a)
		resetFlyingMax(a)
	
def fall(a):
	setY(a, -5)
	#FIN DU JEU


def onUpperPlatform(a):
	if getOnUpperPlatform(a) == True:
		setY(a, 16)	
					