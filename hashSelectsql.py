import sqlite3
  
class hashSelectsql:

# neviem kde v tabulke su uložene hashe ak vôbec sú tak som len slepý debilko preto selektujem 
# filenamena zstenie či fuguje porovnanie

    def selectMail(self):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute(("SELECT filename FROM users WHERE mail = 'oliverbielik@gmail.,com'"))
        hashTab = c.fetchall()
        conn.close()

        return hashTab