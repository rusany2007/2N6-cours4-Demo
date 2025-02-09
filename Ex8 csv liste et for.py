import os                             # N'enlevez pas ces lignes.
os.chdir(os.path.dirname(__file__))   # Elles permettent de se positionner dans le répertoire de ce script

# Importez csv


 

# Vous utiliserez encore le fichier "Ex7 Lan Party.csv"
# 
#         Créez une liste des jeux joués dans les différents Lan Party du fichier.
#         N'ajoutez à cette liste chaque jeu qu'une seule fois 
#                         (vérifiez si le jeu est dans la liste avant de l'ajouter
#                          vous pouvez vérifier avec l'instruction 'in'
#         Triez la liste en ordre aphabétique 
#         Finalement, imprimez la liste des différents jeux joués triés en ordre alphabétique


#         Si besoin, des instructions détaillées sont données plus bas
import csv

Csv = "Liste_jeux"

with open("csvs\\Ex7 Lan Party.csv","r",encoding="utf-8") as file:
    reader = csv.reader(file,delimiter=";")
    next(reader)
    for line in reader:
        lines = line.copy()
        top1 = line[1] 
        top2 = line[2]
        top3 = line[3]

        with open ("Liste_jeux.list","w",encoding="utf-8",newline="") as files :
            csv_writer = csv.writer(files,delimiter="\n")
            for linge in line:
               csv_writer.writerows(linge)




















# INSTRUCTIONS DÉTAILLÉES
#      Commencez par créer une liste des différents jeux vide
#      Ouvrez le fichier 'Ex4 Lan Party.csv' en lecture
#      utilisez csv.reader pour lire le fichier avec le bon delimiter
#      Sautez la première ligne de l'entête
#      Faites une boucle pour passer à travers chacune des lignes 
#      Utilisez le slicing pour garder uniquement les 3 jeux
#      Faites une boucle pour passer à travers chacun des jeux
#      Avec count, obtenez le nombre de fois que le jeu est dans votre liste des différents jeux
#      Si le count est de 0, vous ne l'avez jamais ajouté alors ajoutez le jeu à votre liste
#      En dehors de toute boucle, utilisez sorted() pour trier la liste et obtenir une nouvelle liste triée
#      Imprimez votre nouvelle liste triée


