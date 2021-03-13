# 交流10Hz误差
import matplotlib
import matplotlib.pyplot as plt

# 负载/KΩ
x_list = ['3', '4.3', '5.1', '6.2', '7.5', '8.2', '9.1', '10', '15', '18']
# 误差/%
y1 = [2.33, 1.42, 0.38, 0.36, 0.42, 0.98, 1.01, 1.66, 1.68, 1.77]
y2 = [2.04, 1.29, 0.50, 0.51, 0.59, 0.69, 1.13, 1.33, 1.96, 2.13]
y3 = [1.26, 0.87, 1.19, 1.28, 1.36, 1.47, 1.56, 1.83, 2.06, 2.11]
y4 = [0.40, 1.33, 1.20, 1.35, 1.69, 1.79, 1.85, 1.99, 2.16, 2.56]
y5 = [0.19, 1.58, 1.54, 1.59, 1.76, 1.97, 2.34, 2.07, 2.57, 2.98]
y6 = [0.49, 1.71, 1.77, 1.71, 2.26, 2.06, 2.44, 2.76, 2.95, 3.29]
y7 = [1.06, 1.63, 2.18, 2.27, 2.37, 2.57, 2.57, 2.77, 3.13, 4.11]
y8 = [1.29, 1.86, 2.29, 2.48, 2.56, 2.78, 2.88, 3.36, 3.81, 4.31]
y9 = [1.09, 1.76, 2.29, 2.52, 2.77, 2.99, 3.58, 4.02, 4.30, 4.82]

# 定义中文格式
font = {'family': 'MicroSoft Yahei', 'size': 24}
matplotlib.rc('font', **font)

plt.figure(figsize=(14.4, 10.8))

l1, = plt.plot(range(len(y1)), y1, marker='o', markersize=1, color='blue', linewidth=1.10)
l2, = plt.plot(range(len(y2)), y2, marker='o', markersize=1, color='orange', linewidth=1.10)
l3, = plt.plot(range(len(y3)), y3, marker='o', markersize=1, color='grey', linewidth=1.10)
l4, = plt.plot(range(len(y4)), y4, marker='o', markersize=1, color='yellow', linewidth=1.10)
l5, = plt.plot(range(len(y5)), y5, marker='o', markersize=1, color='cornflowerblue', linewidth=1.10)
l6, = plt.plot(range(len(y6)), y6, marker='o', markersize=1, color='red', linewidth=1.10)
l7, = plt.plot(range(len(y7)), y7, marker='o', markersize=1, color='green', linewidth=1.10)
l8, = plt.plot(range(len(y8)), y8, marker='o', markersize=1, color='black', linewidth=1.10)
l9, = plt.plot(range(len(y9)), y9, marker='o', markersize=1, color='pink', linewidth=1.10)

label_font = {'family': 'MicroSoft Yahei', 'size': 26}
plt.xticks(range(len(x_list)), x_list)
plt.xlabel("负载/KΩ", font=label_font)

plt.ylabel("误差/%", font=label_font)
plt.ylim(0, 6)

plt.title('电流源不同电流10Hz交流误差')
legend_font = {'family': 'MicroSoft Yahei', 'size': 16}
plt.legend(handles=[l1, l2, l3, l4, l5, l6, l7, l8, l9],
           labels=['0.12mA', '0.2mA', '0.6mA', '0.8mA', '1.0mA', '1.2mA', '1.6mA', '1.8mA', '2.0mA'], prop=legend_font)

plt.axhline(y=5, ls=":", c="red")  # 添加水平直线

plt.show()
