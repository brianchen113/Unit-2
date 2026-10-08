def wizard(N, start, duels):
    owner = start
    num_owners= 1
    for i in range(N):
        if duels[0][1] == owner:
            owner = duels[0][0]
            num_owners += 1                                        
    print(owner)

wizard(3, "A", ["BA", "CB", "DA"])
