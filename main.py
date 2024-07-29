import matplotlib.pyplot as plt
import sympy
import numpy as np

def calculate_points(delta_x, delta_y, x0, y0, depth) -> tuple[list, list]:
    points_x = []
    points_y = []

    try:
        for _ in range(depth):
            x0 = x0 + delta_x.subs({'x': x0, 'y': y0})
            y0 = y0 + delta_y.subs({'x': x0, 'y': y0})
            points_x.append(float(x0))
            points_y.append(float(y0))

    except:
        print("Um erro ocorreu na execução do seu programa.")
        print("Verifique se o seu sistema possui solução.")
        exit(1)

    return points_x, points_y

def plot_function(f, g, plot_points_x, plot_points_y, axis_size) -> None:
    x_vals = np.linspace(-axis_size//2, axis_size//2, 1000)
    y_vals = np.linspace(-axis_size//2, axis_size//2, 1000)
    x, y = np.meshgrid(x_vals, y_vals)

    f_lambdified = sympy.lambdify(["x", "y"], f, 'numpy')
    g_lambdified = sympy.lambdify(["x", "y"], g, 'numpy')

    f_vals = f_lambdified(x, y)
    g_vals = g_lambdified(x, y)

    plt.figure(figsize=(16, 8))
    plt.contour(x, y, f_vals, levels=[0], colors='r', label='f(x,y)=0')
    plt.contour(x, y, g_vals, levels=[0], colors='b', label='g(x,y)=0')
    plt.scatter(plot_points_x, plot_points_y, c='green', label='Chutes')

    for i in range(len(plot_points_x)):
        plt.annotate(f"#{i+1}", (plot_points_x[i], plot_points_y[i]))

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Resultados Método de Newton')

    table_data = list(zip(range(1, len(plot_points_x) + 1), plot_points_x, plot_points_y))
    table_columns = ('Índice', 'x', 'y')
    plt.table(cellText=table_data, colLabels=table_columns, cellLoc='center', loc='right')
    plt.subplots_adjust(right=0.5)

    plt.show()

def main():
    f = sympy.sympify(input("f(x, y) = "))
    g = sympy.sympify(input("g(x, y) = "))
    x0, y0 = tuple(map(float, input("Chute inicial no formato a,b: ").strip().split(",")))
    axis_size = int(input("Tamanho do eixo: "))

    f_line_x = sympy.diff(f, "x")
    f_line_y = sympy.diff(f, "y")

    g_line_x = sympy.diff(g, "x")
    g_line_y = sympy.diff(g, "y")

    matrix = sympy.Matrix([[f_line_x, f_line_y], [g_line_x, g_line_y]])
    images = sympy.Matrix([f, g])

    delta_x, delta_y = matrix.inv() * (-images)

    depth = int(input("Depth: "))

    plot_points_x, plot_points_y = calculate_points(delta_x, delta_y, x0, y0, depth)
    plot_points_x.insert(0, x0)
    plot_points_y.insert(0, y0)

    plot_function(f, g, plot_points_x, plot_points_y, axis_size)
    plt.show()

if __name__ == "__main__":
    main()