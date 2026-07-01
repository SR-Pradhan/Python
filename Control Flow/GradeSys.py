# We have to assign Grade to Student acc. to his/her mark

print("Enter Mark: ",end="")
mark = int(input())

if mark >= 90 and mark <= 100:
    print("Grade A")
elif mark >= 80 and mark < 90:
    print("Grade B")
elif mark >= 70 and mark < 80:
    print("Grade C")
elif mark >= 60 and mark < 70:
    print("Grade C")
else:
    print("Grade E")