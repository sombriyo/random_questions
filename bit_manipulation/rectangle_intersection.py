'''
Find the number of  overlapping rectangles
from the given coordinates 
And return the coordinates of overlapping triangles

'''

from collections import namedtuple
#namedtuple support indexing starting from 0
rectangle = namedtuple('Rectangle',('x', 'y', 'width', 'height'))



def intersect_rectangle(r1,r2):
    def is_intersect(r1, r2):
        if ((r1.x <= (r2.x + r2.width) and (r1.x + r1.width) >= r2.x ) and
                (r1.y <= (r2.y +r2.height) and (r1.y + r1.height) >= r2.y)):
            return True

    if not is_intersect(r1,r2):
        return 'No overlapping'
    x = max(r1.x, r2.x)
    y =  max(r1.y, r2.y)
    width = min((r1.x + r1.width), (r2.x + r2.width)) - max(r1.x, r2.x)
    height = min((r1.y + r1.height), (r2.y + r2.height)) - max(r1.y, r2.y)

    return rectangle(x,y, width, height)

r1 = rectangle(5,3,2,4)
r2 = rectangle(2,3,4,3)

print(intersect_rectangle(r1,r2))
