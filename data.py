x = 3
y = float (3)
print(x,y)
values = [1,2.23,5,7,2,30,15]
print(values)

def spaces(n,y,t):
    occupied = 0
    for i in range(n):
        if y[i] == "C" and t[i] == "C":
            occupied = occupied = 1
    return occupied
print(spaces(6, "CC..C", ".CC.."))

                                                                                                                     