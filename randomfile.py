# create 3 lucky winner from names.txt file using Random.
import random
f = open("names.txt","r")
names = f.readlines()
winner =""
for i in range(3):
    win= random.choice(names)
    names.remove(win)
    winner += win
    

print(f"The lucky winners are below:\ncongratulations!\n{winner}")