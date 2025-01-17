# say good morning to all friends from names.txt
f=open("names.txt","r")
names= f.readlines()
names = [name.strip() for name in names]
names = [name.title() for name in names]
# print(names)

def greet(names):
    for name in names:
        print(f"Hello Good Morning {name}.Have a nice day!")

greet(names)