import matplotlib.pyplot as plt

def hitung_digit_iteratif(n):
    if n == 0:
        return 1
    count = 0
    n = abs(n)
    while n > 0:
        count += 1
        n //= 10
    return count

def hitung_digit_rekursif(n):
    n = abs(n)
    if n < 10:
        return 1
    return 1 + hitung_digit_rekursif(n // 10)

if __name__ == "__main__":
    n = int(input("Masukkan bilangan bulat: "))

    hasil_iteratif = hitung_digit_iteratif(n)
    hasil_rekursif = hitung_digit_rekursif(n)

    print("\nHasil Perhitungan:")
    print("Jumlah digit (Iteratif) :", hasil_iteratif)
    print("Jumlah digit (Rekursif) :", hasil_rekursif)

    digit = list(range(1, 11))
    iteratif_ops = digit
    rekursif_ops = digit

    plt.figure()
    plt.plot(digit, iteratif_ops, label="Iteratif O(d)")
    plt.plot(digit, rekursif_ops, label="Rekursif O(d)")
    plt.xlabel("Jumlah Digit")
    plt.ylabel("Jumlah Operasi")
    plt.title("Perbandingan Kompleksitas Iteratif vs Rekursif")
    plt.legend()
    plt.show()
