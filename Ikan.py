from Animal import Animal

class Ikan(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_sirip, habitat):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis_sirip = jenis_sirip
        self.habitat = habitat

    def berenang(self):
        print(f"{self.name} sedang berenang di {self.habitat}!")
