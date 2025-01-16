# list ini menggunakan kata e_list dan item
# fungsi e_list dan item adalah untuk membuat list lebih rapih
todolist = ["bangun tidur ","mandi ","makan ", "ngoding ."]
e_list = enumerate(todolist, start = 1)
for item in e_list:
    print(item)