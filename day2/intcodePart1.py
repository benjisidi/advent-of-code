def performOp(program, pointer):
    op = program[pointer]
    if (op == 99):
        return [program, -1]
    [arg1, arg2, target] = program[pointer+1:pointer+4]
    if (op == 1):
        program[target] = program[arg1] + program[arg2]
    elif(op == 2):
        program[target] = program[arg1] * program[arg2]
    pointer += 4
    return [program, pointer]


def runIntcode(program):
    pointer = 0
    while(pointer >= 0):
        [program, pointer] = performOp(program, pointer)
    return program


if __name__ == '__main__':
    with open("./intcodeInput.txt", "r") as _input:
        intcode = [int(x) for x in _input.readline().split(',')]
        programResult = runIntcode(intcode)
    print(programResult[0])
