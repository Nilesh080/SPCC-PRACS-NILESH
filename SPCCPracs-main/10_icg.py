OPERATORS = {'+', '-', '*', '/', '(', ')'}
PRI = {'+': 1, '-': 1, '*': 2, '/': 2}

def infix_to_postfix(formula):
    stack = []
    output = ""
    for ch in formula:
        if ch not in OPERATORS:
            output += ch
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(' and PRI[ch] <= PRI[stack[-1]]:
                output += stack.pop()
            stack.append(ch)
    output += "".join(reversed(stack))
    return output

def generate3AC(pos):
    stack = []
    t = 1
    for i in pos:
        if i not in OPERATORS:
            stack.append(i)
        else:
            print(f"t{t} = {stack.pop(-2)} {i} {stack.pop()}")
            stack.append(f"t{t}")
            t += 1

expression = input("Enter the arithmetic expression: ") # x+y/z*w
pos = infix_to_postfix(expression)
print(f"Postfix expression: {pos}")
generate3AC(pos)