from Animal import Animal

class Burung(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_paruh, warna_bulu):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis_paruh = jenis_paruh
        self.warna_bulu = warna_bulu

    def terbang(self):
        print(f"{self.name} sedang terbang tinggi di udara!")
