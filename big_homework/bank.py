import random


# Создайте функцию get_random_digits, которое принимает целое число count (количество цифр), и возвращает строку,
# сгенерированную из count рандомных цифр от нуля до девяти (исп. random.randint).

def get_random_digits(count: int) -> str:
    result = ''
    for _ in range(count):
        result += str(random.randint(0, 9))
    return result


# Создайте класс BankAccount
# Создайте в классе конструктор, который принимает одно значение: card_holder (строка с именем держателя карты).
# В конструкторе должны создаваться следующие поля:
# card_holder - поле равное аргументу конструктора card_holder, но в верхнем регистре (исп. функцию upper).
# money - количество денег на счету. Выставьте в 0 (счёт только открыли, на нём пока нет денег).
# account_number - номер счёта, строка из 20 рандомных чисел.
# card_number - номер карты, строка из 16 рандомных чисел.

class BankAccount:
    def __init__(self, card_holder):
        self.card_holder = card_holder.upper()
        self.money = 0
        self.account_number = get_random_digits(20)
        self.card_number = get_random_digits(16)


# Создайте класс Bank.
# Добавьте в класс конструктор без аргументов. Создайте в конструкторе поле bank_accounts c типом dict[str, BankAccount]
# (словарь, где ключом является номер счёта, а значением - объект BankAccount). Изначально данное поле - пустой словарь.

class Bank:
    def __init__(self):
        self.bank_accounts: dict[str, BankAccount] = {}

# Добавьте метод open_account:
# Метод принимает один аргумент - card_holder
# Создаёт новый банковский счёт и сохраняет его в поле bank_accounts
# Возвращает (return) созданный счёт.

    def open_account(self, card_holder) -> BankAccount:
        account = BankAccount(card_holder)
        self.bank_accounts[account.account_number] = account
        return account

# Добавьте метод add_money:
# Метод принимает два аргумента: account_number и money
# Находит счёт в поле bank_accounts и прибавляет к деньгам на счету соответствующее количество денег (money).

    def add_money(self, account_number: str, money: float):
        target_account = self.bank_accounts[account_number]
        target_account.money += money

# Добавьте метод transfer_money:
# Метод принимает три аргумента: from_account_number (номер счёта-отправителя), to_account_number
# (номер счёта-получателя), money.
# Снимает деньги со счёта-отправителя.
# Добавляет деньги на счёт-получателя.

    def transfer_money(self, from_account_number, to_account_number, money):
        from_account = self.bank_accounts[from_account_number]
        to_account = self.bank_accounts[to_account_number]
        from_account.money -= money
        to_account.money += money

# Добавьте метод external_transfer:
# Метод принимает три аргумента: from_account_number (номер счёта-отправителя), to_external_number
# (внешний номер счёта-получателя), money.
# Снимает деньги со счёта-отправителя
# Мы не настоящий банк, поэтому просто пишем в консоль
# "Банк перевёл xxx$ с вашего счёта XXXX на внешний счёт YYYY"

    def external_transfer(self, from_account_number, to_external_number, money):
        from_account = self.bank_accounts[from_account_number]
        from_account.money -= money
        print(f'Банк перевёл {money}$ с вашего счёта {from_account_number} на внешний счёт {to_external_number}')


# Создайте класс Controller
# Добавьте в класс конструктор без аргументов. В конструкторе должно создаваться одно поле bank (объект класса Bank).
# Добавьте в класс метод run, который пока будет просто выводить на экран "Здравствуйте, наш банк открылся!"

class Controller:
    def __init__(self):
        self.bank = Bank()

    def run(self):
        print('Здравствуйте, наш банк открылся!')

# Добавьте в метод run бесконечный цикл (while True) + прочитайте цифру, которую ввёл пользователь.

        while True:
            print('# Выберите действие:')
            print('0. Завершить программу')
            print('1. Открыть новый счёт')
            print('2. Просмотреть открытые счета')
            print('3. Положить деньги на счёт')
            print('4. Перевести деньги между счетами')
            print('5. Совершить платёж')

            action = int(input())

# Если эта цифра 0 (Завершить программу):
# Вывести на экран "До свидания!"
# Выйти из бесконечного цикла (просто break)

            if action == 0:
                print('До свидания!')
                break

# Если 1 (Открыть новый счёт):
# Запросить у пользователя имя и фамилию держателя карты.
# Создать новый счёт в банке.
# Вывести сообщение "Счёт XXXX создан".

            elif action == 1:
                card_holder = input('Введите имя и фамилию держателя карты: ')
                account = self.bank.open_account(card_holder)
                print(f'Счёт {account.account_number} создан')

# Если 2 (Просмотреть открытые счета):
# Вывести на экран все открытые счета (bank.bank_accounts)

            elif action == 2:
                print('Все счета: ')
                for account in self.bank.bank_accounts.values():
                    print(f' Счёт: {account.account_number}')
                    print(f'    Остаток на счету: {account.money}S')
                    print(f'    Номер карты: {account.card_number}S')
                    print(f'    Держатель карты: {account.card_holder}S')

# Если 3 (Положить деньги на счёт):
# Запросить у пользователя номер счёта и сумму, на которую его нужно пополнить.
# Положить деньги на соответствующий счёт.

            elif action == 3:
                account_number = input('Введите номер счёта: ')
                money = float(input('Введите количество денег: '))
                self.bank.add_money(account_number, money)
                print(f'')

# Если 4 (Перевести деньги между счетами):
# Запросить у пользователя номер счёта-отправителя, номер счёта-получателя и количество денег.
# Выполнить перевод в банке.

            elif action == 4:
                from_account_number = input('Введите номер счёта отправителя: ')
                to_account_number = input('Введите номер счёта получателя: ')
                money = float(input('Введите количество денег: '))
                self.bank.transfer_money(from_account_number, to_account_number, money)

# Если 5 (Совершить платёж):
# Запросить у пользователя номер счёта-отправителя, номер внешнего счёта (может быть просто рандомной строкой) и
# количество денег.
# Выполнить платёж в банке (transfer_external)

            elif action == 5:
                from_account_number = input('Введите номер счёта отправителя: ')
                to_external_number = input('Введите номер счёта получателя: ')
                money = float(input('Введите количество денег: '))
                self.bank.external_transfer(from_account_number, to_external_number, money)
            else:
                print('Вы ввели неподдерживаемую команду')


# Добавьте в конец файла bank.py следующий код:
# if __name__ == '__main__':
#     controller = Controller()
#     controller.run()
# Этот код будет запускать всю программу и будет работать до тех пор, пока пользователь не захочет выйти.

if __name__ == '__main__':
    controller = Controller()
    controller.run()