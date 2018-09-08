from vpython import *

sphere(pos=vector(1, 0, 0), radius=1, color=color.magenta)

arrow(pos=vector(1, 0, 0), axis=vector(+1, +3, -1,), color=color.green)

# You can add and subtract vectors

v1 = vector(1, 2, 3)
v2 = vector(-3, 1, -2)

v3 = v1 + v2
print(v3)