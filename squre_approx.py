import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 样本数据
x = np.array([])
y = np.array([])

# 定义二次拟合函数
def quadratic_fit(x, a, b, c):
    return a * x**2 + b * x + c

# 拟合数据
params, covariance = curve_fit(quadratic_fit, x, y)
a, b, c = params

# 计算预测值
y_pred = quadratic_fit(x, a, b, c)

# 计算R^2
ss_res = np.sum((y - y_pred) ** 2)  # 残差平方和
ss_tot = np.sum((y - np.mean(y)) ** 2)  # 总体平方和
r_squared = 1 - (ss_res / ss_tot)

# 绘制散点图和拟合曲线
plt.scatter(x, y, label='Data Points', color='blue')
plt.plot(x, y_pred, label=f'Fit: y = {a:.2f}x^2 + {b:.2f}x + {c:.2f}\n$R^2$ = {r_squared:.4f}', color='red')

# 添加网格
plt.grid(True)

# 添加图例和标题
plt.legend()
plt.xlabel('t/T')
plt.ylabel('y/cm')
#plt.title('Quadratic Fit of Data')
plt.show()
