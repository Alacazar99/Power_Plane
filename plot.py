# @Time    : 2019/6/15 17:23
# @Author  : Zurich.Alcazar
# @Email   : 1178824808@qq.com
# @File    : plot.py
# @Software: PyCharm
import math
import numpy as np
import matplotlib.pyplot as pl
a = 1

t = np.linspace(0, 2*np.pi, 1024)
x = a*(2*np.cos(t) - np.cos(2*t))
y = a*(2*np.sin(t) - np.sin(2*t))
pl.plot(y, x, color = "r")
pl.show()
