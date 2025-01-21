def bmi(gewicht,groesse):
    bmi = gewicht/(groesse**2)
    print(f"Der BMI liegt bei {bmi:>.2f}.")

bmi(
    int(input("Gewicht in kg: ")),
    float(input("Größe in m: "))
)