import datetime
from config import write_message_null,con,ch_nch_week




def lessons_p (sender,reseived_message):

    weekly = datetime.datetime.today().strftime("%A") #ДЕНЬ НЕДЕЛИ
    date = datetime.datetime.today().strftime("%d.%m.%Y") # ДАТА
    time = datetime.datetime.today().strftime("%H:%M:%S") # ВРЕМЯ

    check = False
    cur = con.cursor()
    cur.execute("SELECT l.lesson,l.week,l.time_p,l.teacher,l.audience,l.type_p FROM lessons as l,grp WHERE grp.id_gr = '%s' and grp.id_gr = l.id_gr and l.week = '%s' and (l.week_type = '%s' or l.week_type = 'Общая') " % (reseived_message,weekly,ch_nch_week()))
    rows = cur.fetchall()
    write_message_null(sender, '('+date+')' + "    Сегодня у нас: " + weekly + "\nВремя: " + time+'\n' )
    for row in rows:
        check = True
        text = '****************************************\n'+'Предмет: ' + row[0] + '\n Время пары: ' + row[2] + '\n Преподователь: ' + row[3] + '\n Аудитория: ' + row[4] + '\n Тип пары: ' + row[5] + '\n ****************************************'
        write_message_null(sender, text)
    if check == False:
        write_message_null(sender, "Сегодня занятий нет!\nМожешь отдохнуть!")
