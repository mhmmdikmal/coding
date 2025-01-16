import pandas as pd
from tabulate import tabulate # tabulate untuk menambahkan tabel

# Membaca file CSV
df = pd.read_csv('C:\\Users\\ikmal\\Coding\\Python\\music.csv')

# Menampilkan DataFrame dengan tabulate
print(tabulate(df, headers='keys', tablefmt='psql'))