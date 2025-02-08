def multiply(input_number_a,input_number_b):
    if input_number_b == 0:
        return 0
    elif input_number_b >=1:
        return input_number_a+ multiply(input_number_a,input_number_b-1)

print(multiply(3,3))