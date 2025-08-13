import tkinter as tk

def click(symbol):
    entry.insert(tk.END, symbol)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=20, font=('Arial', 18))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '+', '='
]

row_val = 1
col_val = 0

for btn in buttons:
    if btn == "=":
        tk.Button(root, text=btn, width=5, height=2, command=calculate).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=btn, width=5, height=2, command=lambda b=btn: click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

tk.Button(root, text="C", width=22, height=2, command=clear).grid(row=row_val, column=0, columnspan=4)

root.mainloop()
