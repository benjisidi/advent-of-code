import math
def getFuel(mass):
	return math.floor(mass/3) - 2

with open("./1-1.txt", "r") as f:
	fuels = [getFuel(int(x)) for x in f.readlines()]
	print sum(fuels)