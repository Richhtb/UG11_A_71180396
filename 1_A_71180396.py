print("="*10, "Progeam Manipulasi String","="*10)
print("Pilihan Menu :")
print("1. Hitung kata \n2. Ubah Kata")
pilihan = int(input("Pilihan anda: "))
QalimatQata = input("Masukkan sebuah kalimat/kata :")

def HitungKata(QalimatQata):
    qata = input("Masukkan kata yang ingin dihitung :")
    hitoeng = QalimatQata.count(qata)
    print(f"Terdapat sebanyak {hitoeng} kata {qata} di dalam kalimat")

def UbahKata(QalimatQata):
    qataDiubach = input("kata yang ingin diubah :")
    qatapengganty = input("Masukkan kata pengganti :")
    ganty = QalimatQata.replace(qataDiubach,qatapengganty)
    print(f"String berhasil diubah menjadi : {ganty}")

if pilihan == 1 :
    HitungKata(QalimatQata)

elif pilihan == 2 :
    UbahKata(QalimatQata)
else:
    print("Pilihan yang anda input tidak terdaftar di daftar pilihan")