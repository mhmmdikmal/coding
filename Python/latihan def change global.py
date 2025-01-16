#CARA MEMBUAT DEF CHANGE ITU MENGGUNAKAN KATA GLOBAL

x = 20
def change():
    global x
x = x + 10
change()
print("angka pertambahan ini adalah: ", x)