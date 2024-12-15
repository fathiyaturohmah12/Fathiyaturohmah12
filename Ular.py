from Animal import Animal

class Ular(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, panjang_tubuh, berbisa):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.panjang_tubuh = panjang_tubuh
        self.berbisa = berbisa

    def melata(self):
        print(f"{self.name} sedang melata dengan tubuh sepanjang {self.panjang_tubuh} meter!")
