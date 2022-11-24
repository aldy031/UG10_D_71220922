print ('Program Kalkulator Sederhana')
print ('1. untuk menghitung Penjumlahan')
print ('2. untuk menghitung Penjumlahan')
print ('3. untuk menghitung Penjumlahan')
print ('4. untuk menghitung Penjumlahan')
print ('5. untuk menghitung Penjumlahan')
print ('6. untuk menghitung Penjumlahan')
print ('silahkan pilih 1-6')

 

pil = int(input ('Masukkan pilihan : '))
if pil == 1:
    a = int(input("bil 1 = "))
    b = int(input("bil 2 = "))
    print(f"hasil dari {a} dijumlahkan dengan {b} adalah", a+b)
elif pil == 2:
    a = int(input("bil 1 = "))
    b = int(input("bil 2 = "))
    print(f"hasil dari {a} dijumlahkan dengan {b} adalah", a-b)
elif pil == 3:
    a = int(input("bil 1 = "))
    b = int(input("bil 2 = "))
    print(f"hasil dari {a} dijumlahkan dengan {b} adalah ",a*b)
elif pil == 4:
    a = int(input("bil 1 = "))
    b = int(input("bil 2 = "))
    print(f"hasil dari {a} dijumlahkan dengan {b} adalah", a/b)
elif pil == 5:
    a = int(input("bil 1 = "))
    b = int(input("bil 2 = "))
    print(f"hasil dari {a} dijumlahkan dengan {b} adalah", a%b)
elif pil == 6:
    a = int(input("bil 1 = "))
    b = int(input("bil 2 = "))
    print(f"hasil dari {a} dijumlahkan dengan {b} adalah", a**b)
