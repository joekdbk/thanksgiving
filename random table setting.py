#not sure how many people we are going to have, so i'll make it work for anyamount of people
import random

people = []
name = " "
i = 0

while(name != "no"):
    print("What is your name? (If you are done entering names enter 'no')")
    name = input()
    if (name != "no"):
        people.append(name)

table = []

while(len(people) > 0):
    i = random.randrange(0, len(people), 1)
    x = people[i]
    table.append(x)
    people.pop(i)


print(people)
print(table)
i=1

for x in table:

    print("seat " + str(i) + " is " + str(x))
    i = i + 1







