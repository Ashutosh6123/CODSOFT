import tkinter as tk

def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + str(number))

def button_clear():
    display.delete(0, tk.END)

def button_equal():
    try:
        expression = display.get()
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

root = tk.Tk()
root.title("Calculator")

display = tk.Entry(root, width=25, justify=tk.RIGHT)
display.grid(row=0, column=0, columnspan=4)

button_1 = tk.Button(root, text="1", command=lambda: button_click(1))
button_1.grid(row=1, column=0)

button_2 = tk.Button(root, text="2", command=lambda: button_click(2))
button_2.grid(row=1, column=1)

button_3 = tk.Button(root, text="3", command=lambda: button_click(3))
button_3.grid(row=1, column=2)

button_4 = tk.Button(root, text="4", command=lambda: button_click(4))
button_4.grid(row=2, column=0)

button_5 = tk.Button(root, text="5", command=lambda: button_click(5))
button_5.grid(row=2, column=1)

button_6 = tk.Button(root, text="6", command=lambda: button_click(6))
button_6.grid(row=2, column=2)

button_7 = tk.Button(root, text="7", command=lambda: button_click(7))
button_7.grid(row=3, column=0)

button_8 = tk.Button(root, text="8", command=lambda: button_click(8))
button_8.grid(row=3, column=1)

button_9 = tk.Button(root, text="9", command=lambda: button_click(9))
button_9.grid(row=3, column=2)

button_0 = tk.Button(root, text="0", command=lambda: button_click(0))
button_0.grid(row=4, column=1)

button_plus = tk.Button(root, text="+", command=lambda: button_click("+"))
button_plus.grid(row=1, column=3)

button_minus = tk.Button(root, text="-", command=lambda: button_click("-"))
button_minus.grid(row=2, column=3)

button_multiply = tk.Button(root, text="*", command=lambda: button_click("*"))
button_multiply.grid(row=3, column=3)

button_divide = tk.Button(root, text="/", command=lambda: button_click("/"))
button_divide.grid(row=4, column=3)

button_equal = tk.Button(root, text="=", command=button_equal)
button_equal.grid(row=4, column=2)

button_clear = tk.Button(root, text="C", command=button_clear)
button_clear.grid(row=4, column=0)

root.mainloop()