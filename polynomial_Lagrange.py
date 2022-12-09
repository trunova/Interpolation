from point import point
import numpy as np

class polynomial_Lagrange:

     def __init__(self, x: list, y: list):
          self._list_points_x = x
          self._list_points_y = y
          self._len = len(x)

     def point(self, param):
          if param < self._list_points_x[0] or param > self._list_points_x[-1]:
               return None
          result = self.calculate_polynomial_Lagrange(param)
          return result

     def polynomial_i(self, i: int, x: float) -> float:
          result = 1
          for j in range(self._len):
               if j != i:
                    result *= (x - self._list_points_x[j]) / (self._list_points_x[i] - self._list_points_x[j])
          return result

     def calculate_polynomial_Lagrange(self, x: float):
          result = 0
          for i in range(self._len):
               result += self._list_points_y[i] * self.polynomial_i(i, x)
          return result

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