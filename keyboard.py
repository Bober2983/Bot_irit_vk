from vk_api.keyboard import VkKeyboard,VkKeyboardColor


# КЛАВИАТУРА (КНОПКИ)

menu = VkKeyboard(one_time=True)
menu.add_button('Расписание', color = VkKeyboardColor.PRIMARY) # КНОПКА "РАСПИСАНИЕ"

start = VkKeyboard(one_time=True)
start.add_button('Начать', color = VkKeyboardColor.PRIMARY) # КНОПКА "Начать"

timetable = VkKeyboard(one_time=True)
timetable.add_button('Расписание занятий', color = VkKeyboardColor.PRIMARY)# КНОПКА "РАСПИСАНИЕ ЗАНЯТИЙ"
timetable.add_button('Расписание звонков', color = VkKeyboardColor.PRIMARY)# КНОПКА "РАСПИСАНИЕ ЗВОНКОВ"

return_ = VkKeyboard(one_time=True)
return_.add_button('Возврат в меню', color = VkKeyboardColor.NEGATIVE) # КНОПКА "ОБРАТНО В МЕНЮ"