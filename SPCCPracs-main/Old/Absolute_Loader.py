def load_program(memory, lines):
    for line in lines:
        parts = line.strip().split('\t')
        if parts[0] == 'T':
            address = int(parts[1], 16)
            length = int(parts[2], 16)
            data = ''.join(parts[3:])
            for i in range(0, length * 2, 2):
                byte_str = data[i:i+2]
                if byte_str:
                    memory[address] = int(byte_str, 16)
                address += 1

def read_input_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines

memory_size = 0xFFFFF
memory = [0] * memory_size
input_file = input("Enter the name of the file: ")
input_data = read_input_file(input_file)
load_program(memory, input_data)
print("Memory address\t\tcontent")
for i in range(len(memory)):
    if memory[i] != 0:
        print(f"{hex(i)[2:].zfill(6).upper()}\t\t\t{memory[i]:02X}")