import tkinter as tk
from tkinter import messagebox, ttk

def add_task():
    task = task_entry.get()
    if task:
        task_list.insert("", "end", values=(task, "Not Completed"), tags=("not_completed",))
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "masukin kegiatannya.")

def complete_task():
    selected_item = task_list.selection()
    if selected_item:
        task_list.item(selected_item, values=(task_list.item(selected_item)["values"][0], "Completed"), tags=("completed",))
        task_list.tag_configure("completed", background="light green")
    else:
        messagebox.showwarning("Warning", "pilih kegiatan yang udah beres.")

def delete_task():
    selected_item = task_list.selection()
    if selected_item:
        task_list.delete(selected_item)
    else:
        messagebox.showwarning("Warning", "pilih dulu kegiatannya.")

# Membuat jendela utama
root = tk.Tk()
root.title("Apa Yang Ingin Kamu Lakukan Hari Ini?")

task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

add_task_button = tk.Button(root, text="Tambah Kegiatan", command=add_task)
add_task_button.pack(pady=5)

# Membuat tabel menggunakan Treeview
task_list = ttk.Treeview(root, columns=("Kegiatan", "Status"), show="headings")
task_list.heading("Kegiatan", text="Kegiatan")
task_list.heading("Status", text="Status")
task_list.pack(pady=10)

delete_task_button = tk.Button(root, text="Hapus", command=delete_task)
delete_task_button.pack(pady=5)

complete_task_button = tk.Button(root, text="Complete Task", command=complete_task)
complete_task_button.pack(pady=5)

# Menjalankan aplikasi
root.mainloop()