import matplotlib.pyplot as plt
from cubic_spline_3d import *


def calculate_3d_spline_interpolation(x: list, y: list, z: list, num=100):
    cubic_spline_3d = CubicSpline3D(x, y, z)
    params = np.linspace(cubic_spline_3d.params[0], cubic_spline_3d.params[-1], num + 1)[:-1]
    result_x, result_y, result_z = [], [], []
    for param in params:
        point_x, point_y, point_z = cubic_spline_3d.point(param)
        result_x.append(point_x)
        result_y.append(point_y)
        result_z.append(point_z)
    return result_x, result_y, result_z

def calculate_2d_spline_interpolation(x: list, y: list, num=100):
    cubic_spline_2d = CubicSpline2D(x, y)
    params = np.linspace(cubic_spline_2d.params[0], cubic_spline_2d.params[-1], num + 1)[:-1]
    result_x, result_y = [], []
    for param in params:
        point_x, point_y = cubic_spline_2d.point(param)
        result_x.append(point_x)
        result_y.append(point_y)
    return result_x, result_y

if __name__ == '__main__':
    x_points = []
    y_points = []
    z_points = []
    # fig, ax = plt.subplots(figsize=(9, 9), num="Cubic Splines Simple App")
    fig = plt.figure()
    # ax = plt.axes(projection='3d')
    ax = plt.axes(projection='3d')


    curve, = ax.plot(x_points, y_points,  z_points, label="spline")
    points, = ax.plot(x_points, y_points, z_points, "x")

    def on_click(event):
        x_new_point = float(input("Введите координату x: "))
        y_new_point = float(input("Введите координату y: "))
        z_new_point = float(input("Введите координату z: "))
        x_points.append(x_new_point)
        y_points.append(y_new_point)
        z_points.append(z_new_point)

        if len(x_points) > 1 and len(x_points) == len(y_points):
            x_curve_points, y_curve_points, z_curve_points = calculate_3d_spline_interpolation(x_points, y_points, z_points, num=500)
            # ax.plot(x_curve_points, y_curve_points, z_curve_points)
        # ax.scatter(x_points, y_points, z_points)
            curve.set_xdata(x_curve_points)
            curve.set_ydata(y_curve_points)
            curve.set_3d_properties(zs=z_curve_points)

        points.set_xdata(x_points)
        points.set_ydata(y_points)
        points.set_3d_properties(zs=z_points)

        fig.canvas.draw()

    fig.canvas.mpl_connect('button_press_event', on_click)
    plt.show()
