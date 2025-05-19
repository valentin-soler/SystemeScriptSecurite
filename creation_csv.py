import csv

#Tableau data csv
data = [["Jean",25,"Paris"],["Marie",30,"Lyon"],["Paris",22,"Marseille"],["Sophie",35,"Toulouse"]]

#Nom fichier CSV en sortie
filename="out.csv"

#Création du fichier CSV
with open(filename,"w",newline='') as file:
    writer=csv.writer(file)
    #En-tête
    writer.writerow(["Nom", "Age", "Ville"])
    writer.writerows(data)