#A sample code of drawing a star with 7 point is given below. 
#craete black background.
#on that create 50 starts of small size with different number of points(vertices) and different colors to craete colorful starry night.


import turtle as t
size = 300
points = 7
#angle = 144
angle = 180 - (180 / points)
t.color('yellow')
t.begin_fill()
for i in range(points):
    t.forward(size)
    t.right(angle)
t.end_fill()