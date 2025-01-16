rows = 6
for i in range(1, rows + 1):
    # Cetak spasi untuk merapikan segitiga
    print(' ' * (rows - i), end='')
    # Cetak angka
    for a in range(i):
        print(i, end=' ')
    print()
