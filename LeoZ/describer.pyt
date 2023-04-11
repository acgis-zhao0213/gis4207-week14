# -*- coding: utf-8 -*-

import arcpy

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = "toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [FCDescriber]


class FCDescriber(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Describer"
        self.description = "Describe"
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""

        param0= arcpy.Parameter(
            displayName="Feature Class",
            name="fc",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Input")        
        return [param0]

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
        """The source code of the tool."""
        fc = parameters[0].valueAsText

        if not arcpy.Exists(fc):
            print(fc + " does not exist")
            sys.exit()
        dsc = arcpy.da.Describe(fc)
        
        fields = dsc['fields']
        for field in fields:
            arcpy.AddMessage(f'{field.name:15} {field.type:15} {field.length:>3}')
    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return

       
