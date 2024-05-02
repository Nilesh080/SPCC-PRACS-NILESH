instructions = {
    "+": "ADD",
    "-": "SUB",
    "*": "MUL",
    "/": "DIV"
}

def generateTargetCode(tac):
    i = 0
    for line in tac:
        if(len(line) == 4):
            print(f"MOV R{i}, {line[1]}")
            print(f"{instructions[line[3]]} R{i}, {line[2]}")
            print(f"MOV {line[0]}, R{i}")
            i = i + 1
        else:
            print(f"MOV {line[0]}, {line[1]}")

tac = [
    ["t1", "a", "b", "+"],
    ["t2", "c", "d", "/"],
    ["t3", "t1", "t2", "-"],
    ["r", "t3"]
]
generateTargetCode(tac)

"""
    The TAC given as input is:
        t1 = a + b
        t2 = c / d
        t3 = t1 - t2
        r = t3
"""