##Written by Conrad Lee (https://github.com/conrad45605/)


from PIL import Image
import os

directory = os.getcwd()
for filename in os.listdir(directory):
    f = os.path.join(filename)
    name = f.split("_")
    newpath = name[0]+"_"+name[1]

    bg = Image.open(f"{newpath}/{newpath}_GATA3.tif")
    fg = Image.open(f"{newpath}/{newpath}_MMG.tif")
    firstblend = Image.blend(bg, fg, .33)
    
    fgg = Image.open(f"{newpath}/{newpath}_GCDFP.tif")
    secondblend = Image.blend(firstblend, fgg, .33)
    blendmap = secondblend.save(f"../Blend map/{newpath}_blend_map.png")
    
    h = Image.open(f"../Haematoxylin only/{newpath}_composite_image.tif")
    blend = Image.blend(secondblend, h, .77).save(f"Nucleus map/{newpath}_blend.png")