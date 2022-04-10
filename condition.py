# True AND True = True
# True AND False = False
# True OR False = True
# False OR False = False

# Masuk kerja = 7, pulang = 15, telat dua jam = ditolerir, telat >2 = potong gaji, >3 = datang setelah org pulang

masuk: int = 7
pulang: int = 15
max_late: int = 9

pukul_datang = int(input("Kamu datang pukul berapa?: "))

if pukul_datang == masuk:
    print("Kamu datang tepat waktu")
elif pukul_datang > masuk and pukul_datang <= max_late:
    print("Kamu telat! besok jangan diulangin lagi yah.")
elif pukul_datang > max_late and pukul_datang <= pulang:
    print("Kamu telat banget! dapat sanksi yah guys.")
else:
    print("Kamu datang ketika orang lain sudah pulang")
