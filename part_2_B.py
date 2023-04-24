import math

# Fonksiyonların tanımlanması
def f1(x):
    return x * math.log(x)

def f2(x):
    return x * math.cos(x) - x**2 * math.sin(x)

# Merkezi Fark Yaklaşımı ile 1. türev hesaplaması
def central_difference(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

# İleri Fark Yaklaşımı ile 1. türev hesaplaması
def forward_difference(f, x, h):
    return (f(x + h) - f(x)) / h

# Geri Fark Yaklaşımı ile 1. türev hesaplaması
def backward_difference(f, x, h):
    return (f(x) - f(x - h)) / h

# Hesaplanan ve gerçek 1. türev değerlerini karşılaştırma
def compare_derivatives(f, x, h):
    f_prime_exact = f(x)
    f_prime_central = central_difference(f, x, h)
    f_prime_forward = forward_difference(f, x, h)
    f_prime_backward = backward_difference(f, x, h)
    print("Fonksiyon: f(x) =", f.__name__)
    print("x =", x)
    print("Merkezi Fark Yaklaşımı ile 1. türev:", f_prime_central)
    print("İleri Fark Yaklaşımı ile 1. türev:", f_prime_forward)
    print("Geri Fark Yaklaşımı ile 1. türev:", f_prime_backward)
    print("Gerçek 1. türev:", f_prime_exact)
    print("Merkezi Fark Yaklaşımı Hata:", abs(f_prime_exact - f_prime_central))
    print("İleri Fark Yaklaşımı Hata:", abs(f_prime_exact - f_prime_forward))
    print("Geri Fark Yaklaşımı Hata:", abs(f_prime_exact - f_prime_backward))
    print("**************************************")

# Fonksiyonların hesaplamalarının yapılacağı x değerleri
x1 = 8
x2 = 3

# Fonksiyonların hesaplamalarının yapılacağı h değerleri
h1 = 0.01
h2 = 0.001

# 1. türev hesaplamalarının yapılması ve sonuçların karşılaştırılması
compare_derivatives(f1, x1, h1)
compare_derivatives(f1, x1, h2)
compare_derivatives(f2, x2, h1)
compare_derivatives(f2, x2, h2)
