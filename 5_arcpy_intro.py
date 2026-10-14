#ArcPy_Intro.py - An introduction to using the ArcPy module

#%% Import the module
import arcpy

#%% List the functions
funcList = dir(arcpy)
print(len(funcList))

#%% Print the help
help(arcpy)

#%% Print help on the spatial analyst "Slope" tool
help(arcpy.sa.Slope)

#%% Add parentheses after the command to display contextual help
arcpy.analysis.Buffer

