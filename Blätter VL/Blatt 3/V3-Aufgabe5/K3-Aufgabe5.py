def heron_wurzel(x,g): #x = zu bestimmende Zahl #g = startwert/schätzung
    d = abs(x - g)
    iteration = 1

    while d >= 0.000005 and iteration <=5:
        g = ((x/g+g)/2)
        print(f"Iteration {iteration}, Näherung {g}")
        iteration += 1

    print(f"Wurzel aus {x} ist näherungsweise {g}")

#(heron_wurzel(99,2))


def heron_wurzel_rek(x,g,iteration =1):
    d = abs(x-g)

    if d <= 0.000005 or iteration >5:
        print(f"Wurzel aus {x} ist näherungsweise {g}")
        return g
    
    g =((x/g+g)/2)
    print(f"Iteration {iteration}, Näherung {g}")
    return heron_wurzel_rek(x,g,iteration+1)

heron_wurzel_rek(99,2)