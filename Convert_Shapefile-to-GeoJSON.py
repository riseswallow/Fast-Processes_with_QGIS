#------------------CONVERT SHAPEFILE TO GEOJSON -------------------

import os

from qgis.core import QgsCoordinateReferenceSystem, QgsVectorLayer, QgsVectorFileWriter

# Setting workspace
workspace = "C:\\data"

# Setting out path file
out_file = "C:\\data\\out"

# Setting Coordinate Reference System WGS84
reference_system = QgsCoordinateReferenceSystem(4326)

# Try convert shapefile to GeoJSON
try:

    # For each shapefile in workspace
    for row in os.listdir(workspace):

        # Find the geometry file
        if row[-4:] == '.shp':
            
            # Get the name file
            markup = row.find(".")
            geoJson_name = row[:markup] + ".geojson"

            # Create a new temporary layer
            vector_lyr = QgsVectorLayer(workspace + "\\" + row, row[:markup], "ogr")
            vector_lyr .setProviderEncoding(u'latin1')
            vector_lyr .dataProvider().setEncoding(u'latin1')

            # Convert the layer to GeoJSON file
            print "Converting Shapefile to GeoJSON"
            QgsVectorFileWriter.writeAsVectorFormat(vector_lyr, out_file + '\\' + geoJson_name, "latin1", reference_system, "GEOJSON")

            print "Success!"
except:
    print "It was not possible to convert shapefile to GeoJSON"
