def createMenu():
    print("\nMenu : \n1. Faktorial \n2. Prima")
    usr = int(input("\nMasukan pilihan anda 1/2 : "))
    if usr == 1 :
        faktorial()
    elif usr == 2 :
        prima()
    else:
        createMenu()

def faktorial():
    val = int(input("\nMasukan jumlah n faktorial : "))
    hasil = 1
    for i in range(val):
        hasil = (i+1)*hasil
    print("\n{}".format(hasil))

def prima():
    temp = []
    val = int(input("\nMasukan angka : "))
    for a in range(2,val+1,1):
        mod = 1
        for b in range(2,a,1):
            if (a % b == 0):
                mod = 0
        if (mod == 1):
            temp.append(a)
    if val in temp :
        print("{} merupakan bilangan prima".format(val))
    else:
        print("{} bukan bilangan prima".format(val))

createMenu()