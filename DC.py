# 直流误差
import matplotlib
import matplotlib.pyplot as plt

# 负载/KΩ
x_list = ['3', '4.3', '5.1', '6.2', '7.5', '8.2', '9.1', '10', '15', '18']
# 误差/%
y1 = [2.82, 1.79, 0.20, 0.29, 0.50, 0.49, 1.21, 1.10, 1.50, 1.62]
y2 = [2.67, 1.28, 0.40, 0.73, 1.27, 1.41, 1.64, 1.71, 2.10, 2.22]
y3 = [0.93, 0.65, 1.01, 1.58, 1.59, 1.66, 1.83, 1.81, 2.08, 2.40]
y4 = [0.04, 0.32, 1.25, 1.42, 1.65, 1.80, 1.96, 2.04, 2.46, 2.57]
y5 = [0.63, 0.93, 1.24, 1.66, 2.37, 2.46, 2.54, 2.33, 2.65, 2.92]
y6 = [0.36, 0.64, 1.36, 1.58, 2.41, 2.52, 2.47, 2.63, 2.95, 3.40]
y7 = [0.27, 1.29, 1.45, 1.73, 2.48, 2.44, 2.60, 2.76, 3.37, 4.16]
y8 = [0.19, 1.51, 1.52, 1.82, 2.52, 2.78, 2.69, 3.02, 3.56, 4.54]
y9 = [0.35, 1.76, 1.69, 1.85, 2.53, 3.03, 3.10, 4.02, 4.30, 4.82]

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

plt.title('电流源不同电流直流误差')
legend_font = {'family': 'MicroSoft Yahei', 'size': 16}
plt.legend(handles=[l1, l2, l3, l4, l5, l6, l7, l8, l9],
           labels=['0.1mA', '0.2mA', '0.5mA', '0.8mA', '1.0mA', '1.2mA', '1.5mA', '1.8mA', '2.0mA'], prop=legend_font)

# 添加水平直线
plt.axhline(y=3, ls="--", c="black", linewidth=1.10)
plt.axhline(y=5, ls="--", c="red", linewidth=1.10)

plt.show()
