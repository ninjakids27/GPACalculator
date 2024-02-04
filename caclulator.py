import tkinter as ttk
### Varibles ###
frame = ttk.Tk()
entry_var1 = ttk.StringVar()
entry_var2 = ttk.StringVar()
int1 = ttk.Entry(frame, width=40, bg="light blue",textvariable=entry_var1).pack()
int2 = ttk.Entry(frame, width=40, bg="light blue",textvariable=entry_var2).pack()
### caclulator function ###
def add():
    num1 = entry_var1.get()
    num2 = entry_var2.get()
    result = num1 + num2
    print(result)
frame.title("Calculator")

button = ttk.Button(frame, text="Add", command=add()).pack()


ttk.mainloop()
