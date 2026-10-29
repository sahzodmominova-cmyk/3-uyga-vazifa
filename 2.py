class Telefon:
    def __init__(self, quvvat):
        self.__quvvat = max(0, min(quvvat, 100))

    def quvvatni_korish(self):
        return self.__quvvat

    def zaryadla(self, foiz):
        if foiz > 0:
            self.__quvvat = min(100, self.__quvvat + foiz)

    def ishlat(self, foiz):
        if foiz > 0:
            self.__quvvat = max(0, self.__quvvat - foiz)


telefon = Telefon(40)
telefon.zaryadla(30)
telefon.ishlat(20)

print("Zaryad:", telefon.quvvatni_korish(), "%")