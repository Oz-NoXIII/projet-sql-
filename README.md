# projet-sql-

Outil de compilation (traduction) de requêtes SPJRUD vers des requêtes SQL

      Langage utilisé: Python

      Contributeurs: NYATCHO TONYA Frank
                     MUJYABWAMI Arsène
               
      Choix d'implémentation: 

                        a)Les relations sont définies par un objet Relation qui a deux attributs: un nom et un dictionnaire 
                        de listes de taille constante.
                        Nous avons fait ce choix car il facilite l'accès à la requête(le nom) et au attribut de la relation.
                        
                        b)La selection est une fonction à 5 paramètres: 1.La relation qui est une instance de Relation;
                        
                                                                        2.L'attribut qui doit être une clé du dictionnaire
                                                                        de relation;
                                                                        
                                                                        3.Le symbole qui doit faire partie de la liste
                                                                        prédéfini de symboles;
                                                                        
                                                                        4.La valeur qui doit être du même type que les
                                                                        valeurs de la liste pointée par l'attribut si 
                                                                        le compteur est différent de 1. Sinon, elle doit 
                                                                        être une clé du dictionnaire de relation;
                                                                        
                                                                        5.Le compteur qui définit si la valeur est une 
                                                                        clé ou une valeur du dictionnaire de relation. 
                                                                         
                        c)La projection est une fonction à paramètres variables: 1.La relation;
                                                                                  ***les attributs qui doivent être des 
                                                                                  clés du dictionnaire(supprime les doublons)
                          
                        d)La jointure sera une fonction à 2 paramètres: deux relations de mêmes attributs.
                          (à préciser)
                          
                        e)Le renommage sera une fonction à 3 paramètres:1.La relation dans laquelle l'action aura lieu;
                                                                        2.L'ancien nom de l'attribut;
                                                                        3.Le nouveau nom de l'attribut;
                                                                        
                        f)L'union sera une fonction à 2 paramètres: deux relations de mêmes attributs.
                          (supprime les doublons)
                          
                        g)La différence sera une fonction à 2 paramètres: deux relations de mêmes attributs.
                        
                        h)L'affichage d'une table ne sera possible qu'après la creation de cette table dans la base de données. 
                        Pour afficher une liste de tuple qu'une requête pourrrait créer sans créer la table dans la base de 
                        données, il faut passer par l'intermediaire de module SQlLiteManage et print(execute(la_requête)).
                        
                        i)La création d'une table peut se faire par l'intermediaire d'un nom et d'un dictionnaire 
                        (fonction relation) ou par l'intermédiaire d'un nom et d'une instance de relation c-à-d une requête.
                        
      Explication:
      
                        Pour utiliser cet outil de compilation (traduction) de requêtes SPJRUD vers des requêtes SQL, 
                        il suffit d'utiliser le module SPJRUDtoSQL qui contient 9 fonctions différentes: 
                        une fonction pour chaque opérateur unitaire ou binaire, une fonction display pour l'affichage,
                        une fonction create pour la création par résultat de requête et une fonction relation pour 
                        la création par dictionnaire python.
                        
                        Les requêtes imbriquées sont permises. (exemple: 
                        SPJRUDtoSQL.project((
                        SPJRUDtoSQL.select(
                        SPJRUDtoSQL.join(rel1, rel2),
                        "=", 'B', 3, 0)), # paramètres de la sélection
                        'A') # paramètre de la projection
                        est la projection de A sur la selection où B=3 sur la jointure de la relation 1 avec la relation 2)
                        
                        Les noms des attributs sont des str et doivent respecter les règles d'écriture de SQL.
                        
                        La fonction create est utilisable sur toutes les requêtes sauf celle qui font appele à la fonction 
                        rename car rename modifie la table de base.
         
      Difficultées:
      
                        La répartition des tâches a été un vrai défi tout comme la communication en générale et cela est surtout
                        dû aux circonstances exceptionnelles dans lesquelles nous nous trouvons actuellement, mais aussi par la 
                        découverte du projet le mois passé qui suivait justement la fin d'un autre projet d'un autre cours.
                        
                        La fonction rename ne nous a pas laissé le choix que de directement altérer la table dans la base de données
                        contrairement aux autres opérateurs.
                        
               
