from random import *
from math import sqrt

def getPi(numberOfPoints):
	LessThanOne = 0
	for i in range(0,numberOfPoints):
		x = random()
		y = random()
		distance = x**2 + y**2
		if(distance<1):
			LessThanOne+=1
	return 4*LessThanOne/numberOfPoints

print(getPi(10000000))