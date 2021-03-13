# 交流5Hz误差
import matplotlib
import matplotlib.pyplot as plt

# 负载/KΩ
x_list = ['3', '4.3', '5.1', '6.2', '7.5', '8.2', '9.1', '10', '15', '18']
# 误差/%
y1 = [2.37, 1.21, 0.39, 0.35, 0.42, 0.98, 1.01, 1.66, 1.78, 1.89]
y2 = [2.14, 1.17, 0.30, 0.46, 0.57, 0.69, 1.13, 1.33, 1.87, 2.00]
y3 = [1.03, 0.91, 1.19, 1.28, 1.56, 1.47, 1.56, 1.87, 2.06, 2.08]
y4 = [0.33, 1.33, 1.20, 1.35, 1.78, 1.79, 1.85, 1.99, 2.16, 2.42]
y5 = [0.21, 1.67, 1.54, 1.59, 1.94, 1.97, 2.01, 2.07, 2.57, 2.91]
y6 = [0.47, 1.63, 1.87, 1.71, 2.11, 2.06, 2.54, 2.86, 2.95, 3.44]
y7 = [0.76, 1.73, 2.20, 2.27, 2.48, 2.57, 2.60, 2.77, 3.09, 4.06]
y8 = [0.89, 1.86, 2.31, 2.45, 2.58, 2.80, 2.88, 3.36, 3.71, 4.29]
y9 = [1.12, 1.84, 2.30, 2.49, 2.67, 2.98, 3.52, 3.99, 4.20, 4.70]

# 定义中文格式
font = {'family': 'MicroSoft Yahei', 'size': 24}
matplotlib.rc('font', **font)

plt.figure(figsize=(14.4, 10.8))

l1, = plt.plot(range(len(y1)), y1, marker='o', markersize=1, color='blue', linewidth=0.80)
l2, = plt.plot(range(len(y2)), y2, marker='o', markersize=1, color='orange', linewidth=0.80)
l3, = plt.plot(range(len(y3)), y3, marker='o', markersize=1, color='grey', linewidth=0.80)
l4, = plt.plot(range(len(y4)), y4, marker='o', markersize=1, color='yellow', linewidth=0.80)
l5, = plt.plot(range(len(y5)), y5, marker='o', markersize=1, color='cornflowerblue', linewidth=0.80)
l6, = plt.plot(range(len(y6)), y6, marker='o', markersize=1, color='red', linewidth=0.80)
l7, = plt.plot(range(len(y7)), y7, marker='o', markersize=1, color='green', linewidth=0.80)
l8, = plt.plot(range(len(y8)), y8, marker='o', markersize=1, color='black', linewidth=0.80)
l9, = plt.plot(range(len(y9)), y9, marker='o', markersize=1, color='pink', linewidth=0.80)

label_font = {'family': 'MicroSoft Yahei', 'size': 26}
plt.xticks(range(len(x_list)), x_list)
plt.xlabel("负载/KΩ", font=label_font)

plt.ylabel("误差/%", font=label_font)
plt.ylim(0, 6)

plt.title('电流源不同电流5Hz交流误差')
legend_font = {'family': 'MicroSoft Yahei', 'size': 16}
plt.legend(handles=[l1, l2, l3, l4, l5, l6, l7, l8, l9],
           labels=['0.12mA', '0.2mA', '0.6mA', '0.8mA', '1.0mA', '1.2mA', '1.6mA', '1.8mA', '2.0mA'], prop=legend_font)

plt.axhline(y=5, ls="--", c="red")  # 添加水平直线

plt.show()
