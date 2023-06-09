import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('Pearson.csv')
import numpy as np

x = data['Father']
y = data['Son']
x1 = data[(data['Father'] >= 63.5) & (data['Father'] <= 64.4)]['Son']  # 64
x2 = data[(data['Father'] >= 68.5) & (data['Father'] <= 69.4)]['Son']  # 69
x3 = data[(data['Father'] >= 69.5) & (data['Father'] <= 70.4)]['Son']  # 70
y1 = data[(data['Son'] >= 65.5) & (data['Son'] <= 66.4)]['Father']  # 66
y2 = data[(data['Son'] >= 64.5) & (data['Son'] <= 65.4)]['Father']  # 65
y3 = data[(data['Son'] >= 67.5) & (data['Son'] <= 68.4)]['Father']  # 68
grid = plt.GridSpec(6, 6, wspace=0.4, hspace=0.7)
main_axe = plt.subplot(grid[0:3, 0:3])
main_axe.scatter(x, y, color='midnightblue')
x_prim = plt.subplot(grid[3, 0:3])
x_prim.hist(x1, color='springgreen')
x_prim.set_xticks([])
x_prim.invert_yaxis()
x_sec = plt.subplot(grid[4, 0:3])
x_sec.hist(x2, color='lightseagreen')
x_sec.set_xticks([])
x_sec.invert_yaxis()
x_ter = plt.subplot(grid[5, 0:3])
x_ter.hist(x3, color='dodgerblue')
x_ter.set_xticks([])
x_ter.invert_yaxis()
y_prim = plt.subplot(grid[0:3, 3])
y_prim.hist(y1, color='purple')
y_prim.set_yticks([])
y_sec = plt.subplot(grid[0:3, 4])
y_sec.hist(y2, color='deeppink')
y_sec.set_yticks([])
y_ter = plt.subplot(grid[0:3, 5])
y_ter.hist(y3, color='crimson')
y_ter.set_yticks([])
plt.gcf().suptitle("Fathers and sons", fontfamily='Century Gothic', fontsize=30, weight='bold')
plt.show()
