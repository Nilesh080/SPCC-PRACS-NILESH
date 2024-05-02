pos = 0

def consume(string):
    global pos
    pos+=1
    return string[pos-1]

def A(string):
    c = consume(string)
    if(c == 'c'):
        if(consume(string) == 'd'):
            return
        else:
            print("ERROR!!!")
        exit()
    elif(c == 'd'):
        return
    else:
        print("ERROR!!!")
        exit()

def S(string):
    global pos
    if(consume(string) == 'a'):
        A(string)
        if consume(string) == 'b':
            return
        else:
            print("ERROR!!!")
            exit()
    elif(string[pos-1] == 'c'):
        return
    else:
        print("ERROR!!!")
        exit()

string = input("Enter the string to parse: ")
S(string)
if(pos != len(string)):
    print("ERROR!!! Unparsed Input remains.")
    exit()
else:
    print("Input Parsed Successfully.")