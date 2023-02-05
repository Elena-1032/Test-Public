per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму вклада:_ "))
# print("per_cent-",per_cent)
# print("per_cent.keys() -", per_cent.keys())
# print("per_cent.values() - ",per_cent.values())
deposit = []
deposit = [money/100*i for i in per_cent.values()]
print("deposit", deposit)
print("максимальная сумма",max(deposit))
