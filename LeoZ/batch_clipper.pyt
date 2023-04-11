# -*- coding: utf-8 -*-

import arcpy
import os

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Batch clip"
        self.alias = "Batch clip"

        # List of tool classes associated with this toolbox
        self.tools = [BatchClipper]


class BatchClipper(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Batch"
        self.description = "Batch clipper"
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        
        param0 = arcpy.Parameter(
            displayName="Input Workspace",
            name="in_ws",
            datatype="DEWorkspace",
            parameterType="Required",
            direction="Input")
        param1 = arcpy.Parameter(
            displayName="Clip Features",
            name="clip_ws",
            datatype="DEWorkspace",
            parameterType="Required",
            direction="Input")
        param2 = arcpy.Parameter(
            displayName="Input Features",
            name="out_ws",
            datatype="DEWorkspace",
            parameterType="Required",
            direction="Input")                

        return [param0, param1, param2]

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
        in_ws   =  parameters[0].valueAsText
        clip_ws =  parameters[1].valueAsText
        out_ws  =  parameters[2].valueAsText

        for ws in [in_ws, clip_ws, out_ws]:
            if not arcpy.Exists(ws):
                print( "In Workspace '%s' does not exist" % in_ws)
                sys.exit()

        arcpy.env.workspace = in_ws
        in_fc_list = arcpy.ListFeatureClasses()

        arcpy.env.workspace = clip_ws
        clip_fc_list = arcpy.ListFeatureClasses()

        for in_fc in in_fc_list:
            in_fc_path = os.path.join(in_ws, in_fc)
            in_fc_base = arcpy.Describe(in_fc_path).basename
            for clip_fc in clip_fc_list:
                clip_fc_path = os.path.join(clip_ws, clip_fc)
                clip_fc_base = arcpy.Describe(clip_fc_path).basename
                out_fc  = f'{clip_fc_base}_{in_fc_base}'
                out_fc_path = os.path.join(out_ws, out_fc)
                print( (f'{out_fc} ...'))
                arcpy.Clip_analysis(in_fc_path,
                                    clip_fc_path,
                                    out_fc_path)

        arcpy.AddMessage(f'{in_ws} is clipped by {clip_ws}')
    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return
