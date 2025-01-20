#CREATE PROgram that display number is even or odd
def even_odd(num):
    if num %2==0:
        print(f"The number {num} you have entered is even.")

    else:
        print(f"The number {num} you have entered is odd.")

even_odd(num=int(input("enter here: ")))

