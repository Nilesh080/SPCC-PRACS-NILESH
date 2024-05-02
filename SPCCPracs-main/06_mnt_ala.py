def generate_mnt_ala(alp):
    mnt = {}
    ala = {}
    macro_name = None
    parameters = []
    for line in alp.split('\n'):
        if line.startswith('MACRO'):
            parts = line.split()
            macro_name = parts[1]
            parameters = parts[2:]
            ala[macro_name] = parameters
            mnt[macro_name] = len(parameters)
    return mnt, ala

alp2 = ""
with open("macro2.txt") as f:
  alp2 = f.read()
mnt, ala = generate_mnt_ala(alp2)

print("Macro Name Table (MNT):\nMacro Name\t#Parameters")
for macro, params in mnt.items():
    print(f"{macro}\t\t{params}")

print("\nArgument List Array (ALA):\nMacro Name\tArguments")
for macro_name, params in ala.items():
    print(f"{macro_name}\t\t{params}")