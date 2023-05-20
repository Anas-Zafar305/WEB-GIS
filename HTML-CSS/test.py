import arcpy
from arcpy import env
env.workspace = "G:\\ANAS_ZAFAR_DON_OF_THE_ERA\\Semester 6\\GIS PROGRAMMING\\Lesson1"
fclist = arcpy.ListFeatureClasses()
print(fclist)