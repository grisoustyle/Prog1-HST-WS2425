def multiply(input_number_a,input_number_b):
    if input_number_b == 0:
        return 0
    elif input_number_b >=1:
        return input_number_a+ multiply(input_number_a,input_number_b-1)

print(multiply(3,3))

'''rekursive algorithmen rufen sich selbst auf um ein problem schrittweise zu lösen.
die funktionen rufen sich so lange erneut auf bis eine abbruchbedingung erreicht ist.
vorteil ist meist weniger schreibaufwand beim code - rekursiv ist relativ schlank je nach formel
nachteil ist hoher speicherverbrauch durch ständig erneute aufrufung und finale ausrechnung erst am ende; code schwerer nachvollziehbar''' 