class Mahsulot:
    def __init__(self, nom, miqdor):
        self.nom = nom
        self.__miqdor = max(0, miqdor)

    def miqdorni_korish(self):
        return self.__miqdor

    def qabul_qil(self, son):
        if son > 0:
            self.__miqdor += son

    def sotish(self, son):
        if 0 < son <= self.__miqdor:
            self.__miqdor -= son
        else:
            print("Mahsulot yetarli emas!")


mahsulot = Mahsulot("Daftar", 20)
mahsulot.sotish(6)
mahsulot.qabul_qil(4)

print("Mahsulot:", mahsulot.nom)
print("Miqdor:", mahsulot.miqdorni_korish(), "dona")