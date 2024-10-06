# import package
import math

# function untuk menghitung luas dan keliling persegi
def persegi():
    # initialize
    sisi = float(input("Masukkan panjang sisi persegi: "))
    luas = sisi ** 2
    keliling = 4 * sisi
    
    # output
    print(f"Luas persegi: {luas}")
    print(f"Keliling persegi: {keliling}")

# function untuk menghitung luas dan keliling persegi panjang
def persegi_panjang():
    # initialize
    panjang = float(input("Masukkan panjang persegi panjang: "))
    lebar = float(input("Masukkan lebar persegi panjang: "))
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    
    # output
    print(f"Luas persegi panjang: {luas}")
    print(f"Keliling persegi panjang: {keliling}")

# function untuk menghitung luas dan keliling lingkaran
def lingkaran():
    # initialize
    jari_jari = float(input("Masukkan jari-jari lingkaran: "))
    luas = math.pi * (jari_jari ** 2)
    keliling = 2 * math.pi * jari_jari
    
    # output
    print(f"Luas lingkaran: {luas}")
    print(f"Keliling lingkaran: {keliling}")

# function untuk menghitung luas segitiga
def segitiga():
    # initialize
    alas = float(input("Masukkan panjang alas segitiga: "))
    tinggi = float(input("Masukkan tinggi segitiga: "))
    luas = 0.5 * alas * tinggi
    
    # output
    print(f"Luas segitiga: {luas}")

# function untuk menghitung volume kubus
def kubus():
    # initialize
    sisi = float(input("Masukkan panjang sisi kubus: "))
    volume = sisi ** 3
    
    # output
    print(f"Volume kubus: {volume}")

# function untuk menghitung volume balok
def balok():
    # initialize
    panjang = float(input("Masukkan panjang balok: "))
    lebar = float(input("Masukkan lebar balok: "))
    tinggi = float(input("Masukkan tinggi balok: "))
    volume = panjang * lebar * tinggi
    
    # output
    print(f"Volume balok: {volume}")

# function untuk menghitung volume tabung
def tabung():
    # initialize
    jari_jari = float(input("Masukkan jari-jari tabung: "))
    tinggi = float(input("Masukkan tinggi tabung: "))
    volume = math.pi * (jari_jari ** 2) * tinggi
    
    # output
    print(f"Volume tabung: {volume}")

# function untuk menghitung volume kerucut
def kerucut():
    # initialize
    jari_jari = float(input("Masukkan jari-jari kerucut: "))
    tinggi = float(input("Masukkan tinggi kerucut: "))
    volume = (1/3) * math.pi * (jari_jari ** 2) * tinggi
    
    # output
    print(f"Volume kerucut: {volume}")

# function untuk menyelesaikan persamaan kuadrat
def persamaan_kuadrat():
    # initialize
    print("Persamaan kuadrat dalam bentuk ax^2 + bx + c = 0")
    a = float(input("Masukkan nilai a: "))
    b = float(input("Masukkan nilai b: "))
    c = float(input("Masukkan nilai c: "))

    # output dan hitung diskriminan
    diskriminan = b ** 2 - 4 * a * c

    if diskriminan > 0:
        # dua solusi real
        x1 = (-b + math.sqrt(diskriminan)) / (2 * a)
        x2 = (-b - math.sqrt(diskriminan)) / (2 * a)
        print(f"Solusi persamaan kuadrat: x1 = {x1}, x2 = {x2}")
    elif diskriminan == 0:
        # satu solusi real
        x = -b / (2 * a)
        print(f"Solusi persamaan kuadrat: x = {x}")
    else:
        # tidak ada solusi real
        print("Tidak ada solusi real untuk persamaan ini.")

# function untuk perhitungan trigonometri (sin, cos, tan)
def trigonometri():
    # initialize
    sudut = float(input("Masukkan sudut dalam derajat: "))
    
    # konversi sudut dari derajat ke radian
    radian = math.radians(sudut)  
    
    # output
    print(f"Sin({sudut}) = {math.sin(radian)}")
    print(f"Cos({sudut}) = {math.cos(radian)}")
    print(f"Tan({sudut}) = {math.tan(radian)}")

# Menu utama aplikasi
def main_menu():
    while True:
        print("\nPilih perhitungan matematika:")
        print("1. Luas dan Keliling Persegi")
        print("2. Luas dan Keliling Persegi Panjang")
        print("3. Luas dan Keliling Lingkaran")
        print("4. Luas Segitiga")
        print("5. Volume Kubus")
        print("6. Volume Balok")
        print("7. Volume Tabung")
        print("8. Volume Kerucut")
        print("9. Persamaan Kuadrat")
        print("10. Trigonometri (Sin, Cos, Tan)")
        print("0. Keluar")

        pilihan = input("Masukkan pilihan: ")

        if pilihan == "1":
            persegi()
        elif pilihan == "2":
            persegi_panjang()
        elif pilihan == "3":
            lingkaran()
        elif pilihan == "4":
            segitiga()
        elif pilihan == "5":
            kubus()
        elif pilihan == "6":
            balok()
        elif pilihan == "7":
            tabung()
        elif pilihan == "8":
            kerucut()
        elif pilihan == "9":
            persamaan_kuadrat()
        elif pilihan == "10":
            trigonometri()
        elif pilihan == "0":
            print("Terima kasih telah menggunakan MathCalc!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

# start the mathcalc
main_menu()