class Relation:
    def __init__(self, nom, dico):
        self.nom = nom
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
