def pass1LT(fileName):
  lines = []
  literal_table = {}
  litlist = []
  LC = 0
  with open(fileName) as f:
    lines = f.readlines()
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
      if opcode:
          if opcode == 'START' or opcode == 'ORG':
              LC = int(operand)
          elif opcode == 'DS':
              LC += int(operand)
          else:
              LC += 1
          if operand.startswith('='):
              literal = operand
              if literal not in litlist:
                  litlist.append(operand)
  for lit in litlist:
      if lit not in literal_table:
          literal_table[lit] = LC
          LC += 1 
  return literal_table

LT = pass1LT("pass1.txt")
print(f"Literal Table: {LT}")