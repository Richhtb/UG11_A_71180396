katak = input("Masukkan kata:")

def ambilHuruf(katak):
    banyakurup =len(katak)
    bagi2 = banyakurup // 2
    if banyakurup % 2 != 0: 
        katakGanjil= katak[bagi2 - 1: 1 - bagi2]
        print(f"huruf yang diambil pada kata {katak} adalah {katakGanjil}")
    else: 
        katak1 = katak[0:3]
        katak2 = katak[-3:]
        print(f"Huruf yang diambil pada kata {katak} adalah {katak1} dan {katak2}")


ambilHuruf(katak)