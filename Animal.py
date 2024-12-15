class Animal:
    def __init__(self, name, makanan, hidup, berkembang_biak):
        self.name = name
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

    def info_animal(self):
        print(f"Nama Hewan       : {self.name}")
        print(f"Makanan          : {self.makanan}")
        print(f"Hidup di         : {self.hidup}")
        print(f"Berkembang Biak  : {self.berkembang_biak}")
