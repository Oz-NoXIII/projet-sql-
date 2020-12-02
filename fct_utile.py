class Relation:
    def __init__(self, nom, dico):
        self.nom = nom
        isarelation(dico)
        self.dico = dico


class ErrorKey(Exception):
    """Exception qui signale une erreur au niveau des clés des dictionnaires"""
    pass


def argsinrel(relation, args):
    """Fonction qui vérifie si tous les arguments dans args font partie de la relation rel.

    Léve une erreur sinon."""
    try:
        for arg in args:
            if arg not in relation:
                raise ErrorKey()
    except ErrorKey:
        print(f"L'argument {arg} n'appartient pas à la relation {relation}.")


def removeduplicate(args):
    new_args = []
    for i in range(len(args)):
        if args[i] not in new_args:
            new_args.append(args[i])
    return new_args


def isarelation(dico):
    """Fonction qui vérifie si toutes les clés pointent vers des listes de même taille contenant des éléments de même type

        Lève une erreur sinon"""
    try:
        len_is_cst(dico)
        for key in dico:
            havesametype(key)
    except ErrorKey:
        print("Ce n'est pas une relation acceptable.")


def len_is_cst(dico):
    """Fonction qui vérifie si toutes les clés pointent vers des listes de même taille

    Lève une erreur sinon"""
    try:
        arelists(dico)
        premierPassage = True
        for argument in dico:
            if premierPassage:
                a = len(argument)
                premierPassage = False
            elif len(argument) != a:
                raise ErrorKey()
    except ErrorKey:
        print("Les tailles des listes ne sont pas constantes.")


def arelists(dico):
    """Fonction qui vérifie si toutes les clés pointent vers des listes

       Lève une erreur sinon"""
    try:
        for argument in dico:
            if type(argument) != list:
                raise ErrorKey()
    except ErrorKey:
        print(f"La clé {argument} ne pointe pas vers une liste.")


def havesametype(args):
    """Fonction qui vérifie si toutes les éléments de la liste sont du même type

        Lève une erreur sinon"""
    try:
        premierPassage = True
        for argument in args:
            if premierPassage:
                a = type(argument)
                premierPassage = False
            elif type(argument) != a:
                raise ErrorKey()
    except ErrorKey:
        print(f"Les éléments de la liste ne sont pas du même type.")
