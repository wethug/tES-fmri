#负载特性曲线
import matplotlib
import matplotlib.pyplot as plt

# 负载/KΩ
x_list = ['1', '3', '4.3', '5.1', '6.2', '7.5', '8.2', '9.1', '10', '15', '18', '20', '24']
# 电流/mA
y1 = [0.124,	0.108,	0.104,	0.100,	0.101,	0.100,	0.100,	0.099,	0.098,	0.094,	0.093,	0.092,	0.090]
y2 = [0.226,    0.207,	0.203,	0.200,	0.199,	0.197,	0.196,	0.195,	0.193,	0.188,	0.186,	0.183,	0.178]
y3 = [0.512,	0.505,	0.497,	0.492,	0.492,	0.489,	0.487,	0.484,	0.480,	0.465,	0.458,	0.453,	0.450]
y4 = [0.837,    0.800,	0.797,	0.790,	0.781,	0.777,	0.774,	0.768,	0.764,	0.752,	0.739,	0.730,	0.711]
y5 = [1.037,    1.006,	0.991,	0.981,	0.974,	0.967,	0.964,	0.960,	0.952,	0.932,	0.918,	0.908,	0.882]
y6 = [1.236,    1.204,	1.192,	1.176,	1.167,	1.159,	1.154,	1.170,	1.161,	1.115,	1.096,	1.084,	1.059]
y7 = [1.530,    1.496,	1.481,	1.465,	1.455,	1.473,	1.463,	1.451,	1.439,	1.387,	1.305,	1.353,	1.315]
y8 = [1.831,	1.797,	1.773,	1.756,	1.773,	1.755,	1.746,	1.735,	1.719,	1.703,	1.628,	1.613,	1.566]
y9 = [2.029,    1.993,	1.965,	1.986,	1.963,	1.945,	1.935,	1.922,	1.906,	1.891,	1.806,	1.788,	1.735]
y10 = [2.527,	2.482,	2.502,	2.469,	2.439,	2.420,	2.409,	2.390,	2.372,	2.291,	2.246,	2.220,	2.080]
y11 = [3.051,	2.974,	2.984,	2.947,	2.921,	2.895,	2.883,	2.863,	2.836,	2.739,	2.692,	2.479,	2.078]
y12 = [3.556,	3.543,	3.463,	3.431,	3.395,	3.377,	3.357,	3.329,	3.310,	3.213,	2.747,	2.495,	2.076]
y13 = [4.054,	4.027,	3.951,	3.910,	3.874,	3.844,	3.827,	3.799,	3.378,	3.290,	2.773,	2.498,	2.040]

# 定义中文格式
font = {'family': 'MicroSoft Yahei', 'size': 10}
matplotlib.rc('font', **font)

l1, = plt.plot(range(len(y1)), y1, marker='o', markersize=1, color='blue', linewidth=1.2)
l2, = plt.plot(range(len(y2)), y2, marker='o', markersize=1, color='orange', linewidth=1.2)
l3, = plt.plot(range(len(y3)), y3, marker='o', markersize=1, color='grey', linewidth=1.2)
l4, = plt.plot(range(len(y4)), y4, marker='o', markersize=1, color='yellow', linewidth=1.2)
l5, = plt.plot(range(len(y5)), y5, marker='o', markersize=1, color='cornflowerblue', linewidth=1.2)
l6, = plt.plot(range(len(y6)), y6, marker='o', markersize=1, color='red', linewidth=1.2)
l7, = plt.plot(range(len(y7)), y7, marker='o', markersize=1, color='green', linewidth=1.2)
l8, = plt.plot(range(len(y8)), y8, marker='o', markersize=1, color='black', linewidth=1.2)
l9, = plt.plot(range(len(y9)), y9, marker='o', markersize=1, color='pink', linewidth=1.2)
l10, = plt.plot(range(len(y10)), y10, marker='o', markersize=1, color='gold', linewidth=1.2)
l11, = plt.plot(range(len(y10)), y11, marker='o', markersize=1, color='wheat', linewidth=1.2)
l12, = plt.plot(range(len(y10)), y12, marker='o', markersize=1, color='bisque', linewidth=1.2)
l13, = plt.plot(range(len(y10)), y13, marker='o', markersize=1, color='maroon', linewidth=1.2)

plt.xticks(range(len(x_list)), x_list)
plt.xlabel("负载/KΩ")

plt.ylabel("电流/mA")
plt.ylim(0, 6.0)

plt.title('电流源负载特性')
plt.legend(handles=[l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13], labels=['0.1mA', '0.2mA', '0.5mA', '0.8mA', '1.0mA', '1.2mA', '1.5mA', '1.8mA', '2.0mA', '2.5mA', '3.0mA', '3.5mA', '4.0mA'], ncol=2,  prop=font)

plt.show()