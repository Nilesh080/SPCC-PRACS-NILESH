intermediate_code = ""
with open("pass2.txt") as f:
  intermediate_code = f.read()

symbol_table = {
    'X': '200',
    'LOOP': '300'
}
symTabAddrs = list(symbol_table.values())

literal_table = {
    '=5': '350',
    '=10': '600'
}
litTabAddrs = list(literal_table.items())

lines = intermediate_code.split("\n")
for line in lines:
    elements = line.split(",")
    output = []
    for element in elements:
        if '(' in element:
            entry_type, entry_value = element.strip('()').split()
            if entry_type == 'S': output.append(symTabAddrs[int(entry_value)-1])
            elif entry_type == 'L': output.append(litTabAddrs[int(entry_value)-1][1])
            output.append(entry_value)
        else:
            output.append(element)
    print(', '.join(output))

for i in range(len(litTabAddrs)):
      print(f"{litTabAddrs[i][1]}, {litTabAddrs[i][0]}")