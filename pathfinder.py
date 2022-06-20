from re import X
from PIL import Image, ImageDraw, ImageColor


def createList(r1, r2):
    if (r1 == r2):
        return r1

    else:
        res = []
        while (r1 < r2+1):
            res.append(r1)
            r1 += 1
        return res


r1, r2 = 0, 600
list = createList(r1, r2)


with open("elevation_small.txt") as elevation_text:
    elevation_grid = elevation_text.readlines()
    x1 = elevation_grid[0].split()
    y_values = len(elevation_grid)
    x_values = len(x1)
    min_elevation1 = min(x1)
    max_elevation1 = max(x1)
    a = []
    elevation_dict1 = {i: x1[i] for i in range(0, len(x1))}
    print(elevation_dict1)
    print(len(elevation_dict1))

    # from here I want to use the draw.point()function where, key = position on x axis and y = the number of the list.... from there i can assign each dict value an rgb value

    # i want to assign each elevation an RGB value to plot with the point(xy, fill) method

    """for example:
        if value = 1, RGB value = [0, 0, 0]"""

    """The point(xy, fill) method draws individual pixels. The xy argument represents a list of the points you want to draw. The list can be a list of x- and y-coordinate tuples, such as [(x, y), (x, y), ...], or a list of x- and y-coordinates without tuples, such as [x1, y1, x2, y2, ...]. The fill argument is the color of the points and is either an RGBA tuple or a string of a color name, such as 'red'. The fill argument is optional."""
