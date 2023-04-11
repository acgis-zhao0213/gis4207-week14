# -*- coding: utf-8 -*-

import arcpy
import sys
import os

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "List"
        self.alias = "List fc"

        # List of tool classes associated with this toolbox
        self.tools = [FCLister]


class FCLister(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "List toolbox"
        self.description = "List"
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
       
        params0 = arcpy.Parameter(
            displayName="Root folder",
            name="root_folder",
            datatype="DEFolder",
            parameterType="Required",
            direction="Input")
        params1 = arcpy.Parameter(
                                    displayName="shp_type",
                                    name="shp_type",
                                    datatype="GPString",
                                
                                    parameterType="Required",
                                    direction="Input"
                                    )
        params1.filter.type = 'ValueList'
        params1.filter.list = ['Point', 'Polyline', 'Polygon']
        params2 = arcpy.Parameter(
            displayName="output file name",
            name="out_filename",
            datatype="GPString",
            parameterType="Required",
            direction="Input")                
       
        return [params0, params1, params2]
    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        
        root_folder = parameters[0].valueAsText
        shp_type = parameters[1].valueAsText
        out_filename = parameters[2].valueAsText
        _shp_types = ['Point', 'Polyline', 'Polygon']
        if not os.path.exists(root_folder):
            print(f"{root_folder} does not exist.")
            sys.exit(0)

        if not shp_type in _shp_types:
            print(f'{shp_type} is not valid.')
            print('Must be one of Point, Polyline, or Polygon')
            sys.exit(0)

        with open(out_filename, 'w') as outfile:
            walk = arcpy.da.Walk(root_folder, datatype="FeatureClass", type=shp_type)
            for ws, _, fc_list in walk:
                for fc in fc_list:
                    arcpy.AddMessage(os.path.join(os.path.abspath(ws), fc))
                    outfile.write(os.path.join(os.path.abspath(ws), fc) + '\n')
        print('Done')

        arcpy.AddMessage(f"under {root_folder} to {out_filename} ...")

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return
