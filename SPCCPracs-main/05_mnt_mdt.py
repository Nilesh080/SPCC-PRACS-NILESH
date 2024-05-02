def generate_mnt_mdt(alp):
    mnt = {}
    mdt = {}
    macro_name = None
    parameters = []
    inside_macro = False
    for line in alp.split('\n'):
        if line.startswith('MACRO'):
            parts = line.split()
            macro_name = parts[1]
            parameters = parts[2:]
            mnt[macro_name] = len(parameters)
            mdt[macro_name] = []
            inside_macro = True
        elif line.startswith('MEND'):
            inside_macro = False
        elif inside_macro:
            mdt[macro_name].append(line)
    for macro_name in mdt:
        mdt[macro_name].append("MEND")
    return mnt, mdt

alp = ""
with open("macro1.txt") as f:
  alp = f.read()

mnt, mdt = generate_mnt_mdt(alp)

print("Macro Name Table (MNT):\nMacro Name\t#Parameters")
for macro, params in mnt.items():
    print(f"{macro}\t\t{params}")

print("\nMacro Definition Table (MDT):\nMacro Name\tDefinition")
for macro, definition in mdt.items():
    print(f"{macro}\t\t{definition}")