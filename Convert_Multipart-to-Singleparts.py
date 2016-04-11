#========================Multipart to singleparts===============================
""""
Processs to save and to run in conslose python from QGIS
"""

import os
import processing

# Setting the process to run in QGIS
processing.alglist("Multipart to singleparts")

# Setting the path for input and out put shapefile
workspace = "C:\\data"

try:
	
    # For each shapefile in workspace
    for row in os.listdir(workspace):

        # Find the geometry file
        if row[-4:] == '.shp':

            # Get the path of shapefile
            filePath = str(workspace) + "\\" + row

	    # Get the name new file
            markup = row.find(".")
            newFileName = str(workspace) + "\\" + row[:markup] + "_singlePart.shp"

            # Convert the layer to kml file
            print "Converting multipart to singleparts"
            processing.runalg("qgis:multiparttosingleparts",filePath,newFileName)

            print "Success!"
except:
    print "It was not possible to convert multipart to singleparts"
