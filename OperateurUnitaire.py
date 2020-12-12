import fct_utile
from fct_utile import ErrorType,isarelation,ComparatorError

def select(relation,cmp,attrib,const):
    comparators=['=','<','>','<=','>=','!=']

    isarelation(relation.dico)

    if comparators.count(cmp)==0:
        print("Veuillez utiliser un des comparateurs suivants: =,<,>,<=,>=,!=")
        raise ComparatorError("l'element "+cmp+" est invalide pour cette operation")
    elif type(attrib) != type(const):
        raise ErrorType(f"Les attributs: {attrib} et {const} doivent etre du même type")
    else:
        query = f"SELECT * FROM {relation.nom} WHERE {attrib}{cmp}{const}";
        print(query);


def project(relation, *args):
    """Fonction qui retourne le str qui est la traduction de la projection en SPJRUD en SQL """

    args = fct_utile.removeduplicate(args)
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


