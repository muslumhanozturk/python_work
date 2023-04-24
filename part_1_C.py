# Sabitlerin tanımlanması
alpha = 1.09e3  # α değeri
rho = 0.33  # ρ değeri
e_squared = 14.4  # e^2 değeri

# Denklemin çözümü
from scipy.optimize import fsolve

def f(r):
    return (e_squared / r**2) - ((alpha / rho) * (e_squared ** (-r / rho)))

# Denklemi çözmek için başlangıç tahmini
initial_guess = 2.0  # başlangıç tahmini
bond_length, = fsolve(f, initial_guess)

# Sonucu ekrana yazdır
print("NaCl molekülündeki bağ uzunluğu: {:.4f} Å".format(bond_length))
