from base_geometry import BaseGeometry
from rectangle import Rectangle


bg = BaseGeometry()
print(dir(bg))

try:
    r = Rectangle(3, 5)
    print(r)
    print(dir(r))
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
