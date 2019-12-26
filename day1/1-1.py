import math


def getFuel(mass):
    return math.floor(mass/3) - 2


if __name__ == '__main__':
    with open("./1-1-input.txt", "r") as f:
        fuels = [getFuel(int(x)) for x in f.readlines()]
        print(sum(fuels))
