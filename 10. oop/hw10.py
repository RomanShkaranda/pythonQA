"""
Створити клас Банківського рахунку
атрибут класу - депозитний портфель
клас при ініціалізації отримує імя користувача, початкову суму внеску, та відсоток нарахування на залишок по рахунку (передається цілим числом, проте є приватним (__ у назві))
при ініціалізації також автоматично генерується дата відкриття рахунку та унікальний ідентифікатор рахунку - для цього погляньте як працює
import uuid
print(uuid.uuid4())
створити геттер та сеттер для зміни ставки по рахунку (аналог дня дародження на прикладі, описаному на лекції)
перевизначте метод __str__ (наповнення - на ваш вибір)
створіть методи для поповнення та зняття коштів з рахунку (рахунок не може мати негативний баланс)
створіть класметоди для контролю депозитного портфелю (запускаються в ініціалізаторі, методах поповнення та зняття, __del__
!!! перевизначте метод __del__ - при його виклику автоматично знімаються всі кошти з рахунків власника та ПРИНТИТЬСЯ повідомлення, що у такого то власника закрито рахунок у звязку з ліквідацією банка, повернуто таку-то суму, власник препензій не має (це один із двох принтів в програмі, все інше має бути здано без принтів - при розробці користуйтеся дебагером чи принтами, на ваш вибір)
створіть метод трансфер, який дозволяє переводити кошти з одного рахунку на інший
створіть метод get_todays_profit, задекорований через property
він має автоматично розраховувати плановий прибуток за сьогоднішній день з огляду на поточний залишок на рахунку
та відсоткову ставку (зауважте, ставка в ініціалізаторі - річна, а за день 1/365 ставки * суму)
    створіть метод, задекорований staticmethod
    в ньому буде принтом (одним із двох в програмі) виводитися рекламний слоган банку - вигадайте щось помпезне
    можете скористатися
    https://www.geeksforgeeks.org/art-module-in-python/
    https://towardsdatascience.com/rich-generate-rich-and-beautiful-text-in-the-terminal-with-python-541f39abf32e
чи самостійно пошукати аналог
головне памятайте - щось встановлюєте ручками, то кріпите requirements.txt
створити мінімум два рахунки
в одному з них змінити ставку
внести та зняти кошти
перевести кошти (чи їх частину) одного рахунку на інший (не дозволяєм заходити в мінуса по рахункам)
впевнитися, що виконуються дії, описані в __del__, при закінченні роботи програми
"""
import uuid
import datetime
from art import *



class BankAccount:
    deposit_portfolio = 0

    def __init__(self, user_name, first_summa, percent, open_date, user_id):
        self.user_name = user_name
        self.first_summa = first_summa
        self.__percent = percent
        self.open_date = open_date
        self.user_id = user_id
        BankAccount.total_money_add(first_summa)

    @property
    def percent_change(self):
        """
        Get the "__percent"
        :return:
        """
        return self.__percent

    @percent_change.setter
    def percent_change(self, change_summa):
        """
        Setter for "__percent"
        :param change_summa:
        :return:
        """
        self.__percent = change_summa

    def __str__(self):
        """
        Rewrite string method to get username + his money
        :return:
        """
        return f'{self.user_name} {self.first_summa}'

    def add_money(self, summa):
        """
        Adding money to user's wallet
        :param summa:
        :return:
        """
        self.first_summa += summa
        BankAccount.total_money_add(summa)

    def sub_money(self, summa):
        """
        Substruct money from user's wallet
        :param summa:
        :return:
        """
        self.first_summa -= summa
        BankAccount.total_money_sub(summa)

    @classmethod
    def total_money_add(cls, summa):
        """
        Deposit portfolio controll
        :param summa:
        :return:
        """
        BankAccount.deposit_portfolio += summa

    @classmethod
    def total_money_sub(cls, summa):
        """
        Deposit portfolio controll
        :param summa:
        :return:
        """
        BankAccount.deposit_portfolio -= summa

    def __del__(self):
        """
        Get all user's money from his wallet and return a text message
        :return:
        """
        text = f"Власнику {self.user_name} закрито рахунок у звязку з ліквідацією банка, повернуто {self.first_summa}, власник претензій не має"
        self.first_summa -= self.first_summa
        return text

    def transfer(self, other, summa):
        """
        Getting money from one account to another
        :param other:
        :param summa:
        :return:
        """
        if other.first_summa >= summa:
            self.first_summa += summa
            other.first_summa -= summa
        else:
            other.first_summa = 0
            self.first_summa += other.first_summa

    @property
    def get_todays_profit(self):
        """
        One day profit by one bank account
        :return:
        """
        profit = (self.first_summa * self.__percent) / 36500
        return profit

    @staticmethod
    def adv_method():
        """
        Фdvertising message
        :return:
        """
        text = tprint("Best bank ever!")
        return text


roman = BankAccount('Roman', 1000, 10, datetime.date.today(), uuid.uuid4())
doe = BankAccount('Doe', 2000, 20, datetime.date.today(), uuid.uuid4())

roman.percent_change = 20
roman.add_money(100)
roman.sub_money(200)
doe.transfer(roman, 99)

