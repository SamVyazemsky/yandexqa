import math

class Scoring():
    def __init__(self, age, gender, source, income, cs, summ, term, target):
        """

        :param age: возраст
        :param gender: пол
        :param source: источник дохода: пассивный, активный
        :param income: доход за последний год
        :param cs: кредитный рейтинг
        :param sum: запрошенная сумма
        :param term: срок погашения
        :param target: цель кредита
        """
        self.age = age
        self.gender = gender
        self.source = source
        self.income = income
        self.cs = cs
        self.sum = summ
        self.term = term
        self.target = target
        self.income = 0
        self.max_limit = 0    # Максимально рассчитанный лимит
        self.stavka = 0     # ставка на кредит вместе с модификаторами
        self.payment = 0  # рассчитанный годовой платеж

    def check_is_issued(self):
        """

        :return: True если дают кредит и False если не дают
        """
        if self.age < 18:
            return False
        elif self.age >= 60:
            if self.gender == 'f':
                return False
            else:
                return True
        elif self.cs == -2:
            return False
        if self.source == "безработный":
            return True

    def check_sum(self):
        max = 0
        if self.source == 'пассивный доход' or self.cs == 0:
            max = 1000000
        if self.source == 'наемный работник':
            max = 5000000
        if self.source == 'собственный бизнес':
            max = 10000000

        self.max_limit = max

    def check_base_st(self):
        base = 10
        mod1 = 0
        if self.target == 'ипотека':
            mod1 = -2
        elif self.target == 'развитие бизнеса':
            mod1 = -0.5
        elif self.target == 'потребительский кредит':
            mod1 = 1.5

        mod2 = int(math.log(self.sum))
        mod3 = 0
        if self.source == 'пассивный доход':
            mod3 = 0.5
        elif self.source == 'наёмный работник':
            mod3 = -0.25
        elif self.source == 'собственный бизнес':
            mod3 = 0.25

        self.stavka = base + mod1 + mod2 + mod3

    def calc_payment(self):
        if self.max_limit == 0:
            self.payment = 0

        elif self.sum <= self.max_limit:
            self.payment = (self.sum * (1 + self.term * self.stavka)) / self.term
            if self.income <= self.payment * 2:
                self.payment = 0
        else:
            self.payment = 0
