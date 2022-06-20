from re import X
from PIL import Image, ImageDraw, ImageColor

with open("elevation_small.txt") as elevation_text:
    elevation_grid = elevation_text.readlines()
    x1 = elevation_grid[0].split()
    print(type(x1))
    y_values = len(elevation_grid)
    x_values = len(x1)
    min_elevation1 = min(x1)
    max_elevation1 = max(x1)
    a = []
    elevation_dict1 = {str(key): x1[key] for key in range(0, len(x1))}
    print(elevation_dict1.keys(), elevation_dict1.values())
    for num in elevation_dict1.values():
        num = int(num)
        if num >= 3859 and num <= 3899:
            color_code = 1
            print(f"{num}'s color code is {color_code}")
        if num >= 3900 and num <= 3999:
            color_code = 2
            print(f"{num}'s color code is {color_code}")
        if num >= 4000 and num <= 4099:
            color_code = 3
            print(f"{num}'s color code is {color_code}")
        if num >= 4100 and num <= 4199:
            color_code = 4
            print(f"{num}'s color code is {color_code}")
        if num >= 4200 and num <= 4299:
            color_code = 5
            print(f"{num}'s color code is {color_code}")
        if num >= 4300 and num <= 4399:
            color_code = 6
            print(f"{num}'s color code is {color_code}")
        if num >= 4400 and num <= 4499:
            color_code = 7
            print(f"{num}'s color code is {color_code}")
        if num >= 4500 and num <= 4599:
            color_code = 8
            print(f"{num}'s color code is {color_code}")
        if num >= 4600 and num <= 4699:
            color_code = 9
        if num >= 4700 and num <= 4799:
            color_code = 10
            print(f"{num}'s color code is {color_code}")
        if num >= 4800 and num <= 4899:
            color_code = 11
            print(f"{num}'s color code is {color_code}")
        if num >= 4900 and num <= 4999:
            color_code = 12
            print(f"{num}'s color code is {color_code}")
        if num >= 5000 and num <= 5099:
            color_code = 13
        if num >= 5100 and num <= 5199:
            color_code = 14
            print(f"{num}'s color code is {color_code}")
        if num >= 5200 and num <= 5299:
            color_code = 15
            print(f"{num}'s color code is {color_code}")
        elif num >= 5300 and num <= 5399:
            color_code = 16
            print(f"{num}'s color code is {color_code}")
    for key in range(600):
        for y in range(1):
            if color_code == 1:
                map.putpixel((key, y), ("black"))
            if color_code == 2:
                map.putpixel((key, y), ("red"))
    map = Image.new("RGBA", (x_values, y_values))
    map.save("map2.png")
# from here I want to use the draw.point()function where, key = position on x axis and y = the number of the list.... from there i can assign each dict value an rgb value

# i want to assign each elevation an RGB value to plot with the point(xy, fill) method

"""for example:
        if value = 1, RGB value = [0, 0, 0]"""

"""The point(xy, fill) method draws individual pixels. The xy argument represents a list of the points you want to draw. The list can be a list of x- and y-coordinate tuples, such as [(x, y), (x, y), ...], or a list of x- and y-coordinates without tuples, such as [x1, y1, x2, y2, ...]. The fill argument is the color of the points and is either an RGBA tuple or a string of a color name, such as 'red'. The fill argument is optional."""
