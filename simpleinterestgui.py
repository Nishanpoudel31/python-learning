import tkinter as tk
def simple_interest_calculator():
    principal = float(textbox1.get())
    rate = float(textbox2.get())
    time= float(textbox3.get())
    simple_interest = (principal*rate*time)/100
    result_label.config(text=f"The simple interest of your amount is Rs.{simple_interest}")


root = tk.Tk()
root.title("Simple Interest Calculator By Nishan.")
root.geometry("550x450")

label1= tk.Label(root,text="Enter principal Amount: ")
label1.pack()
textbox1 = tk.Entry(root)
textbox1.pack()
label2= tk.Label(root,text="Enter Rate of Interest: ")
label2.pack()
textbox2 = tk.Entry(root)
textbox2.pack()
label3= tk.Label(root,text="Enter Time of Interest: ")
label3.pack()
textbox3 = tk.Entry(root)
textbox3.pack()
button1 =tk.Button(root,text="Calculate",command=simple_interest_calculator)
button1.pack()
result_label =tk.Label(root,text="")
result_label.pack()
root.mainloop()