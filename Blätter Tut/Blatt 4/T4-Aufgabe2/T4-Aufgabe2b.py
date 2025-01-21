def rechnen(x,y):
    add = x+y
    sub = x-y
    return add,sub

add_ergebnis,sub_ergebnis=rechnen(
    int(input("x eingeben: ")),
    int(input("y eingeben: "))
)
print(f"Addition: {add_ergebnis}, Subtraktion: {sub_ergebnis}")