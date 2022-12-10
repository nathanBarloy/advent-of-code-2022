with open("input.txt") as f:
    signal = f.read()
    
    #n = 4
    n = 14

    for i in range(n, len(signal)+1):
        if len(set(signal[i-n:i]))==n:
            print(i)
            break