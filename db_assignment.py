"""Database Assignment"""
import sqlite3
import re

conn = sqlite3.connect('db_assignment.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (org TEXT, count INTERER)')

file = input('Enter file name: ')
if file == '':
    file = 'mbox.txt'
    file_handler = open(file, encoding="utf-8")
    for line in file_handler:
        if line.startswith('From '):
            email = line.split()[1]
            org = re.findall('@(.*)', email)[0]
            cur.execute(
                '''
                SELECT count FROM Counts WHERE org = ?
                ''',
                (org,)
                )
            row = cur.fetchone()
            if row is None:
                cur.execute(
                    '''
                    INSERT INTO COUNTS (org, count)
                    VALUES (?, 1)
                    ''',
                    (org,)
                )
            else:
                cur.execute(
                    '''
                    UPDATE Counts SET count = count + 1 WHERE org = ?
                    ''',
                    (org,)
                )
    conn.commit()

cur.close()
