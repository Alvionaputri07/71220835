print ("~~~~~~~~~~~~~~~ /('v')\ ~~~~~~~~~~~~~~~")
print ("PROGRAM PENGHITUNG VOLUME BANGUN RUANG")
print ("~~~~~~~~~~~~~~~ \('V')/ ~~~~~~~~~~~~~~~")
print ("Pilihlah bangun ruang yang ingin dihitung:")
print ("1. Limas")
print ("2. Bola")
print ("3. Prisma")
print ("4. Kerucut")
print ()
pilihan = input ("Masukan Pilihan Anda: ")
if pilihan == "1" :
    alas = int(input ("Masukan panjang sisi alas limas: "))
    tinggi = input ("Masukan tinggi limas: ")
    print ("Volume Limas tersebut adalah:", 1/3 * (alas*alas) * tinggi)

else:
    print ("err")