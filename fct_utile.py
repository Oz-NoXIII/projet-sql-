class Relation:
    def __init__(self, name, attributes):
        self.name = name
        isarelation(attributes)
        self.attributes = attributes
        # create(name, attributes) TODO regler le problème d'import


class AttributesError(Exception):
    """Exception qui signale une erreur au niveau des attributs des relations"""
    pass


class ErrorType(Exception):
    """Exception qui signale une erreur au niveau des types"""
    pass


class ComparatorError(Exception):
    """Exception qui signale une erreur au niveau des comparateurs"""
    pass


def argsinrel(relation, args):
    """Fonction qui vérifie si tous les arguments dans args font partie de la relation rel et retourne True.

    Léve une erreur et retourne False sinon.

    :param relation:
    :param args:
    :return: True or False
    """

    if type(relation) != Relation or type(args) != list:
        raise ErrorType()
    try:
        for arg in args:
            if arg not in relation.attributes:
                raise AttributesError()
        return True
    except AttributesError:
        print(f"L'argument {arg} n'appartient pas à la relation {relation.name} {relation.attributes}.")
        return False


def removeduplicate(args):
    """Fonction qui supprime les doublons dans un tuple et retourne une liste.

    :param args:
    :return:
    """

    if type(args) != tuple:
        raise ErrorType()
    new_args = []
    for i in range(len(args)):
        if args[i] not in new_args:
            new_args.append(args[i])
    return new_args


def isarelation(attributes):
    """Fonction qui vérifie si toutes les attributs pointent vers des listes non-vides de même taille contenant
     des éléments de même type et retourne True.

    :param attributes:
    :return: True
    """

    if type(attributes) != dict:
        raise ErrorType()
    len_is_cst(attributes)
    for attribute in attributes:
        havesametype(attributes[attribute])
    return True


def len_is_cst(attributes):
    """Fonction qui vérifie si toutes les attributs pointent vers des listes non-vides de même taille et retourne True.

    Lève une erreur et retourne False sinon.

    :param attributes:
    :return: True or False
    """

    if type(attributes) != dict:
        raise ErrorType()
    try:
        arelists(attributes)
        premierPassage = True
        for attribute in attributes:
            if premierPassage:
                a = len(attributes[attribute])
                premierPassage = False
                if a == 0:
                    raise AttributesError()
            elif len(attributes[attribute]) != a:
                raise AttributesError()
        return True
    except AttributesError:
        if a == 0:
            print(f"L'attribut {attribute} pointe vers une liste vide.")
        else:
            print("Les tailles des listes ne sont pas constantes.")
        return False


def arelists(attributes):
    """Fonction qui vérifie si toutes les clés pointent vers des listes et retourne True.

    Lève une erreur et retourne False sinon.

    :param attributes:
    :return: True or False
    """

    if type(attributes) != dict:
        raise ErrorType()
    try:
        for attribute in attributes:
            if type(attributes[attribute]) != list:
                raise AttributesError()
        return True
    except AttributesError:
        print(f"L'attribut {attribute} ne pointe pas vers une liste.")
        return False


def havesametype(args):
    """Fonction qui vérifie si toutes les éléments de la liste sont du même type et retourne True.

    Lève une erreur et retourne False sinon.

    :param args:
    :return: True or False
    """

    if type(args) != list:
        raise ErrorType()
    try:
        premierPassage = True
        for arg in args:
            if premierPassage:
                a = type(arg)
                premierPassage = False
            elif type(arg) != a:
                raise ErrorType()
        return True
    except ErrorType:
        if len(args) > 2:
            print(f"Il y a au moins deux types différents dans la liste dont {type(arg)} et {a}.")
        else:
            print(f"Format Incompatible: {type(arg)} différent de {a}")
        return False


def isarginrel(arg, rel):
    """Fonction qui retourne True si un argument arg est attribut de la relation rel.

    Retourne False sinon.

    :param arg:
    :param rel:
    :return: True or False
    """

    if type(rel) != Relation:
        raise ErrorType()
    if arg in rel.attributes:
        return True
    else:
        return False


def joinable(rel1, rel2):
    """Fonction qui retourne True si deux relations possèdent au moins un attribut en commun.

    Retourne False sinon.

    :param rel1:
    :param rel2:
    :return: True or False
    """

    if type(rel1) != Relation or type(rel2) != Relation:
        raise ErrorType("Prends uniquement des relations en tant que paramètre!")
    for arg in rel1.attributes:
        if isarginrel(arg, rel2):
            return True
    return False


def havesameattributes(rel1, rel2):
    """
    Fonction qui retourne True si deux relations possèdent exactement les mêmes attributs ayant des valeurs de même
    type.

    Retourne False sinon.

    :param rel1:
    :param rel2:
    :return: True or False
    """

    if type(rel1) != Relation or type(rel2) != Relation:
        raise ErrorType("Prends uniquement des relations en tant que paramètre!")
    if len(rel1.attributes) != len(rel2.attributes):
        return False
    for arg in rel1.attributes:
        if not isarginrel(arg, rel2):
            return False
        else:
            a = rel1.attributes[arg]
            b = rel2.attributes[arg]
            args = [a[0], b[0]]
            if not havesametype(args):
                return False
    return True


def listofkey(dictionnaire):
    """ Fonction qui retourne une liste des clès d'un dictionnaire

    :param dictionnaire:
    :return keys:
    """
    keys = []
    for key in dictionnaire:
        keys.append(key)
    return keys


def nameandtype(dictionnaire, keys):
    """Fonction qui prends un dictionnaire de liste en paramètre
    et retourne un str des noms des clés avec le type SQL
    des valeur de la liste contenue dans cette clé

    exemple: dict["a"]=2 retournera 'a integer'

    Correspondance Type python-SQl

    None           <=> null

    int            <=> integer

    float          <=> real

    str            <=> text
    """

    s = ""
    c = 0
    for i in range(len(keys)):
        if not dictionnaire[keys[i]]:
            s += keys[i] + " null"
            c += 1
        elif type(dictionnaire[keys[i]][0]) == int:
            s += keys[i] + " integer"
            c += 1
        elif type(dictionnaire[keys[i]][0]) == float:
            s += keys[i] + " real"
            c += 1
        elif type(dictionnaire[keys[i]][0]) == str:
            s += keys[i] + " text"
            c += 1
        if c != len(dictionnaire):
            s += ", "

    return s


def linedata(dictionnaire, keys, indice):
    """Fonction qui retourne un tuple contenant
    les éléments du dictionnaire se trouvant à l'indice indice
    des listes pointés par les clés keys

    :param dictionnaire:
    :param keys:
    :param indice:
    :return: tuple(l)
    """
    l = []
    for i in range(len(keys)):
        l.append(dictionnaire[keys[i]][indice])
    return tuple(l)


def data(dictionnaire, keys):
    """Fonction qui retourne les données à insérer dans une table

    :param dictionnaire:
    :param keys:
    :return: d
    """
    d = []
    for i in range(len(dictionnaire[keys[0]])):
        d.append(linedata(dictionnaire, keys, i))
    return d
