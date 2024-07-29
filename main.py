import matplotlib.pyplot as plt
import sympy

def calculate_points(delta_x, delta_y, x0, y0, depth) -> list:
    points_x = []
    points_y = []

    try:
        for _ in range(depth):
            x0 = x0 + delta_x.subs({'x': x0, 'y': y0})
            y0 = y0 + delta_y.subs({'x': x0, 'y': y0})
            points_x.append(x0)
            points_y.append(x0)

    except:
        print("Um erro ocorreu na execução do seu programa.")
        print("Verifique se o seu sistema possui solução.")
        exit(1)

    return points_x, points_y

def main():

    f = sympy.sympify(input("f(x, y) = "))
    g = sympy.sympify(input("g(x, y) = "))
    x0, y0 = tuple(map(float, input("Initial guess in a,b format: ").strip().split(",")))

    f_line_x = sympy.diff(f, "x")
    f_line_y = sympy.diff(f, "y")

    g_line_x = sympy.diff(g, "x")
    g_line_y = sympy.diff(g, "y")

    matrix = sympy.Matrix([[f_line_x, f_line_y], [g_line_x, g_line_y]])
    images = sympy.Matrix([f, g])

    delta_x, delta_y = matrix.inv() * (-images)

    depth = int(input("Depth: "))

    plot_points_x, plot_points_y = calculate_points(delta_x, delta_y, x0, y0, depth)
        
    plt.plot()
    plt.scatter(plot_points_x, plot_points_y)
    plt.show()

if __name__ == "__main__":
    main()