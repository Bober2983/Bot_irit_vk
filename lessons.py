import datetime
import pytz

from config import connection_db
from write_message import write_message_null
from auxiliary_def import multiple_week, name_convert


def lessons(sender, reseived_message):
    tz = pytz.timezone('Europe/Moscow')  # ВЫБОР МОСКОВСКОГО ВРЕМЕНИ
    weekly = datetime.datetime.now(tz).strftime("%A")  # ДЕНЬ НЕДЕЛИ
    date = datetime.datetime.now(tz).strftime("%d.%m.%Y")  # ДАТА
    time = datetime.datetime.now(tz).strftime("%H:%M:%S")  # ВРЕМЯ
    check = False  # ПРОВЕРКА НА ПУСТОЙ ДЕНЬ НЕДЕЛИ

    cur = connection_db.cursor()
    cur.execute("SELECT l.lesson, l.week, l.time_p, l.teacher, l.audience, l.type_p FROM lessons as l, grp WHERE"
                " grp.id_gr = '%s' and grp.id_gr = l.id_gr and l.week = '%s' and "
                "(l.week_type = '%s' or l.week_type = 'Общая')" % (
                    name_convert(reseived_message), weekly, multiple_week()))
    rows = cur.fetchall()
    write_message_null(sender, '(' + date + ')' + "    Сегодня у нас: " + weekly + "\nВремя: " + time + '\n')
    for row in rows:
        check = True
        text = '***************************************\n' + 'Предмет: ' + row[0] + '\n Время пары: ' + row[2] + \
               '\n Преподователь: ' + row[3] + '\n Аудитория: ' + row[4] + '\n Тип пары: ' + row[5] + \
               '\n ***************************************'
        write_message_null(sender, text)
    if not check:
        write_message_null(sender, "Сегодня занятий нет!\nМожешь отдохнуть!")
