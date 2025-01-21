def multiplikation_iterativ(var_a, var_b):
    result = 0

    while var_b > 0:
        result += var_a
        var_b -= 1

    return result



def multiplikation_rekursiv(var_a, var_b):
    if var_b == 1:
        return var_a
    else:
        return var_a + multiplikation_rekursiv(var_a, var_b-1)
    
print(multiplikation_rekursiv(var_a=int(input("A: ")),var_b=(int(input("B: ")))))