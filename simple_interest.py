#welcome to interest calculator
principal = float(input("enter the principal amount: "))

rate = float(input("enter the rate of interet:  "))
time = float(input("enter the time of interest: "))

simple_interest = (principal * rate * time) /100
print(f"simple_interest is {simple_interest}")