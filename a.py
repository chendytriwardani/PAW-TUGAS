x = int(input("masukkan angka ="))
def angka(x):
    temp = 0
    for i in range(1, x+1):
        temp+=4*i
    print(temp)

angka(x)