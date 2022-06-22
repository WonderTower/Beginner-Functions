from math import sqrt


a_value = int(input("Value of a: "))
b_value = int(input("Value of b: "))
c_value = int(input("Value of c: "))

result = (-b_value + sqrt(b_value**2 - 4 * a_value * c_value)) / (2 * a_value)

print(f"The roots are {(-b_value + sqrt(b_value**2 - 4 * a_value * c_value)) / (2 * a_value)} and "
      f"{(-b_value - sqrt(b_value**2 - 4 * a_value * c_value)) / (2 * a_value)}")