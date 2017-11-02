import pyb
lcd = pyb.LCD('X')

def create(filename):
	bg = dict()
	bg["map"] = []
	myfile = open(filename)
	chaine = myfile.read()
	listeLignes = chaine.splitlines()
	for line in listeLignes:
		listeChar = list(line)
		bg["map"].append(listeChar)
	myfile.close()
	return bg
	
def getChar(bg,x,y):
	return bg["map"][y][x]
	
	
def show(bg):
	for y in range(len(bg["map"])):
		for x in range(len(bg["map"][y])):
			if getChar(bg,x,y) !=" ":
				lcd.pixel(x,y,1)
				lcd.show()
				
			