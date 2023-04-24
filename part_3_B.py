import math

# Diferansiyel denklem sistemi fonksiyonları
def f1(x, y1, y2):
    return y1 * y2

def f2(x, y1, y2):
    return math.exp(x) - 2 * y2 + y1

# Runge-Kutta yöntemi ile diferansiyel denklem sistemi çözümü
def runge_kutta(f1, f2, x0, y10, y20, h, n):
    x = x0
    y1 = y10
    y2 = y20
    print("x = {:.1f}, y1 = {:.6f}, y2 = {:.6f}".format(x, y1, y2))  # Başlangıç değerleri
    for i in range(n):
        k1y1 = h * f1(x, y1, y2)
        k1y2 = h * f2(x, y1, y2)
        k2y1 = h * f1(x + h/2, y1 + k1y1/2, y2 + k1y2/2)
        k2y2 = h * f2(x + h/2, y1 + k1y1/2, y2 + k1y2/2)
        k3y1 = h * f1(x + h/2, y1 + k2y1/2, y2 + k2y2/2)
        k3y2 = h * f2(x + h/2, y1 + k2y1/2, y2 + k2y2/2)
        k4y1 = h * f1(x + h, y1 + k3y1, y2 + k3y2)
        k4y2 = h * f2(x + h, y1 + k3y1, y2 + k3y2)

        y1 = y1 + (k1y1 + 2 * k2y1 + 2 * k3y1 + k4y1) / 6
        y2 = y2 + (k1y2 + 2 * k2y2 + 2 * k3y2 + k4y2) / 6
        x = x + h
        print("x = {:.1f}, y1 = {:.6f}, y2 = {:.6f}".format(x, y1, y2))  # Çözüm değerleri

# Diferansiyel denklem sistemi için başlangıç değerleri ve adım h
x0 = 0
y10 = 1
y20 = -1
h = 0.1
n = 10

# Diferansiyel denklem sistemi çözümü
print("Diferansiyel Denklem 1: y'' = yy', y(0) = 1, y'(0) = -1")
runge_kutta(f1, f2, x0, y10, y20, h, n)

# Diferansiyel denklem sistemi için başlangıç değerleri ve adım h
y10 = 0
y20 = 0

# Diferansiyel denklem sistemi çözümü
print("\nDiferansiyel Denklem 2: y'' - 2y' + y = e^x, y(0) = y'(0) = 0")
runge_kutta(f1, f2, x0, y10, y20, h, n)