import numpy as np
import matplotlib.pyplot as plt

# Fungsi dan fungsi invers
def f(x):
    return 2 * x + 3

def f_inv(x):
    return (x - 3) / 2

# Data untuk plotting
x = np.linspace(-10, 10, 400)

# Membuat plot
plt.figure(figsize=(8, 8))
plt.plot(x, f(x), label=r'$f(x) = 2x + 3$', color='b')
plt.plot(x, f_inv(x), label=r'$f^{-1}(x) = \frac{x - 3}{2}$', color='g')
plt.plot(x, x, label='$y = x$', color='r', linestyle='--')  # Garis y = x sebagai referensi

# Menambahkan detail grafik
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.legend(loc='upper left')
plt.title('Grafik Fungsi dan Fungsi Invers')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

# Menampilkan grafik
plt.show()
