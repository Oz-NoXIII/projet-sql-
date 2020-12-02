import fct_utile


def select():
    pass


def project(relation, *args):
    """Fonction qui retourne le str qui est la traduction de la projection en SPJRUD en SQL """
    # print(args)
    args = fct_utile.removeduplicate(args)
    # print(args)
    fct_utile.argsinrel(relation.dico, args)
    sol = "select "
    for i in range(len(args)):
        if i != len(args) - 1:
            sol += args[i] + ", "
        else:
            sol += args[i] + f" from {relation.nom}"
            return sol


def rename():
    pass
