class BankHisobi:
    def __init__(self, balans):
        self.__balans = balans

    def balansni_korish(self):
        return self.__balans

    def pul_qosh(self, miqdor):
        if miqdor > 0:
            self.__balans += miqdor

    def pul_yech(self, miqdor):
        if 0 < miqdor <= self.__balans:
            self.__balans -= miqdor
        else:
            print("Mablag' yetarli emas!")


hisob = BankHisobi(100000)
hisob.pul_qosh(25000)
hisob.pul_yech(30000)

print("Balans:", hisob.balansni_korish())