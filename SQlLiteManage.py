import sqlite3

connection = sqlite3.connect('spjrudDB.db')
cursor = connection.cursor()


def execute(request):
    """Fonction qui prend une requette SQL en parametre, l'execute et retourne le resultat de l'operation"""

    cursor.execute(request)
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result

