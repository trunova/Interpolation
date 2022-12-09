from point import point
import numpy as np

class polynomial_Newton:

    def __init__(self, x: list, y: list):
        self._list_points_x = x
        self._list_points_y = y
        self._len = len(x)

    def point(self, param):
        if param < self._list_points_x[0] or param > self._list_points_x[-1]:
            return None
        result = self.calculate_polynomial_Newton(param)
        return result

    def calculate_polynomial_Newton(self, x):
        result = self._list_points_y[0]
        for i in range(1, self._len):
            tmp = self.divided_difference(self._list_points_x[0:i+1])
            for j in range(0, i):
                tmp *= (x - self._list_points_x[j])
            result += tmp
        return result


    def divided_difference(self, list_x: list):
        result = 0
        for j in range(len(list_x)):
            tmp = 1
            for i in range(len(list_x)):
                if i != j:
                    tmp *= (list_x[j] - list_x[i])
            result += self._list_points_y[j] / tmp
        return result


    # def calculate_interpolation(self, n=100):
    #     result_x, result_y = [], []
    #     params = np.linspace(self._list_points_x[0], self._list_points_x[-1], n)
    #     for param in params:
    #         result_x.append(param)
    #         result_y.append(self.calculate_polynomial_Newton(param))
    #
    #     return result_x, result_y

    @property
    def list_points_x(self) -> list:
        return self._list_points_x

    @list_points_x.setter
    def list_points_x(self, list_points_x: list):
        self._list_points_x = list_points_x

    @property
    def list_points_y(self) -> list:
        return self._list_points_y

    @list_points_y.setter
    def list_points_y(self, list_points_y: list):
        self._list_points_y = list_points_y

    @property
    def len(self) -> int:
        return self._len

    @len.setter
    def len(self, len: int):
        self._len = len