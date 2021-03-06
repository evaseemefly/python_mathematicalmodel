#!/usr/bin/python
#  -*- coding:utf-8 -*-

import numpy as np
import math
import matplotlib as mpl
import matplotlib.pyplot as plt

# 最小二乘法
from scipy.optimize import leastsq


def residual(theta, x1, y1):
    mu1 = theta[0]
    sigma1 = theta[1]
    y_hat = np.exp(-(x1-mu1)**2 / (2*sigma1**2)) / (math.sqrt(2*math.pi)*sigma1)
    return y1 - y_hat


if __name__ == "__main__":
    # 均值为2，标准差为3
    data = np.random.randn(1000) * 3 + 2
    y, x = np.histogram(data, bins=20, density=True)
    x = (x[1:] + x[:-1]) / 2
    print(x)
    print(y)

    mu = 0
    sigma = 1
    t = leastsq(residual, (mu, sigma), args=(x, y))[0]
    mu, sigma = t
    print('期望和标准差的估计值：', mu, sigma)

    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    plt.figure(facecolor='w')
    plt.plot(x, y, 'go--', lw=2)
    y_hat = np.exp(-(x-mu)**2 / (2*sigma**2)) / (math.sqrt(2*math.pi)*sigma)
    plt.plot(x, y_hat, 'ro-', lw=2)
    plt.hist(data, bins=20, normed=True, color='g', alpha=0.6)
    plt.grid(b=True, ls=':')
    plt.title('正态分布采样与参数估计', fontsize=20)
    plt.xlabel('X', fontsize=16)
    plt.ylabel('Y', fontsize=16)
    plt.show()

