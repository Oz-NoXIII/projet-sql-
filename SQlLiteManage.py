import sqlite3

from fct_utile import nameandtype, listofkey, data

connection = sqlite3.connect('spjrudDB.db')
cursor = connection.cursor()


def execute(request):
    """Fonction qui prend une requette SQL en parametre, l'execute et retourne le resultat de l'operation"""

    cursor.execute(request)
    result = cursor.fetchall()
    connection.commit()
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
    connection.commit()


def relations_order(relation1, relation2):
    """Fonction qui prend deux Relations en paramètre, récupére les colonnes de la relation2 en BD et crée la relation1 par rapport à l'ordre
    des colonnes de la relation2 récupérés en BD"""

    # Récupérer les colonnes de la relation2 en BD
    execute(f"SELECT * FROM {relation2.name}")
    result = list(cursor.description)
    col = [i[0] for i in result]

    # Récuperer les données de la relation1 en BD dans attributes
    attributes = {}
    premierpassage = True
    for i in range(len(col)):
        if premierpassage:
            attributes[col[i]] = []
        for row in execute(f'SELECT {col[i]} FROM {relation1.name}'):
            attributes[col[i]].append(row[0])

    nbcolonne = '(' + '?,' * (len(attributes) - 1) + '?)'
    namesAttributesAndType = nameandtype(attributes, col)
    donnees = data(attributes, col)

    # Verifie si la relation1 est déjà existante en BD et la supprimer si oui
    execute(f"DROP TABLE IF EXISTS {relation1.name}")

    # créer la relation1
    cursor.execute(f'''CREATE TABLE {relation1.name}
        ({namesAttributesAndType})''')

    # Inserer les données de la relation1
    cursor.executemany(f"INSERT INTO {relation1.name}" f" VALUES {nbcolonne}", donnees)
    connection.commit()


def close():
    connection.close()
