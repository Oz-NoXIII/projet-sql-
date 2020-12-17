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
    SQlLiteManage.execute(requete.name)
    return requete


def project(rel, *args):
    requete = OperateurUnitaire.project(rel, *args)
    SQlLiteManage.execute(requete.name)
    return requete


def rename(rel, old_name, new_name):
    requete = OperateurUnitaire.rename(rel, old_name, new_name)
    SQlLiteManage.execute(requete.name)
    return requete


def join(rel1, rel2):
    requete = OperateurBinaire.join(rel1, rel2)
    SQlLiteManage.execute(requete.name)
    return requete


def union(rel1, rel2):
    requete = OperateurBinaire.union(rel1, rel2)
    SQlLiteManage.relations_order(rel2, rel1)
    SQlLiteManage.execute(requete.name)
    return requete


def difference(rel1, rel2):
    requete = OperateurBinaire.difference(rel1, rel2)
    SQlLiteManage.relations_order(rel2, rel1)
    SQlLiteManage.execute(requete.name)
    return requete
