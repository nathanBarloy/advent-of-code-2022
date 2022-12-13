from functools import cmp_to_key


with open("input.txt") as f:
    pairs = f.read().split("\n\n")
    pairs = list(map(lambda x: x.split("\n"), pairs))


def compare_packet(l1, l2):
    if isinstance(l1, int):
        if isinstance(l2, int):
            return -1 if l1 < l2 else (0 if l1 == l2 else 1)
        else:
            return compare_packet([l1], l2)
    if isinstance(l2, int):
        return compare_packet(l1, [l2])
    
    if len(l1) == 0:
        if len(l2) == 0:
            return 0
        return -1
    if len(l2) == 0:
        return 1
    
    test = compare_packet(l1[0], l2[0])
    if test != 0:
        return test
    
    return compare_packet(l1[1:], l2[1:])


def p1():
    tot = 0
    for i in range(len(pairs)):
        l1 = eval(pairs[i][0])
        l2 = eval(pairs[i][1])
        if compare_packet(l1, l2) == -1:
            tot += i+1

    print(tot)


def p2():
    packets = [x for pair in pairs for x in pair]
    packets = list(map(eval, packets))
    packets.append([[2]])
    packets.append([[6]])
    packets.sort(key=cmp_to_key(compare_packet))
    i2 = -1
    i6 = -1
    for i, x in enumerate(packets):
        if x == [[2]]:
            i2 = i+1
        if x == [[6]]:
            i6 = i+1
    print(i2*i6)

p2()