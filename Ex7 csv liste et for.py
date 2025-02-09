import os                             # N'enlevez pas ces lignes.
os.chdir(os.path.dirname(__file__))   # Elles permettent de se positionner dans le répertoire de ce script

# Importez csv
import csv

 

# Regardez le contenu du fichier "Ex7 Lan Party.csv"
#          Observez que dans ce fichier, la première ligne comprends les en-têtes de colonne 
#                 Lan Party;Top 1;Top 2; Top 3
#          Top 1, Top 2 et Top 3 sont les jeux les plus populaires dans chaque Lan Party
#          
#          Vous aimez jouer à Valorant
#          Imprimez la liste des Lan Party dans lesquels votre jeu préféré est parmi leurs Tops
# 
#          Aucune instruction détaillée n'est donnée plus bas

with open("csvs\\Ex7 Lan Party.csv","r",encoding="utf-8") as file:
    reader = csv.reader(file,delimiter=";")
    next(reader)
    for line in reader:
        lines = line.copy()
        top1 = line[1] 
        top2 = line[2]
        top3 = line[3]
        if top2=="Valorant" or top3=="Valorant" or top1=="Valorant":
            print (line)


