from fct_utile import removeduplicate, argsinrel, Relation, isarelation, ComparatorError, ErrorType, isarginrel, \
    havesametype


def select(relation, cmp, attrib, const, counter):
    """Fonction qui retourne une relation dont le name est la traduction de la selection en SPJRUD en SQL
    et le attributes est le attributes de la relation en paramètre
    """

    comparators = ['=', '<', '>', '<=', '>=', '!=']
    isarelation(relation.attributes)
    if comparators.count(cmp) == 0:
        raise ComparatorError("L'élément " + cmp + " est invalide pour cette operation. " +
                              f"Veuillez utiliser un des comparateurs suivants:{comparators}")
    if not isarginrel(attrib, relation):
        raise AttributeError(f"{attrib} n'est pas un attribut de la relation {relation}")

    # counter !=1 => attribut égal constante
    # counter=1 => attribut égal attribut
    if counter == 1:
        args = [relation.attributes[attrib][0], relation.attributes[const][0]]
        if not isarginrel(const, relation):
            raise AttributeError(f"{const} n'est pas un attribut de la relation {relation}")
        elif not havesametype(args):
            raise ErrorType(f"Dans les attributs: {relation.attributes[attrib][0]} et "
                            f"{relation.attributes[const][0]} doivent etre du même type")
    else:
        if type(relation.attributes[attrib][0]) != type(const):
            raise ErrorType(f"Dans les attributs: {relation.attributes[attrib][0]} et {const} doivent etre du meme type")
    name = f"SELECT * FROM {relation.nom} WHERE {attrib}{cmp}{const}"
    new_rel = Relation(name, relation.attributes)
    return new_rel


def project(relation, *args):
    """Fonction qui retourne une relation dont le name est la traduction de la projection en SPJRUD en SQL
    et le attributes est un dictionnaire qui décrit superficiellement la relation obtenue par la projection
    (mêmes attributs et types de valeurs)"""

    args = removeduplicate(args)
    argsinrel(relation, args)
    name = "select "
    for i in range(len(args)):
        if i != len(args) - 1:
            name += args[i] + ", "
        else:
            name += args[i] + f" from {relation.name}"
    attributes = {}
    for arg in args:
        if type(relation.attributes[arg][0]) == int:
            attributes[arg] = [1]
        elif type(relation.attributes[arg][0]) == str:
            attributes[arg] = ["a"]
        else:
            attributes[arg] = []
    new_rel = Relation(name, attributes)
    return new_rel


def rename():
    pass  # TODO
