#直流误差
import matplotlib
import matplotlib.pyplot as plt

# 负载/KΩ
x_list = ['3', '4.3', '5.1', '6.2', '7.5', '8.2', '9.1', '10', '15', '18']
# 误差/%
y1 = [4.67, 3.19, 0.20, 1.29, 0.50, 0.49, 1.21, 2.40, 2.40, 7.00]
y2 = [3.67, 1.28, 0.20, 0.73, 1.67, 2.01, 2.64, 3.50, 3.50, 7.22]
y3 = [0.93, 0.65, 1.61, 1.58, 2.29, 2.66, 3.23, 4.08, 4.08, 8.50]
y4 = [0.04, 0.32, 1.25, 2.32, 2.85, 3.20, 3.96, 4.46, 4.46, 7.57]
y5 = [0.63, 0.93, 1.94, 2.56, 3.25, 3.56, 4.04,	4.85, 4.85, 8.22]
y6 = [0.36, 0.64, 1.96, 2.78, 3.41, 3.82, 2.47, 3.25, 3.25, 8.70]
y7 = [0.27, 1.29, 2.30, 3.03, 1.78, 2.44, 3.30, 4.07, 4.07, 9.00]
y8 = [0.19, 1.51, 2.42, 1.52, 2.52, 2.98, 3.60, 4.50, 4.50, 9.54]
y9 = [0.35, 1.76, 0.69, 1.85, 2.73, 3.23, 3.90, 4.70, 4.70,	9.72]
y10 = [0.73, 0.09, 1.25, 2.45, 3.20, 3.66, 4.40, 5.12, 5.12, 10.18]

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

plt.title('电流源不同电流直流误差')
plt.legend(handles=[l1, l2, l3, l4, l5, l6, l7, l8, l9, l10], labels=['0.1mA', '0.2mA', '0.5mA', '0.8mA', '1.0mA', '1.2mA', '1.5mA', '1.8mA', '2.0mA', '2.5mA'], prop=font)

plt.axhline(y=5, ls=":", c="red")#添加水平直线

plt.show()