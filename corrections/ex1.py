# 0. Import de la classe date depuis le module datetime
from datetime import date

# 1. Ouverture du fichier
with open('cities.csv', 'r') as f:
    data = f.read()

# 2. Corrections
data = data.replace('coord1', 'latitude')
data = data.replace('coord2', 'longitude')

# 3. Sauvegarde (dans un fichier différent, en prenant
#    soin d'ajouter la date du jour dans le nom du fichier)
with open(f'cities-{date.today()}.csv', 'w') as f:
    f.write(data)
