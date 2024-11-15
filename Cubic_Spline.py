import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# 样本数据点
x = np.array([])
y = np.array([])

# 使用CubicSpline进行三次样条插值
cs = CubicSpline(x, y)

# 生成插值点
x_interp = np.linspace(x.min(), x.max(), 100)
y_interp = cs(x_interp)

# 绘制原始数据点和插值结果
plt.scatter(x, y, color='red')
plt.plot(x_interp, y_interp)
plt.legend()
plt.xlabel('x')
plt.ylabel('t')
plt.title('x-t function image')
plt.show()
