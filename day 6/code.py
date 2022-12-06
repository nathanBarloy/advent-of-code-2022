with open("input.txt") as f:
    signal = f.read()
    
    for i in range(14, len(signal)+1):
        if len(set(signal[i-14:i]))==14:
            print(i)
            break