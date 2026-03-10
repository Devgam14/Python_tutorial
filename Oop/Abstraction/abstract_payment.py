from abc import ABC , abstractmethod

class Payment():
    @abstractmethod
    def tax_pay(self , amount : float) -> float:
        pass
class NigPay(Payment):
    def tax_pay(self, amount : float) -> float:
        return amount - (amount * 0.05)
class GHPay(Payment):
    def tax_pay(self, amount : float) -> float:
        return amount - (amount * 0.08)
class TgPay(Payment):
    def tax_pay(self, amount : float) -> float:
        return amount - (amount * 0.07)
pay = NigPay()
print(pay.tax_pay(1234.33))
g_pay = GHPay()
print(g_pay.tax_pay(1234.33))
tg_pay = TgPay()
print(tg_pay.tax_pay(1234.33))