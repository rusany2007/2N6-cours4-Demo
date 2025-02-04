import os
# # allez dans le dossier Ex3 Videos
info_env = os.environ
user = info_env.get("USERPROFILE")
(f"{user}/Documents")
os.chdir("Ex3 videos")

# # avec la boucle for, passez à travers chacun des dossiers de os.listdir()
for list in os.listdir():
    print(list)
# #     utilisez os.path.splitext pour obtenir le filename et l'extension
    print(os.path.splitext(f"{user}/Ex3 Videos"))

# #     utilisez split sur le filename pour obtenir le titre, le cours et le numéro du cours¸


for lit in os.listdir():
    titre,cours,numero = lit.split("_")
    print(titre,cours,numero)

# #     utilisez strip pour enlever les espaces qui pourraient rester pour le titre et le numéro
# #     en plus utilisez zfill pour remplir le numéro de sorte que 1 deviendra 01
# #     recréez le nouveau nom de fichier#   utliser os.rename pour renommer le fichier

for lit in os.listdir():
    titre,cours,numero = lit.split("_")
    place1 = numero.split("#")
    Nouveau_nom =f"{titre.strip()} {numero.strip()}  {place1[1].zfill(6)}"
    os.rename(lit,Nouveau_nom)


