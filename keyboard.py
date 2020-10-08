from vk_api.keyboard import VkKeyboard, VkKeyboardColor

# КЛАВИАТУРА (КНОПКИ)
menu = VkKeyboard(one_time=True)
menu.add_button('Расписание', color=VkKeyboardColor.PRIMARY)  # КНОПКА "РАСПИСАНИЕ"
menu.add_button('Методическое пособие', color=VkKeyboardColor.PRIMARY)  # КНОПКА "МЕТОДИЧЕСКОЕ ПОСОБИЕ

start = VkKeyboard(one_time=True)
start.add_button('Начать', color=VkKeyboardColor.PRIMARY)  # КНОПКА "Начать"

timetable = VkKeyboard(one_time=True)
timetable.add_button('Расписание занятий', color=VkKeyboardColor.PRIMARY)  # КНОПКА "РАСПИСАНИЕ ЗАНЯТИЙ"
timetable.add_line()
timetable.add_button('Расписание звонков', color=VkKeyboardColor.PRIMARY)  # КНОПКА "РАСПИСАНИЕ ЗВОНКОВ"
timetable.add_button('Расписание сессии', color=VkKeyboardColor.PRIMARY)  # КНОПКА "РАСПИСАНИЕ СЕССИИ"

return_ = VkKeyboard(one_time=True)
return_.add_button('Возврат в меню', color=VkKeyboardColor.NEGATIVE)  # КНОПКА "ОБРАТНО В МЕНЮ"

class_uni = VkKeyboard(one_time=True)
class_uni.add_button('1 Курс', color=VkKeyboardColor.POSITIVE)
class_uni.add_button('2 Курс', color=VkKeyboardColor.POSITIVE)
class_uni.add_line()
class_uni.add_button('3 Курс', color=VkKeyboardColor.POSITIVE)
class_uni.add_button('4 Курс', color=VkKeyboardColor.POSITIVE)
