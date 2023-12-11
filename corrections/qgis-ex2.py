import random

layer = QgsProject.instance().mapLayersByName('ne_10m_populated_places_simple')[0]

# On crée une couche mémoire vide
mem_layer = QgsVectorLayer('Polygon?crs=EPSG:4326', 'cities-buffer', 'memory')
pr = mem_layer.dataProvider()

# Spécification de deux champs
pr.addAttributes([
    QgsField("Buffer_value", QVariant.Double),
])
mem_layer.updateFields()

for feature in layer.getFeatures():
    ft = QgsFeature()
    # On calcule le buffer
    geom = QgsGeometry(feature.geometry())
    buffer_value = random.randint(1, 20)
    buffer = geom.buffer(buffer_value, 5)
    # On ajoute la géométrie à l'entité
    ft.setGeometry(buffer)
    ft.setAttributes([buffer_value])
    # On ajoute l'entité à la couche mémoire
    pr.addFeature(ft)

mem_layer.updateExtents()

# On ajoute la couche mémoire au projet
QgsProject.instance().addMapLayer(mem_layer)
