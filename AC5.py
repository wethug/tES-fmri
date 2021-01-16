#交流5Hz误差
import matplotlib
import matplotlib.pyplot as plt

# 负载/KΩ
x_list = ['3', '4.3', '5.1', '6.2', '7.5', '8.2', '9.1', '10', '15', '18']
# 误差/%
y1 = [4.67,	1.21,	2.99,	2.35,	2.42,	1.98,	4.31,	3.96,	4.98,	6.89]
y2 = [3.34,	2.47,	0.30,	1.26,	2.17,	2.89,	3.43,	4.43,	8.00,	9.68]
y3 = [1.03,	0.91,	2.19,	3.18,	3.86,	4.27,	4.56,	5.37,	8.36,	9.98]
y4 = [0.33,	1.33,	2.59,	3.35,	3.88,	4.49,	4.85,	5.70,	8.46,	10.02]
y5 = [0.21,	1.67,	2.84,	3.69,	4.14,	4.67,	4.91,	5.77,	8.17,	10.21]
y6 = [0.47,	1.83,	3.17,	3.71,	4.31,	4.26,	5.14,	6.27,	8.45,	10.24]
y7 = [0.76,	2.13,	3.20,	3.87,	4.48,	4.67,	5.30,	6.17,	8.40,	10.16]
y8 = [0.89,	2.26,	3.31,	4.05,	4.58,	4.80,	5.38,	6.26,	8.51,	10.29]
y9 = [1.12,	2.44,	3.40,	4.29,	4.67,	4.88,	5.42,	6.29,	8.50,	10.30]
y10 = [1.35,	2.87,	3.72,	4.43,	4.87,	5.06,	5.42,	6.30,	8.99,	10.68]
# 定义中文格式
font = {'family': 'MicroSoft Yahei', 'size': 7}
matplotlib.rc('font', **font)

l1, = plt.plot(range(len(y1)), y1, marker='o', markersize=3, color='blue', linewidth=0.80)
l2, = plt.plot(range(len(y2)), y2, marker='o', markersize=3, color='orange', linewidth=0.80)
l3, = plt.plot(range(len(y3)), y3, marker='o', markersize=3, color='grey', linewidth=0.80)
l4, = plt.plot(range(len(y4)), y4, marker='o', markersize=3, color='yellow', linewidth=0.80)
l5, = plt.plot(range(len(y5)), y5, marker='o', markersize=3, color='cornflowerblue', linewidth=0.80)
l6, = plt.plot(range(len(y6)), y6, marker='o', markersize=3, color='red', linewidth=0.80)
l7, = plt.plot(range(len(y7)), y7, marker='o', markersize=3, color='green', linewidth=0.80)
l8, = plt.plot(range(len(y8)), y8, marker='o', markersize=3, color='black', linewidth=0.80)
l9, = plt.plot(range(len(y9)), y9, marker='o', markersize=3, color='pink', linewidth=0.80)
l10, = plt.plot(range(len(y10)), y10, marker='o', markersize=3, color='purple', linewidth=0.80)

plt.xticks(range(len(x_list)), x_list)
plt.xlabel("负载/KΩ")

plt.ylabel("误差/%")
plt.ylim(0, 12)

plt.title('电流源不同电流5Hz交流误差')
plt.legend(handles=[l1, l2, l3, l4, l5, l6, l7, l8, l9, l10], labels=['0.12mA', '0.2mA', '0.6mA', '0.8mA', '1.0mA', '1.2mA', '1.6mA', '1.8mA', '2.0mA', '2.6mA'], prop=font)

plt.axhline(y=5, ls=":", c="red")#添加水平直线

plt.show()