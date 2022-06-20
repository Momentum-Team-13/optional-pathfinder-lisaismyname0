from PIL import Image, ImageDraw, ImageColor

with open("elevation_small.txt") as elevation_text:
    elevation_grid = elevation_text.readlines()
    x1 = elevation_grid[0].split()
    y_values = len(elevation_grid)
    print(y_values)
    x_values = len(x1)
    print(x_values)
    min_elevation1 = min(x1)
    max_elevation1 = max(x1)
    value = 0
    x_axis1 = dict.fromkeys(x1, value)
    for key in x_axis1:
        print(key)
        if int(key) >= 3859 and int(key) <= 3899:
            value = int(1)
            print(value)
        if int(key) >= 3900 and int(key) <= 3999:
            value = 2
            print(value)
        if int(key) >= 4000 and int(key) <= 4099:
            value = 3
            print(value)
        if int(key) >= 4100 and int(key) <= 4199:
            value = 4
            print(value)
        if int(key) >= 4200 and int(key) <= 4299:
            value = 5
            print(value)
        if int(key) >= 4300 and int(key) <= 4399:
            value = 6
            print(value)
        if int(key) >= 4400 and int(key) <= 4499:
            value = 7
            print(value)
        if int(key) >= 4500 and int(key) <= 4599:
            value = 8
            print(value)
        if int(key) >= 4600 and int(key) <= 4699:
            value = 9
        if int(key) >= 4700 and int(key) <= 4799:
            value = 10
            print(value)
        if int(key) >= 4800 and int(key) <= 4899:
            value = 11
            print(value)
        if int(key) >= 4900 and int(key) <= 4999:
            value = 12
            print(value)
        if int(key) >= 5000 and int(key) <= 5099:
            value = 13
        if int(key) >= 5100 and int(key) <= 5199:
            value = 14
            print(value)
        if int(key) >= 5200 and int(key) <= 5299:
            value = 15
            print(value)
        elif int(key) >= 5300 and int(key) <= 5399:
            value = 16
            print(value)
    map = Image.new("RGBA", (x_values, y_values), "white")
    for x in range(600):
        for y in range(1):
            if value == 1:
                map.putpixel((x, y), "black")
            if value == 2:
                map.putpixel((x, y), "red")
            if value == 3:
                map.putpixel((x, y), "green")
    map.save("map2.png")

    # i want to assign each elevation an RGB value to plot with the point(xy, fill) method

    """for example:
        if value = 1, RGB value = [0, 0, 0]"""

    """The point(xy, fill) method draws individual pixels. The xy argument represents a list of the points you want to draw. The list can be a list of x- and y-coordinate tuples, such as [(x, y), (x, y), ...], or a list of x- and y-coordinates without tuples, such as [x1, y1, x2, y2, ...]. The fill argument is the color of the points and is either an RGBA tuple or a string of a color name, such as 'red'. The fill argument is optional."""
