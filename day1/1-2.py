import math


def getFuel(mass, totalFuel=0):
    requiredFuel = math.floor(mass/3) - 2
    if requiredFuel <= 0:
        return totalFuel
    else:
        return getFuel(requiredFuel, totalFuel + requiredFuel)
    return math.floor(mass/3) - 2


if __name__ == '__main__':
    with open("./1-1-input.txt", "r") as f:
        fuels = [getFuel(int(x)) for x in f.readlines()]
        print(sum(fuels))
