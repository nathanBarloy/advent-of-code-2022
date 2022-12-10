
with open("input.txt") as f:
    lines = list(map(lambda x: x.split(), f.readlines()))


def p1():
    
    values = [1]
    x = 1
    for line in lines:
        if line[0] == "addx":
            values.append(x)
            values.append(x)
            x += int(line[1])
        
        elif line[0] == "noop":
            values.append(x)
        
        else:
            print("Unknown command")
    
    res = 0
    for i in range(20, len(values), 40):
        res += values[i] * i
    
    print(res)


def p2():
    
    screen = []
    clock = 0
    x = 1
    for line in lines:

        if line[0] == "addx":
            if x-1 <= clock % 40 <= x+1:
                screen.append("#")
            else:
                screen.append(".")
            clock += 1
            if x-1 <= clock % 40 <= x+1:
                screen.append("#")
            else:
                screen.append(".")
            clock += 1
            x += int(line[1])

        elif line[0] == "noop":
            if x-1 <= clock % 40 <= x+1:
                screen.append("#")
            else:
                screen.append(".")
            clock += 1
        
        else:
            print("Unknown command")
    
    for i in range(0, len(screen), 40):
        print("".join(screen[i:i+40]))

p2()
