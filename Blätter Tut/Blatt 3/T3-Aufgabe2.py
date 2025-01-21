#2a
x = 0
y= 0
while x <= 10:
    while y<=10:
        print(f"{x} x {y} = {x*y}")
        y+=1
    x+=1
    y=0

#2b
x = 0
y= 0
while x <= 10:
    while y<=10:
        if x*y%2!=0:
            print(f"{x} x {y} = {x*y}")
        y+=1
    x+=1
    y=0