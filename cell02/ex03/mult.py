#!/usr/bin/env python3

first_number = int(input("Enter the first number: \n"))
second_number = int(input("Enter the second number: \n"))

mult = first_number * second_number

print(f"{first_number} x {second_number} = {first_number * second_number}")

if mult > 0 :
    print("The result is positive.")
elif mult < 0 :
    print("The result is negative.")
else :
    print("The result is positive and negative.")