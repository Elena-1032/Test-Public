qt_bilet = int(input("Введите количество билетов:"))
cost_bilet = 0
for i in range(qt_bilet):
    age_bilet =int(input("Введите возраст посетителя: "))
    if age_bilet < 18:
        cost_bilet = cost_bilet + 0
        print("стоимость билета равна 0р.")
    elif age_bilet < 25:
        cost_bilet = cost_bilet + 990
        print("стоимость билета равна 990р.")
    else:
        cost_bilet = cost_bilet + 1390
        print("стоимость билета равна 1390р.")
if qt_bilet < 4:
    if (cost_bilet%10==1 and cost_bilet%100 != 11):rub =' рубль'
    elif (cost_bilet%10==0 or 11 <= cost_bilet%100 <=19 or 5 <= cost_bilet%10 <=10):rub=' рублей'
    elif (2 <= cost_bilet%10 <= 4):rub=' рубля'
    print("количество билетов: ", qt_bilet," Сумма к оплате: ",cost_bilet, rub)
else:
    cost_bilet = cost_bilet*0.9
    if (cost_bilet%10==1 and cost_bilet%100 != 11):rub =' рубль'
    elif (cost_bilet%10==0 or 11 <= cost_bilet%100 <=19 or 5 <= cost_bilet%10 <=10):rub=' рублей'
    elif (2 <= cost_bilet%10 <= 4):rub=' рубля'
    print("количество посетителей: ", qt_bilet, "Cумма к оплате со скидкой 10%: ",cost_bilet, rub)
