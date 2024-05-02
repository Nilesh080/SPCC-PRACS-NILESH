def pass1ST(fileName):
  lines = []
  symbol_table = {}
  LC = 0
  with open(fileName) as f:
    lines = f.readlines()
  for line in lines:
    label = None
    opcode = None
    operand = None
    parts = line.split()
    if len(parts) == 3:
      label = parts[0]
      opcode = parts[1]
      operand = parts[2]
    elif len(parts) == 2:
      opcode = parts[0]
      operand = parts[1] 
    if label:
      symbol_table[label] = LC
    if opcode:
      if opcode == "START" or opcode == "ORG":
        LC = int(operand)
      elif opcode == "DS":
        LC += int(operand)
      else:
        LC += 1
  return symbol_table

ST = pass1ST("pass1.txt")
print(f"Symbol Table: {ST}")