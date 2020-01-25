# №2 задача
# time = int(input('Введите время в секундах: '))
# hour = time//3600
# minutes = (time - hour * 3600)//60
# seconds = (time - hour * 3600 - minutes * 60)
# print(f'время {hour} часа {minutes} минут {seconds} секунд')

# №3 задание
# n = input('Введите число от 1 до 9: ')
# summ = int(n)+int(n+n)+int(n+n+n)
# print(summ)

# №4 задание. Честно недопонял задание

# # №5 я так и не смог округлить до 2х знаков после запятой в рентабильности и прибыли на 1 сотрудника
# revenue = int(input('Введите выручку организации: '))
# costs = int(input('Введите издержки организации: '))
# profitability = (revenue - costs) / revenue * 100
# if revenue > costs:
#     print(f'Поздравляем ваша прибыль {revenue - costs} рублей')
#     print(f'Рентабильность организации:  {profitability} %')
#     staff = int(input('Введите количество сотрудников организации: '))
#     print(f'Прибыль организации на одного сотрудника: {(revenue-costs) / staff} рублей')
# elif revenue < costs:
#     print('К сожалению у вас убытки :(')
# else:
#     print('Вы сработали в ноль')

# №6 хотел не много модифицировать. Если цель достигнеться более чем через 30 дней выводить надпись и выйти из цикла
#  только он всё равно печатал последний принт с результатом. :(
# first_resuls = int(input('Сколько вы пробежали за первый день тренеровок?: '))
# finish_result = int(input('Какого результата вы ходите достичь?: '))
# finish_day = -1
# while first_resuls <= finish_result:
#     first_resuls += (first_resuls / 10)
#     finish_day += 1
#     # print(first_resuls) это я проверял прибавление 10%
#
#     # if finish_day > 30:
#     #     print('Поставте более достижимую цель')
#     #     break
# print(f'Вы достигните цели на {finish_day}-й день')

