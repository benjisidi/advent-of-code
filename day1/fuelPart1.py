import math


def getFuel(mass):
    return math.floor(mass/3) - 2


if __name__ == '__main__':
    with open("./fuelInput.txt", "r") as f:
        fuels = [getFuel(int(x)) for x in f.readlines()]
        print(sum(fuels))
