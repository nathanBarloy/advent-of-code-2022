f = open("input.txt")
raw = f.read()


# read the input and format it correctly

init_stacks, commands = raw.split("\n\n")
init_stacks = init_stacks.split("\n")
commands = commands.split("\n")

for i, x in enumerate(commands):
    a, b = x.split(" from")
    b, c = b.split(" to")
    a = int(a.split()[-1])
    b = int(b.split()[-1])-1
    c = int(c.split()[-1])-1

    commands[i] = (a, b, c)


nb_stack = int(init_stacks[-1].split()[-1])
init_stacks = init_stacks[:-1]
stacks = [[] for i in range(nb_stack)]

for line in init_stacks[::-1]:
    for i in range(nb_stack):
        x = line[4*i+1]
        if x != " ":
            stacks[i].append(x)


# manipulate the stacks

for nb, s1, s2 in commands:
    """ Code for first part
    for _ in range(nb):
        stacks[s2].append(stacks[s1].pop())
    """

    stacks[s2] += stacks[s1][-nb:]
    stacks[s1] = stacks[s1][:-nb]


# print the result

for x in stacks:
    print(x[-1], end="")


f.close()
