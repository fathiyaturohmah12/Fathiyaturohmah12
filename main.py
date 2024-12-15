from Burung import Burung
from Ikan import Ikan
from Ular import Ular

# Membuat 3 objek Burung
burung1 = Burung("Elang", "Daging", "Udara", "Bertelur", "Paruh Tajam", "Coklat")
burung2 = Burung("Merpati", "Biji-bijian", "Udara", "Bertelur", "Paruh Kecil", "Putih")
burung3 = Burung("Burung Hantu", "Daging", "Hutan", "Bertelur", "Paruh Tajam", "Abu-abu")

# Membuat 3 objek Ikan
ikan1 = Ikan("Hiu", "Daging", "Laut", "Melahirkan", "Sirip Tajam", "Samudra")
ikan2 = Ikan("Gurame", "Tumbuhan", "Air Tawar", "Bertelur", "Sirip Kecil", "Kolam")
ikan3 = Ikan("Nemo", "Plankton", "Laut", "Bertelur", "Sirip Kecil", "Terumbu Karang")

# Membuat 3 objek Ular
ular1 = Ular("King Cobra", "Daging", "Darat", "Bertelur", 5, True)
ular2 = Ular("Sanca", "Daging", "Darat", "Bertelur", 8, False)
ular3 = Ular("Piton", "Daging", "Darat", "Bertelur", 6, False)

# Menampilkan informasi dan memanggil method masing-masing objek
print("=== Informasi Burung ===")
burung1.info_animal()
burung1.terbang()
print()
burung2.info_animal()
burung2.terbang()
print()
burung3.info_animal()
burung3.terbang()

print("\n=== Informasi Ikan ===")
ikan1.info_animal()
ikan1.berenang()
print()
ikan2.info_animal()
ikan2.berenang()
print()
ikan3.info_animal()
ikan3.berenang()

print("\n=== Informasi Ular ===")
ular1.info_animal()
ular1.melata()
print()
ular2.info_animal()
ular2.melata()
print()
ular3.info_animal()
ular3.melata()
