import math

# xtanx - 1 = 0 fonksiyonu
def f1(x):
    return x * math.tan(x) - 1

# e^x - x^2 + 3x - 2 = 0 fonksiyonu
def f2(x):
    return math.exp(x) - x**2 + 3*x - 2

# Interval Halving (Aralık Bölme) yöntemi
def interval_halving(f, a, b, epsilon=1e-6, max_iter=100):
    iter_count = 0
    while abs(b - a) > epsilon and iter_count < max_iter:
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iter_count += 1
    return (a + b) / 2

# Sekant yöntemi
def secant(f, x0, x1, epsilon=1e-6, max_iter=100):
    iter_count = 0
    while abs(x1 - x0) > epsilon and iter_count < max_iter:
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x0 = x1
        x1 = x2
        iter_count += 1
    return x1

# Newton-Raphson yöntemi
def newton_raphson(f, f_prime, x0, epsilon=1e-6, max_iter=100):
    iter_count = 0
    while abs(f(x0)) > epsilon and iter_count < max_iter:
        x1 = x0 - f(x0) / f_prime(x0)
        x0 = x1
        iter_count += 1
    return x1

# xtanx - 1 = 0 fonksiyonunun [0, 1] aralığındaki kökleri
print("xtanx - 1 = 0 fonksiyonunun [0, 1] aralığındaki kökü (Aralık Bölme yöntemi):", interval_halving(f1, 0, 1))
print("xtanx - 1 = 0 fonksiyonunun [0, 1] aralığındaki kökü (Sekant yöntemi):", secant(f1, 0.1, 0.9))
print("xtanx - 1 = 0 fonksiyonunun [0, 1] aralığındaki kökü (Newton-Raphson yöntemi):", newton_raphson(f1, lambda x: x * (1 + math.tan(x)**2), 0.5))

# e^x - x^2 + 3x - 2 = 0 fonksiyonunun [0, 1] aralığındaki kökleri
print("e^x - x^2 + 3x - 2 = 0 fonksiyonunun [0, 1] aralığındaki kökü (Aralık Bölme yöntemi):", interval_halving(f2, 0, 1))
print("e^x - x^2 + 3x - 2 = 0 fonksiyonunun [0, 1] aralığındaki kökü (Sekant yöntemi):", secant(f2, 0.1, 0.9))
print("e^x - x^2 + 3x - 2 = 0 fonksiyonunun [0, 1] aralığındaki kökü (Newton-Raphson yöntemi):", newton_raphson(f2, lambda x: math.exp(x) - 2*x + 3, 0.5))

