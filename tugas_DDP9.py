print("========== no 1 ==========")
def celcius_ke_fahrenheit(celcius):
    hasil_konversi = (celcius * 9/5) + 32
    return  hasil_konversi 

celciuis = 0
print(celcius_ke_fahrenheit(0))
print(celcius_ke_fahrenheit(100))

# celciuis1 = 1
# print(f"hasilnya adalah{celcius_ke_fahrenheit(celcius1)}")
# print(celcius_ke_fahrenheit(100))

#soal no 2
print("========= no 2 ===========")

def is_genap(angka):
    """fungsi di gunakan untuk mengecek bilangan genap"""
    return angka % 2 == 0
print(is_genap(4))
print(is_genap(13))

genap = 4
print(f"output dari bilangan {genap} {is_genap(genap)}")
print(is_genap(15))

#soal no 3
print("========== no 3 ===========")

def nilai_kelulusan(nilai):
    print()
    if nilai >= 80:
        return "lulus"
    else :
        return "gagal"
print(nilai_kelulusan(80))    
print(nilai_kelulusan(60))


#soal no 4
print("========= no 4 ===========")

def bilangan(n):
    for i in range(1, n, 2):
        print(i, end=", ") 
bilangan(20)
