#A =r^2 * pi

import math

def radius_linear(A):
    schrittgröße = 0.01
    radius = 0
    iteration = 0
    while (radius**2)*math.pi <= A:
        iteration +=1
        radius += schrittgröße
        print(f"Iteration {iteration}: {radius}")
    return radius

print(radius_linear(5))

def radius_binär(A):
    epsilon = 0.01
    iteration = 0

    unteresLimit = 0
    oberesLimit = A

    näherung = unteresLimit + (oberesLimit-unteresLimit)/2
    while abs(((näherung**2)*math.pi)-A) >= epsilon:
        iteration +=1
        print(f"Iteration {iteration}: [{unteresLimit};{oberesLimit}]: {näherung}")

        if näherung**2*math.pi < A:
            unteresLimit = näherung
        else:
            oberesLimit = näherung
        näherung = unteresLimit + (oberesLimit-unteresLimit)/2
    return näherung

print(radius_binär(5))

#Linear benötigt 127; Binär nur 10 -> Damit Binär deutlich effizienter