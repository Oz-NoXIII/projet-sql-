import sqlite3

import OperateurBinaire
import SQlLiteManage
import fct_utile
import OperateurUnitaire


def relation(name, attributes):
    requete = fct_utile.Relation(name, attributes)
    SQlLiteManage.create(name, attributes)
    return requete


def select(rel, cmp, attrib, const, counter):
    requete = OperateurUnitaire.select(rel, cmp, attrib, const, counter)
    # SQlLiteManage.execute(requete.name)
    return requete


def project(rel, *args):
    requete = OperateurUnitaire.project(rel, *args)
    # SQlLiteManage.execute(requete.name)
    return requete


def rename(rel, old_name, new_name):
    requete = OperateurUnitaire.rename(rel, old_name, new_name)
    # SQlLiteManage.execute(requete.name)
    return requete


def join(rel1, rel2):
    requete = OperateurBinaire.join(rel1, rel2)
    # SQlLiteManage.execute(requete.name)
    return requete


def union(rel1, rel2):
    requete = OperateurBinaire.union(rel1, rel2)
    SQlLiteManage.relations_order(rel2, rel1)
    # SQlLiteManage.execute(requete.name)
    return requete


def difference(rel1, rel2):
    requete = OperateurBinaire.difference(rel1, rel2)
    SQlLiteManage.relations_order(rel2, rel1)
    # SQlLiteManage.execute(requete.name)
    return requete


def run(relation):
    """Fonction qui prend en paramètre une requête simple ou imbriquée, l'exécute et affiche le résultat à l'écran"""

    request = relation.name
    result = SQlLiteManage.execute(request)

    # Récupérer les noms d'attributs du résultat de la requête
    desc_cursor = list(SQlLiteManage.cursor.description)
    columns = [i[0] for i in desc_cursor]

    print(f"Le résultat de l'opération est l'ensemble d'attribut(s) {columns} de valeur(s): \n {result}")
    return result


