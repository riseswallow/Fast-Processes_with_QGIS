#------------------CONVERT SHAPEFILE TO CSV file -------------------

import os

from qgis.core import QgsCoordinateReferenceSystem, QgsVectorLayer, QgsVectorFileWriter

# Setting workspace
workspace = "C:\\data"

# Setting out path file
out_file = "C:\\data\\out"

# Setting Coordinate Reference System WGS84
reference_system = QgsCoordinateReferenceSystem(4326)

# Try convert shapefile to CSV
try:

    # For each shapefile in workspace
    for row in os.listdir(workspace):

        # Find the geometry file
        if row[-4:] == '.shp':

            # Get the name file
            markup = row.find(".")
            csv_name = row[:markup] + ".csv"

            # Create a new temporary layer
            vector_lyr = QgsVectorLayer(workspace + "\\" + row, row[:markup], "ogr")
            vector_lyr .setProviderEncoding(u'latin1')
            vector_lyr .dataProvider().setEncoding(u'latin1')

            # Convert the layer to CSV file
            print "Converting Shapefile to CSV"
            QgsVectorFileWriter.writeAsVectorFormat(vector_lyr, out_file + '\\' + csv_name, "latin1", reference_system, "CSV")

            print "Success!"
except:
    print "It was not possible to convert shapefile to CSV file"
