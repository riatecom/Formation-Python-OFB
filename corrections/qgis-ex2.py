import random

# On récupère une référence vers la couche qui nous intéresse
layer = QgsProject.instance().mapLayersByName('cities')[0]

# On crée une couche mémoire vide
mem_layer = QgsVectorLayer('Polygon?crs=EPSG:4326', 'cities-buffer', 'memory')
# On crée un fournisseur de données
pr = mem_layer.dataProvider()

# Spécification de deux champs
pr.addAttributes([
    QgsField("Buffer_value", QVariant.Double),
])
# On met à jour les champs
mem_layer.updateFields()

# On parcourt les entités de la couche
for feature in layer.getFeatures():
    ft = QgsFeature()
    # On calcule le buffer
    geom = QgsGeometry(feature.geometry())
    # On converti la géométrie dans un système de coordonnées permettant de calculer des distances
    geom.transform(QgsCoordinateTransform(layer.crs(), QgsCoordinateReferenceSystem("ESRI:53030"), QgsProject.instance()))
    # Calcul de la valeur aléatoire du buffer
    buffer_value = random.randint(10000, 200000)
    # Calcul du buffer
    buffer = geom.buffer(buffer_value, 5)
    # On remet la géométrie dans le système de coordonnées de la couche
    buffer.transform(QgsCoordinateTransform(QgsCoordinateReferenceSystem("ESRI:53030"), layer.crs(), QgsProject.instance()))
    # On ajoute la géométrie à l'entité
    ft.setGeometry(buffer)
    ft.setAttributes([buffer_value])
    # On ajoute l'entité à la couche mémoire
    pr.addFeatures([ft])

# On met à jour les limites de la couche mémoire
mem_layer.updateExtents()

# On ajoute la couche mémoire au projet
QgsProject.instance().addMapLayer(mem_layer)
