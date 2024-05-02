intermediate_code = '''100,(IS 04),(S 1),1
101,(IS 01),2,3
102,(IS 00)'''

symbol_table = {
    'X': '200',
    'LOOP': '300'
}

literal_table = {}

def get_address(entry):
    if entry[0] == 'S':
        return symbol_table.get(entry[1], '')
    elif entry[0] == 'L':
        return literal_table.get(entry[1], '')
    else:
        return entry

lines = intermediate_code.split("\n")
for line in lines:
    elements = line.split(",")
    output = []
    for element in elements:
        if '(' in element:
            entry_type, entry_value = element.strip('()').split()
            output.append(entry_value)
        else:
            output.append(element)
    print(', '.join(output))
