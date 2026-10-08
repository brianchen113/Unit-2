def language(n, s, S, t, T):
    english = 0
    french = 0
    for i in range(n):
        if n[i] == "s" and n[i] == "S":
            french = french = 1
    for i in range(n):
        if n[i] == "t" and n[i] == "T":
             english = english = 1
        if english > french:
            print("english")
        if french > english:
            print("french")
    return english and french  
input("The red cat sat on the mat. Why are you so sad cat? Don't ask that.")                                   
                                                                                             