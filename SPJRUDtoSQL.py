import OperateurBinaire
import SQlLiteManage
import fct_utile
import OperateurUnitaire


def relation(name, attributes):
    """Fonction qui créé une relation dans une base de données

    :param name:
    :param attributes:
    :return: requete
    """

    requete = SQlLiteManage.create(name, attributes)
    return requete


def select(rel, cmp, attrib, const, counter):
    """Fonction qui execute une requête valide de selection

    :param rel:
    :param cmp:
    :param attrib:
    :param const:
    :param counter:
    :return: requete
    """

    requete = OperateurUnitaire.select(rel, cmp, attrib, const, counter)
    SQlLiteManage.run(requete)
    return requete


def project(rel, *args):
    """Fonction qui execute une requête valide de projection

    :param rel:
    :param args:
    :return: requete
    """

    requete = OperateurUnitaire.project(rel, *args)
    SQlLiteManage.run(requete)
    return requete


def rename(rel, old_name, new_name):
    """Fonction qui execute une requête valide de renommage
    PS: altère directement la relation dans la db!

    :param rel:
    :param old_name:
    :param new_name:
    :return: requete
    """
    requete = OperateurUnitaire.rename(rel, old_name, new_name)
    SQlLiteManage.run(requete)
    return requete


def join(rel1, rel2):
    """Fonction qui execute une requête valide de jointure

    :param rel1:
    :param rel2:
    :return: requete
    """
    requete = OperateurBinaire.join(rel1, rel2)
    SQlLiteManage.run(requete)
    return requete


def union(rel1, rel2):
    """Fonction qui execute une requête valide d'union

    :param rel1:
    :param rel2:
    :return: requete
    """
    requete = OperateurBinaire.union(rel1, rel2)
    SQlLiteManage.relations_order(rel2, rel1)
    SQlLiteManage.run(requete)
    return requete


def difference(rel1, rel2):
    """Fonction qui execute une requête valide de différence

    :param rel1:
    :param rel2:
    :return: requete
    """
    requete = OperateurBinaire.difference(rel1, rel2)
    SQlLiteManage.relations_order(rel2, rel1)
    SQlLiteManage.run(requete)
    return requete


def display(name):
    """Fonction qui affiche une table de la db à partir de son nom

    :param name:
    """
    SQlLiteManage.execute(f"SELECT * FROM {name}")
    result = list(SQlLiteManage.cursor.description)
    col = [i[0] for i in result]

    # Récuperer les données de la relation1 en BD dans attributes
    attributes = {}
    print("Le résultat de l'opération est la table\n")
    s = name + "    "
    for i in range(len(col)):
        attributes[col[i]] = []
        for row in SQlLiteManage.execute(f'SELECT {col[i]} FROM {name}'):
            attributes[col[i]].append(row[0])
    for i in range(len(col)):
        s += col[i] + " | "
    print(s)
    print(" " * len(name + "    ") + "-" * (len(s) - len(name + "    ")))
    for j in range(len(attributes[col[0]])):
        l = " " * len(name + "    ")
        for i in range(len(attributes)):
            l += str(attributes[col[i]][j]) + " | "
        print(l)
    print("\n")


def create(name, rel):
    """Fonction qui créé une table dans la db  à partir du résultat d’une requête SQL
    PS: Non utilisable avec un renommage car la table sera déjà altérer

    :param name:
    :param rel:
    """

    # Verifie si la relation est déjà existante en BD et la supprimer si oui
    SQlLiteManage.execute(f"DROP TABLE IF EXISTS {name}")

    nbcolonne = '(' + '?,' * (len(rel.attributes) - 1) + '?)'
    keys = fct_utile.listofkey(rel.attributes)
    namesAttributesAndType = fct_utile.nameandtype(rel.attributes, keys)
    donnees = SQlLiteManage.run(rel)

    # crée la table
    SQlLiteManage.cursor.execute(f'''CREATE TABLE {name}
        ({namesAttributesAndType})''')

    # insert les données
    SQlLiteManage.cursor.executemany(f"INSERT INTO {name}"
                                     f" VALUES {nbcolonne}", donnees)

    # Sauvegarde les changements
    SQlLiteManage.connection.commit()


def run(rel):
    """Fonction qui affiche une table à partir d'une requête

    :param rel:
    """

    print("Le résultat de l'opération sera une table\n")
    result = SQlLiteManage.run(rel)
    s = ""
    k = list(rel.attributes.keys())
    for i in range(len(k)):
        s += k[i] + " | "
    print(s)
    print("-" * len(s))
    for j in range(len(result)):
        l = ""
        for i in range(len(k)):
            l += str(result[j][i]) + " | "
        print(l)
    print("\n")

