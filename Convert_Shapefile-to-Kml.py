#------------------CONVERT SHAPEFILE TO KML -------------------
import os

from qgis.core import QgsCoordinateReferenceSystem, QgsVectorLayer

# Setting workspace
workspace = "C:\\data\\shapefile"

# Setting out path file
out_file = "C:\\data\\out"

# Setting Coordinate Reference System WGS84
reference_system = QgsCoordinateReferenceSystem(4326)

# Try convert shapefile to kml
try:

    # For each shapefile in workspace
    for row in os.listdir(workspace):

        # Find the geometry file 
        if row[-4:] == '.shp':

            # Get the name file
            markup = row.find(".")
            kml_name = row[:markup] + ".kml"
            
            # Create a new temporary layer
            vector_lyr = QgsVectorLayer(workspace + "\\" + row, row[:markup], "ogr")

            # Convert the layer to kml file
            print "Converting Shapefile to Kml"
            QgsVectorFileWriter.writeAsVectorFormat(vector_lyr, out_file + '\\' + kml_name, "utf-8", reference_system, "KML")
            
            print "Success!"
except:
    print "It was not possible to convert shapefile to kml"
