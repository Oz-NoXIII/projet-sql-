# projet-sql-

Outil de compilation (traduction) de requêtes SPJRUD vers des requêtes SQL

      Langage utilisé: Python

      Contributeurs: TONYA Franck
                     MUJYABWAMI Arsène
               
      Choix d'implémentation: 

                        a)Les relations seront définies comme des dictionnaires de liste de taille constante.
                        b)La selection sera une fonction à 4 paramètres: 1.La relation qui est un dictionnaire;
                                                                         2.L'attribut qui doit être une clé du dictionnaire;
                                                                         3.Le symbole qui devra faire partie de la liste prédéfini de symboles;
                                                                         4.La valeur qui devra être du même type que les valeurs de la liste pointée par l'attribut.
                                                                         
                        c)La projection sera une fonction à paramètres variables: 1.La relation;
                                                                                  ***les attributs qui doivent être des clés du dictionnaire
                          (supprime les doublons)
                          
                        d)La jointure sera une fonction à 2 paramètres: deux relations de mêmes attributs.
                          (à préciser)
                          
                        e)Le renommage sera une fonction à 3 paramètres:1.La relation dans laquelle l'action aura lieu;
                                                                        2.L'ancien nom de l'attribut;
                                                                        3.Le nouveau nom de l'attribut;
                                                                        
                        f)L'union sera une fonction à 2 paramètres: deux relations de mêmes attributs.
                          (supprime les doublons)
                          
                        g)La différence sera une fonction à 2 paramètres: deux relations de mêmes attributs.
               
