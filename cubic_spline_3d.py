from cubic_spline import *

class CubicSpline3D:
    def __init__(self, x, y, z):
        self.params = self.__calculate_params(x, y, z)
        self.sx = CubicSpline(self.params, x)
        self.sy = CubicSpline(self.params, y)
        self.sz = CubicSpline(self.params, z)

    def point(self, param):
        x = self.sx.point(param)
        y = self.sy.point(param)
        z = self.sz.point(param)
        return x, y, z

    def __calculate_params(self, x: list, y: list, z: list) -> list:
        dx = np.diff(x)
        dy = np.diff(y)
        dz = np.diff(z)
        
        self.ds = [np.sqrt(idx ** 2 + idy ** 2 + idz ** 2) for (idx, idy, idz) in zip(dx, dy, dz)]
        s = [0.0] 
        s.extend(np.cumsum(self.ds))
        return s
