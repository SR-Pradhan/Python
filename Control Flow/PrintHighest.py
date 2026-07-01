
marks = [90, 30, 100, 50, 80, 95]

highest = marks[0]

for i in marks:
    if(i >= highest):
        highest = i
    else:
        continue

print("Highest Mark", highest, sep=" ----> ")

# instead of this we can use, built in function
print(max(marks)) # for max mark
print(min(marks)) # for min mark

    