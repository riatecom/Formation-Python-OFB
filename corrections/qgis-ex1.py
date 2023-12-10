from qgis.core import *
from qgis.gui import *
import math

@qgsfunction(args='auto', group='Custom', usesgeometry=True)
def get_utm_zone(feature, parent):
    """
    Return the UTM Zone of the
    feature's geometry as a String
    """
    # On récupère la géométrie de l'entité
    geom = feature.geometry()
    # On calcule le centroïde de la géométrie
    centroid = geom.centroid()
    # On récupère les coordonnées du centroïde
    pt = centroid.asPoint()
    longitude = pt.x()
    latitude = pt.y()
    # Calcul de la zone UTM
    zone_number = math.floor(((longitude + 180) / 6) % 60) + 1

    if latitude >= 0:
        zone_letter = 'N'
    else:
        zone_letter = 'S'

    return f"{int(zone_number)}{zone_letter}"

@qgsfunction(args='auto', group='Custom', usesgeometry=True)
def get_distance_to_paris(feature, parent):
    """
    Return the distance between
    the feature's geometry and Paris
    """
    # On récupère la géométrie de l'entité
    geom = feature.geometry()
    # On calcule le centroïde de la géométrie
    centroid = geom.centroid()
    # On récupère les coordonnées du centroïde
    pt = centroid.asPoint()
    longitude = pt.x()
    latitude = pt.y()
    # Calcul de la distance
    paris = QgsPointXY(2.3488, 48.8534)
    return pt.distance(paris)
