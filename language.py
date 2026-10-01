def language(t, T, s, S):
    english = 0
    french = 0
    for i in range(s and S):
        if s[i] == "s" and S[i] == "S":
            french = french = 1
    for i in range(t and T):
        if t[i] == "t" and T[i] == "T":
             english = english = 1
        if english > french:
            print("english")
        if french > english:
            print("french")
    return english and french
                                                                      
print(language("The red cat sat on the mat. Why are you so sad cat. Don't ask that."))
