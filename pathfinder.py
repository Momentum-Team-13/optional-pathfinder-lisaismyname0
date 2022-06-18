with open("elevation_small.txt") as elevation_text:
    elevation_grid = elevation_text.read()
    print(elevation_grid)

from PIL import Image
cat_pic = Image.open("cat.png")
print(cat_pic)
