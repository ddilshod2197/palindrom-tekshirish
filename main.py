def teskari_tartibda(matn):
    so'zlar = matn.split()
    teskari = ' '.join(reversed(so'zlar))
    return teskari

matn = input("Matnni kiriting: ")
print(teskari_tartibda(matn))
