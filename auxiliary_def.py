import time


# ПРОВЕРКА ЧЕТНОСТИ, НЕЧЕТНОСТИ НЕДЕЛИ
def multiple_week():
    week_year = int(time.strftime('%W', ))
    if (week_year % 2) == 1:
        week_c_n = 'НЧ'
    else:
        week_c_n = 'ЧН'
    return week_c_n


# КОНВЕРТАЦИЯ ГРУПП В ФОРМАТЕ "FF-FFF" - ГДЕ F - ЗАГЛАВНАЯ БУКВА
def gr_name_convert(reseived_message):
    temp_message = reseived_message.upper()
    split = temp_message.split()
    message = '-'.join(split)
    return message


# СПИСОК ГРУПП С ЕЁ ПРЕОБРАЗОВАНИЕМ
def gr_availability(reseived_message):
    command = False
    i = 0

    group = ['20-ИВТ-1', '20-ИВТ-2', '20-ИВТ-3', '20-ИСТ-1', '20-ИСТ-2', '20-ИСТ-3', '20-ИСТ-4', '20-ИТС', '20-КТЭС',
             '20-ПМ-1', '20-ПМ-2', '20-Р', 'С-20-РЭС', '19-ИВТ-1', '19-ИВТ-2', '19-ИВТ-3', '19-ИСТ-1', '19-ИСТ-2',
             '19-ИСТ-3', '19-ИСТ-4', '19-ИТС', '19-КТЭС', '19-ПМ-1', '19-ПМ-2', '19-Р', 'С-19-РЭС']

    while i < len(group):
        if group[i] == gr_name_convert(reseived_message):
            command = True
        i = i + 1
    return command
