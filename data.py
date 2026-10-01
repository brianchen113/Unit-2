x = 3
y = float (3)
print(x,y)
values = [1,2.23,5,7,2,30,15]
print(values)


tip_amount = input("How was your service? (bad, okay, good, great) ")
if tip_amount == "bad":
    print("0% tips")
if tip_amount == "okay":
    print("15 tip")
if tip_amount == "good":
    print("20%")
if tip_amount == ("great"):
    print("give me a 25% tip")
if tip_amount == "horrible":
    print("50% tip")

n = input("Choose a number from 1 to 16. ")
if n == "1":
    print("factors are 1")
if n == "2":
    print("factors are 1 and 2")
if n == "3":
    print("factors are 1 and 3")
if n == "4":
    print("factors are 1, 2, and 4")
if n == "5":
    print("factors are 1 and 5")
if n == "6":
    print("factors are 1, 2, 3, and 6")
if n == "7":
    print("factors are 1 and 7")
if n == "8":
    print("factors are 1, 2, 4, and 8")
if n == "9":
    print("factors are 1, 3, and 9")
if n == "10":
    print("factors are 1, 2, 5, and 10")
if n == "11":
    print("factors are 1 and 11")
if n == "12":
    print("factors are 1, 2, 3, 4, 6, 12")
if n == "13": 
    print("factors are 1 and 13")                                  
if n == "14":
    print("factors are 1, 2, 7, and 14") 
if n == "15":
    print("factors are 1, 3, 5, and 15")
if n == "16":
    print("factors are 1, 2, 4, 8, 16")
if n == "17":
    print("factors are 1 and 17")

def spaces(n,y,t):
    occupied = 0
    for i in range(n):
        if y[i] == "C" and t[i] == "C":
            occupied = occupied = 1
    return occupied
print(spaces(6, "CC..C", ".CC.."))