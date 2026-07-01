# Nested If-Else

print("Enter Your Age: ",end="")
age = int(input())

if age > 18:
    if age >= 65:
        print("Take Rest")
    else:
        print("You are eligible")
else:
    print("You are not eligible")