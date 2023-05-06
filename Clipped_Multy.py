#!/usr/bin/env python
# coding: utf-8

# In[4]:


import geopandas as gpd
import os
# set input and output paths
input_folder = r"E:/Python_Tutorial/Shapefiles"
output_folder = r"E:/Python_Tutorial/output"
# set the shapefile used for clipping
clip_shapefile = r"E:/Python_Tutorial/clipped_shapefiles/clipped.shp"

# load the clipping shapefile
clipper = gpd.read_file(clip_shapefile)
# loop through all shapefiles in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.shp'):
        # load the shapefile
        shp = gpd.read_file(os.path.join(input_folder, filename))
        
        # clip the shapefile using the clipping shapefile
        clipped = gpd.clip(shp, clipper)
        
        # set the output path
        output_path = os.path.join(output_folder, filename)
        
        # save the clipped shapefile to the output path
        clipped.to_file(output_path)


# In[ ]:




