import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menangani setiap klik tombol
def button_click(value):
    current = entry_var.get()
    entry_var.set(current + str(value))

def clear_entry():
    entry_var.set("")

def calculate():
    try:
        expression = entry_var.get()
        if expression == "1+1":
            entry_var.set("1+1 masa gatau?")
        elif expression == "2+1":
            entry_var.set("😜")
        else:
            result = eval(expression)  # Evaluasi ekspresi matematika lainnya
            entry_var.set(result)
    except Exception as e:
        messagebox.showerror("Error", "Ekspresi tidak valid!")

# Membuat window utama
root = tk.Tk()
root.title("Ikmal")
root.geometry("400x500")
root.resizable(False, False)

# Variabel untuk menyimpan input pengguna
entry_var = tk.StringVar()

# Entry untuk menampilkan input dan hasil
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 24), bd=8, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Membuat tombol-tombol angka dan operasi
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('.', 4, 0), ('0', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Menambahkan tombol ke window
for (text, row, col) in buttons:
    action = lambda x=text: button_click(x) if x != '=' else calculate()
    tk.Button(root, text=text, width=5, height=2, font=("Arial", 18),
              command=action).grid(row=row, column=col, padx=5, pady=5)

# Tombol Clear
tk.Button(root, text='C', width=22, height=2, font=("Arial", 18),
          command=clear_entry).grid(row=5, column=0, columnspan=4, padx=5, pady=5)

# Menjalankan aplikasi
root.mainloop()
