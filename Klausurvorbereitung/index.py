wort = "hallo"
print(wort.index("h"))

alphabet = "abcdefghijklmnopqrstuvwxyz"
print(alphabet.index("z"))

print("---")
for buchstabe in wort:
    print(f"{alphabet.index(buchstabe)+1} - {buchstabe}")