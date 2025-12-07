import tkinter as tk

def say_hi():
    label.config(text = 'hi prithwin welcome to GUI')

def clear_text():
    label.config(text='')

root = tk.Tk()
root.title('first gui')
root.geometry('500x400')
root.config(bg = "black")

button = tk.Button(root, text='click me', command=say_hi, bg='purple', fg='white')
button.pack(pady=20)

clear_button = tk.Button(root, text = 'clear', command=clear_text, bg='red', fg='white', font=('Arial', 12))
clear_button.pack(pady=10)

label = tk.Label(root, text='', font=('Arial', 24))
label.pack()

root.mainloop()
