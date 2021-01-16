#交流10Hz误差
import matplotlib
import matplotlib.pyplot as plt

# 负载/KΩ
x_list = ['3', '4.3', '5.1', '6.2', '7.5', '8.2', '9.1', '10', '15', '18']
# 误差/%
y1 = [4.78,	1.16,	2.08,	2.15,	1.82,	2.00,	3.82,	3.50,	4.67,	5.45]
y2 = [4.67,	2.44,	0.39,	0.89,	1.73,	2.47,	3.01,	4.05,	5.00,	5.89]
y3 = [0.94,	0.85,	1.69,	2.80,	3.49,	3.89,	4.02,	4.85,	5.20,	5.97]
y4 = [0.29,	1.31,	2.07,	3.05,	3.52,	4.07,	4.36,	4.73,	5.50,	6.07]
y5 = [0.20,	1.65,	2.44,	3.23,	3.71,	4.23,	4.43,	4.67,	5.13,	6.28]
y6 = [0.44,	1.80,	2.57,	3.24,	3.88,	4.28,	4.63,	4.77,	5.44,	7.23]
y7 = [0.69,	2.11,	2.69,	3.46,	4.10,	4.17,	4.59,	4.79,	5.38,	8.10]
y8 = [0.87,	2.21,	2.79,	3.63,	4.07,	4.01,	4.63,	4.78,	5.52,	8.37]
y9 = [0.97,	2.34,	2.88,	3.79,	4.03,	4.08,	4.74,	4.90,	5.70,	9.44]
y10 = [1.35, 2.77,	3.20,	4.00,	4.27,	4.47,	4.91,	5.63,	6.08,	10.71]
# 定义中文格式
font = {'family': 'MicroSoft Yahei', 'size': 9}
matplotlib.rc('font', **font)

l1, = plt.plot(range(len(y1)), y1, marker='o', markersize=1, color='blue', linewidth=1.10)
l2, = plt.plot(range(len(y2)), y2, marker='o', markersize=1, color='orange', linewidth=1.10)
l3, = plt.plot(range(len(y3)), y3, marker='o', markersize=1, color='grey', linewidth=1.10)
l4, = plt.plot(range(len(y4)), y4, marker='o', markersize=1, color='yellow', linewidth=1.10)
l5, = plt.plot(range(len(y5)), y5, marker='o', markersize=1, color='cornflowerblue', linewidth=1.10)
l6, = plt.plot(range(len(y6)), y6, marker='o', markersize=1, color='red', linewidth=1.10)
l7, = plt.plot(range(len(y7)), y7, marker='o', markersize=1, color='green', linewidth=1.10)
l8, = plt.plot(range(len(y8)), y8, marker='o', markersize=1, color='black', linewidth=1.10)
l9, = plt.plot(range(len(y9)), y9, marker='o', markersize=1, color='pink', linewidth=1.10)
l10, = plt.plot(range(len(y10)), y10, marker='o', markersize=1, color='purple', linewidth=1.10)

plt.xticks(range(len(x_list)), x_list)
plt.xlabel("负载/KΩ")

plt.ylabel("误差/%")
plt.ylim(0, 12)

plt.title('电流源不同电流10Hz交流误差')
plt.legend(handles=[l1, l2, l3, l4, l5, l6, l7, l8, l9, l10], labels=['0.12mA', '0.2mA', '0.6mA', '0.8mA', '1.0mA', '1.2mA', '1.6mA', '1.8mA', '2.0mA', '2.6mA'], prop=font)

plt.axhline(y=5, ls=":", c="red")#添加水平直线

plt.show()