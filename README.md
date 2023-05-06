# Clip_MuLTY
Clipping Multiple Shapefiles with Single one
# Clip_MuLTY

Clip_MuLTY is written in python and use for clipped multiple layers using single shapefile.

## Prerequisites

Before running this code in your system you have to install `geopandas` library in your system. To install the `geopandas` library [click_Here](https://geopandas.org/en/stable/getting_started/install.html)

## Clip_MuLTY
Now we will breakdown and see how to execute the code: 

```bash
import geopandas
import os
```
These are import statements that import the `geopandas` and `os` modules. The `geopandas` module is used for working with geospatial data, and the `os` module provides a way to interact with the operating system.

```bash
input_folder = r"E:/Python_Tutorial/Shapefiles"
output_folder = r"E:/Python_Tutorial/output"
```
These lines set the input and output folder paths for the shapefiles that will be read and created, respectively. You can change the path as per your desired location.

```bash
clip_shapefile = r"E:/Python_Tutorial/clipped_shapefiles/clipped.shp"
```
In this line you mentioned your shapefile which is used for clipping all the shapefiles stored in folder.

 ```bash
clipper = gpd.read_file(clip_shapefile)
```
This line reads the shapefile used for clipping and stores it in the variable `clipper` using the `gpd.read_file()` method.

 ```bash
for filename in os.listdir(input_folder):
    if filename.endswith('.shp'):
        # load the shapefile
        shp = gpd.read_file(os.path.join(input_folder, filename))
```
These lines start a loop that will iterate over all the shapefiles in the `input_folder`. For each file, if the file extension is .shp, the file is read using `gpd.read_file()` and stored in the variable `shp`.

```bash
       clipped = gpd.clip(shp, clipper)
```
This line clips the `shp` shapefile using the `clipper` shapefile using the `gpd.clip()` method. The clipped shapefile is stored in the variable `clipped`.

```bash
       output_path = os.path.join(output_folder, filename)
```
This line sets the output path for the clipped shapefile using `os.path.join()` to concatenate the `output_folder` and the input `filename`.

```bash
       clipped.to_file(output_path)
```
This line saves the clipped shapefile to the output path using the `to_file()` method.

So now after explaining all the code line by line, here is the full code:

```bash
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
```

# Why used Clip_MuLTY
Clipping multiple shapefiles with a single shapefile at a time can have several benefits, including:

1. **Efficiency**: Instead of manually clipping each shapefile using the same clipper shapefile, automating the process can save time and effort.

2. **Consistency**: By using the same clipper shapefile for all the input shapefiles, the resulting clipped shapefiles will have consistent boundaries and can be used together in analyses or mapping.

3. **Accuracy**: Clipping multiple shapefiles with a single clipper shapefile can reduce the potential for errors and inconsistencies that can arise when manually clipping multiple shapefiles with different clipper shapefiles.

4. **Reproducibility**: By using a script to clip multiple shapefiles with a single clipper shapefile, the process can be easily reproduced and shared with others, ensuring consistency and accuracy across different users or projects.

Overall, clipping multiple shapefiles with a single shapefile at a time can improve efficiency, consistency, accuracy, and reproducibility in geospatial data processing and analysis.

## Contact ME
* Email: koushikghosh1a2s@gmail.com.

* LinkedIn: [Koushik Ghosh](https://www.linkedin.com/in/koushik-ghosh-490761192/)

* ResearchGate: [Koushik Ghosh](https://www.researchgate.net/profile/Koushik-Ghosh-23)



