import sqlite3

connect = sqlite3.connect('agenda.db')
cursor = connect.cursor()
cursor.execute('''
        create table agenda(
            nome text,
            telefone text)
            ''')
cursor.execute('''
        insert into agenda (nome, telefone)
        values(?, ?)
        ''', ("nilo", "7788-1344"))

connect.commit()
cursor.close()
connect.close()