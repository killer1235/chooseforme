import random 

nofchoices = input("Enter amount of choices.\n")

choices = []
for i in range(0,int(nofchoices)):
    c = input(f'Choice {i+1} is ')

    choices.append(c)

print(random.choice(choices))