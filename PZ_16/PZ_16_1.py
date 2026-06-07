# Создайте класс «Банк», который имеет атрибуты суммы денег и процентной ставки.
# Добавьте методы для вычисления процентных начислений и снятия денег.

class Bank:
    def __init__(self, money, interest_rate):
        self.money = float(money)
        self.interest_rate = float(interest_rate)

    def calculate_interest(self):
        earnings = self.money * self.interest_rate
        print(f"Начисленные проценты: {earnings}")
        return earnings

    def withdraw(self, amount):
        if float(amount) <= self.money:
            self.money -= float(amount)
            print(f"Снято: {amount}. Оставшийся баланс: {self.money}")
        else:
            print("Недостаточно средств на счете!")

try:
    my_account = Bank(money=input('введите сумму денег: '), interest_rate=0.12)
    my_account.calculate_interest()
    my_account.withdraw(input('введите сколько вы хотите снять: '))
except ValueError:
    print('Введите число.')
    exit()

