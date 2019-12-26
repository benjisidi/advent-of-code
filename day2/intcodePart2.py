from intcodePart1 import runIntcode
from copy import copy


def runWithStatus(code1, code2, program):
    newProgram = copy(program)
    newProgram[1] = code1
    newProgram[2] = code2
    return runIntcode(newProgram)


def findStatus(program, targetValue, limitI=100, limitJ=100):
    for i in range(limitI):
        for j in range(limitJ):
            if (runWithStatus(i, j, program)[0] == targetValue):
                return [i, j]
    return [-1, -1]


if __name__ == "__main__":
    with open("./intcodeInput.txt", "r") as _input:
        intcode = [int(x) for x in _input.readline().split(',')]
        print(findStatus(intcode, 19690720))
