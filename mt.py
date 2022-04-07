#Written by Conrad Lee 

from PIL import Image
import os
  
for file in os.listdir('Blend map'):
    name = file.split("_")
    newpath = name[0]+"_"+name[1]
    img = Image.open(f'Blend map/{newpath}_blend_map.png')
    img = img.convert("RGBA")

    datas = img.getdata()

    newData = []

    for items in datas:
        if items[0] == 255 and items[1] == 255 and items[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(items)

    img.putdata(newData)
    img.save(f"Transparent Blend map/{newpath}transparent_blend_map.png", "PNG")
    print("Successful")
