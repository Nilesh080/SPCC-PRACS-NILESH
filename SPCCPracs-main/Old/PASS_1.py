def pass1(assembly_code):
    symbol_table = {}
    literal_table = {}
    litlist = []
    location_counter = 0
    lines = assembly_code.split('\n')
    for line in lines:
        parts = line.split()
        label = None
        opcode = None
        operand = None
        if len(parts) == 3:
            label = parts[0]
            opcode = parts[1]
            operand = parts[2]
        elif len(parts) == 2:
            opcode = parts[0]
            operand = parts[1]
        if label:
            symbol_table[label] = location_counter
        if opcode:
            if opcode == 'START' or opcode == 'ORG':
                location_counter = int(operand)
            elif opcode == 'DS':
                location_counter += int(operand)
            else:
                location_counter += 1
            if operand.startswith('='):
                literal = operand
                if literal not in litlist:
                    litlist.append(operand)
    for lit in litlist:
        if lit not in literal_table:
            literal_table[lit] = location_counter
            location_counter += 1

    print("Symbol Table:")
    for symbol, address in symbol_table.items():
        print(f"{symbol}: {address}")

    print("\nLiteral Table:")
    for literal, address in literal_table.items():
        print(f"{literal}: {address}")

assembly_code = """
FIRST   START 100
        LDA   ='10'
        STA   ALPHA
FIVE    DC    5
ALPHA   DS    5
        END
"""
pass1(assembly_code)