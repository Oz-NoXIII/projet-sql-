import sqlite3

from fct_utile import nameandtype, listofkey, data

connection = sqlite3.connect('spjrudDB.db')
cursor = connection.cursor()


def execute(request):
    """Fonction qui prend une requette SQL en parametre, l'execute et retourne le resultat de l'operation"""

    cursor.execute(request)
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result


def create(name, attributes):
    nbcolonne = '(' + '?,' * (len(attributes) - 1) + '?)'
    keys = listofkey(attributes)
    namesAttributesAndType = nameandtype(attributes, keys)
    donnees = data(attributes, keys)

    # crée la table
    cursor.execute(f'''CREATE TABLE {name}
    ({namesAttributesAndType})''')
    # print(f'''CREATE TABLE {name} ({namesAttributesAndType})''')

    # insert les données
    cursor.executemany(f"INSERT INTO {name}"
                       f" VALUES {nbcolonne}", donnees)
    # print(f"INSERT INTO {name}" f" VALUES {nbcolonne}", donnees)

    # Sauvegarde les changements
    connection.commit()


def delete(name):
    cursor.execute(f"DROP TABLE {name}")
