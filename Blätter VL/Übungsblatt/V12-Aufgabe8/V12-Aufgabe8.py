import math

def rad_lin(v):
    step = 0.001
    schätzung = 0
    
    while abs((4/3)*(schätzung**3)*math.pi)-v <= step: #lieber mit abs() <= step/epsilon arbeiten anstatt () <= V
        schätzung+=step
    return schätzung

print(rad_lin(100))

def rad_bin(v):
    untereGrenze = 0
    obereGrenze = v
    epsilon = 0.001
    r = untereGrenze + (obereGrenze-untereGrenze)/2

    while abs((4/3)*(r**3)*math.pi-v) >= epsilon:
        if (4/3)*(r**3)*math.pi < v:
            untereGrenze = r
            #print(f"{untereGrenze};{obereGrenze} - {r}")
        else:
            obereGrenze = r
            #print(f"{untereGrenze};{obereGrenze} - {r}")

        r = untereGrenze + (obereGrenze-untereGrenze)/2
    return r

print(rad_bin(100))