import matplotlib as plt
import sympy

f = sympy.sympify(input())
g = sympy.sympify(input())
guess = (2, 1)

f_line_x = sympy.diff(f, "x")
f_line_y = sympy.diff(f, "y")

g_line_x = sympy.diff(g, "x")
g_line_y = sympy.diff(g, "y")

matrix = sympy.Matrix([[f_line_x, f_line_y], [g_line_x, g_line_y]])
matrix = matrix**-1
images = sympy.Matrix([f, g])

delta_x, delta_y = matrix * -images

print(matrix)
print(delta_x)
print(delta_y)

x0 = guess[0]
y0 = guess[1]

max_layers = 10
for i in range(max_layers):
    x0 = x0 + delta_x.subs([("x", x0), ("y", y0)])
    y0 = y0 + delta_y.subs([("x", x0), ("y", y0)])

    print(x0, y0)