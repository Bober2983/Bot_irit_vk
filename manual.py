from config import connection_db
from write_message import write_message_null
from text import MANUAL


def manual(sender):
    cur = connection_db.cursor()
    cur.execute("SELECT m.number, m.name FROM manual as m, teacher WHERE teacher.id = m.id_teacher ")
    rows = cur.fetchall()
    write_message_null(sender, MANUAL)
    for row in rows:
        text = row[0] + '. ' + row[1] + '\n'
        write_message_null(sender, text)
