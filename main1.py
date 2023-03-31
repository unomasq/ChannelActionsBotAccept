from tkinter import *
from tkinter import ttk

def calculate():
    a = int(entry.get())
    b = int(entry1.get())
    c = int(entry2.get())
    d = int(entry3.get())
    if rb_var.get() == 0:
        f = a*c/b*d
        operation = "Умножение"
        label["text"] = f
        operation_label["text"] = operation

    elif rb_var.get() == 1:
        f = a*d/b*c
        operation = "Деление"
        label["text"] = f
        operation_label["text"] = operation
    else:
        f = 0
        operation = ""

   

root = Tk()
root.title("Math")
root.geometry("700x500")

rb_var = IntVar()
rb_var.set(0)

r = Radiobutton(root, text="Умножение", variable=rb_var, value=0)
r.grid(row=2, column=8)

r1 = Radiobutton(root, text="Деление", variable=rb_var, value=1)
r1.grid(row=2, column=9)

label1 = Label(root, text="Знаменатель:")
label1.grid(row=2, column=4)

label2 = Label(root, text="Числитель:")
label2.grid(row=3, column=4)

label3 = Label(root, text="Знаменатель:")
label3.grid(row=2, column=6)

label4 = Label(root, text="Числитель:")
label4.grid(row=3, column=6)

entry = ttk.Entry(root, width=13)
entry.grid(row=2, column=5)

entry1 = ttk.Entry(root, width=13)
entry1.grid(row=3, column=5)

entry2 = ttk.Entry(root, width=13)
entry2.grid(row=2, column=7)

entry3 = ttk.Entry(root, width=13)
entry3.grid(row=3, column=7)

btn = ttk.Button(root, text="Выполнить", width=13, command=calculate)
btn.grid(row=6, column=6)

label = ttk.Label(root, text="")
label.grid(row=5, column=6)

operation_label = ttk.Label(root, text="")
operation_label.grid(row=4, column=6)

root.mainloop()
