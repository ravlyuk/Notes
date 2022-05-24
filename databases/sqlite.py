# Импорт модуля
import sqlite3

# Установить соединение с базой данных
conn = sqlite3.connect('База Телеграм.sqlite')

# Создать курсор
cursor = conn.cursor()

# Пример записи в таблицу black_list
cursor = conn.execute("INSERT INTO black_list VALUES ( '{pole1}' , '{pole2}' , '{pole3}' , 'Simple Text' , '{date}' )".format( pole1=pole1 , pole2=pole2 , pole3=pole3, date=datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S") ) )
conn.commit()

# Пример удаления с таблицы white_list
cursor = conn.execute("DELETE FROM white_list WHERE number = '{pole1}'".format( pole1=pole1) )
conn.commit()

# Пример поиска в таблице black_list
cursor = conn.execute("SELECT * FROM black_list WHERE number LIKE  :number" , {"number": number} )
results = cursor.fetchall()