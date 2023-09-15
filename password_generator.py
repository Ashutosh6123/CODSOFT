import string
import tkinter as tk
from tkinter import messagebox
import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def main():
    try:
        desired_length = int(display1.get())
        if desired_length <= 0:
            messagebox.showinfo("Error", "Password length must be a positive integer")
        else:
            password = generate_password(desired_length)
            display2.delete(0, tk.END)
            display2.insert(tk.END, password)
    except ValueError:
        messagebox.showinfo("Error", "Please enter a valid positive integer")
def accept():
    messagebox.showinfo("Success!", "Password Generated")
def reset():
    display2.delete(0, tk.END)
root = tk.Tk()
root.title("Password Generator")
label1 = tk.Label(root, text="Password Generator", bg="blue")
label1.grid(row=0, column=3)
label2 = tk.Label(root, text="Enter User Name :")
label2.grid(row=2, column=0)
display = tk.Entry(root)
display.grid(row=2, column=1, columnspan=4)
label3 = tk.Label(root, text="Enter Password Length :")
label3.grid(row=3, column=0)
display1 = tk.Entry(root)
display1.grid(row=3, column=1, columnspan=4)
label4 = tk.Label(root, text="Generated Password :")
label4.grid(row=4, column=0)
display2 = tk.Entry(root, justify=tk.RIGHT)
display2.grid(row=4, column=1, columnspan=4)
button1 = tk.Button(root, text="Generate Password", command=main)
button1.grid(row=5, column=3)
button2 = tk.Button(root, text="ACCEPT", command=accept)
button2.grid(row=6, column=3)
button3 = tk.Button(root, text="RESET", command=reset)
button3.grid(row=7, column=3)
root.mainloop()