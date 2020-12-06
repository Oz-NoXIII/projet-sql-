class Relation:
    def __init__(self, nom, dico):
        self.nom = nom
        isarelation(dico)
        self.dico = dico


class ErrorKey(Exception):
    """Exception qui signale une erreur au niveau des clés des dictionnaires"""
    pass


class ErrorType(Exception):
    """Exception qui signale une erreur au niveau des types"""
    pass


class ComparatorError(Exception):
    """Exception qui signale une erreur au niveau des comparateurs"""
    pass

class AttributesError(Exception):
    """Exception qui signale une erreur au niveau des attributs de relation"""
    pass

class NumberRelationError(Exception):
    """Exception qui signale une erreur au niveau du nombre de relation dans une operation binaire"""
    pass


def argsinrel(relation, args):
    """Fonction qui vérifie si tous les arguments dans args font partie de la relation rel et retourne True.

    Léve une erreur et retourne False sinon."""

    if type(relation) != Relation or type(args) != list:
        raise ErrorType()
    try:
        for arg in args:
            if arg not in relation.dico:
                raise ErrorKey()
        return True
    except ErrorKey:
        print(f"L'argument {arg} n'appartient pas à la relation {relation}.")
        return False


def removeduplicate(args):
    """Fonction qui supprime les doublons dans la liste"""

    if type(args) != list:
        raise ErrorType()
    new_args = []
    for i in range(len(args)):
        if args[i] not in new_args:
            new_args.append(args[i])
    return new_args


def isarelation(dico):
    """Fonction qui vérifie si toutes les clés pointent vers des listes non-vides de même taille contenant des éléments
    de même type"""

    if type(dico) != dict:
        raise ErrorType()
    len_is_cst(dico)
    for key in dico:
        if havesametype(dico[key]):
            return True

    return False

def len_is_cst(dico):
    """Fonction qui vérifie si toutes les clés pointent vers des listes non-vides de même taille et retourne True.

    Lève une erreur et retourne False sinon."""

    if type(dico) != dict:
        raise ErrorType()
    try:
        arelists(dico)
        premierPassage = True
        for argument in dico:
            if premierPassage:
                a = len(dico[argument])
                premierPassage = False
                if a == 0:
                    raise ErrorKey()
            elif len(dico[argument]) != a:
                raise ErrorKey()
        return True
    except ErrorKey:
        if a == 0:
            print(f"La clé {argument} pointe vers une liste vide.")
        else:
            print("Les tailles des listes ne sont pas constantes.")
        return False


def arelists(dico):
    """Fonction qui vérifie si toutes les clés pointent vers des listes et retourne True.

    Lève une erreur et retourne False sinon."""

    if type(dico) != dict:
        raise ErrorType()
    try:
        for argument in dico:
            if type(dico[argument]) != list:
                raise ErrorKey()
        return True
    except ErrorKey:
        print(f"La clé {argument} ne pointe pas vers une liste.")
        return False


def havesametype(args):
    """Fonction qui vérifie si toutes les éléments de la liste sont du même type et retourne True.

    Lève une erreur et retourne False sinon."""

    if type(args) != list:
        raise ErrorType()
    try:
        premierPassage = True
        for argument in args:
            if premierPassage:
                a = type(argument)
                premierPassage = False
            elif type(argument) != a:
                raise ErrorType()
        return True
    except ErrorType:
        if len(args) > 2:
            print(f"Il y a au moins deux types différents dans la liste dont {type(argument)} et {a}.")
        else:
            print(f"Format Incompatible: {type(argument)} différent de {a}")
        return False


def isarginrel(arg, rel):
    """Fonction qui retourne True si un argument arg est attribut de la relation rel.

    Retourne False sinon."""

    if type(rel) != Relation:
        raise ErrorType()
    if arg in rel.dico:
        return True
    else:
        return False


def joinable(rel1, rel2):
    """Fonction qui retourne True si deux relations possèdent au moins un attribut en commun.

    Retourne False sinon."""

    if type(rel1) != Relation or type(rel2) != Relation:
        raise ErrorType("Prends uniquement des relations en tant que paramètre!")
    for arg in rel1.dico:
        if isarginrel(arg, rel2):
            return True
    return False


def havesameargs(rel1, rel2):
    """Fonction qui retourne True si deux relations possèdent exactement les mêmes attributs.

    Retourne False sinon."""

    if type(rel1) != Relation or type(rel2) != Relation:
        raise ErrorType("Prends uniquement des relations en tant que paramètre!")
    for arg in rel1.dico:
        if not isarginrel(arg, rel2):
            return False
    return True
