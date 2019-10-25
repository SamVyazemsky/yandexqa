import scoring


def main():
    input_data = open('input.txt', 'r')
    input_list = input_data.readline().split(',')
    age, gender, source, income, cs, summ, term, target = input_list
    rez = scoring.Scoring(int(age), gender, source, int(income), cs, int(summ), int(term), target)
    rez.check_sum()
    if rez.check_is_issued() is False:
        print("Кредит не выдан")
    rez.check_sum()
    rez.calc_payment()
    if rez.payment == 0:
        print("Кредит не выдан")
    else:
        print("Сумма кредита: {rez.sum}, Платёж: {rez.payment}")


if __name__=='__main__':
    main()