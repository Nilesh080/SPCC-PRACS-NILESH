def load_program(memory, lines):
    for line in lines:
        parts = line.strip().split('\t')
        if parts[0] == 'T':
            address, length = int(parts[1], 16), int(parts[2], 16)
            data = ''.join(parts[3:])
            memory[address:address+length] = [int(data[i:i+2], 16) for i in range(0, length*2, 2)]

memory_size = 0xFFFFF
memory = [0] * memory_size
with open("object.txt") as f:
  load_program(memory, f)
print("Memory address\t\tcontent")
for i, content in enumerate(memory):
    if content != 0:
        print(f"{i:06X}\t\t\t{content:02X}")