import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def logistic_map(r, x0, generations):
    x = [x0]
    for _ in range(1, generations):
        x.append(r * x[-1] * (1 - x[-1]))
    return x

def plot_bifurcation_diagram(ax, r_values, x0=0.5, generations=200, zoom=None):
    for r in r_values:
        x = logistic_map(r, x0, generations)
        if zoom:
            ax.plot([r] * (generations - zoom), x[zoom:], '.', markersize=1)
        else:
            ax.plot([r] * generations, x, '.', markersize=1)

# Plotting the logistic map for different parameter values
columns = [k * 0.5 for k in range(1, 8)]
rows = [n for n in range(20)]
data = {'': rows}

for column in columns:
    data[column] = logistic_map(column, 0.5, 20)

df = pd.DataFrame(data)

plt.figure(figsize=(10, 6))

# Plotting the logistic map columns
for i, column in enumerate(columns, 1):
    plt.plot(df[''], df[column], f'C{i}', label=str(column))

plt.legend()
plt.xlabel('Generation')
plt.ylabel('Population')
plt.title('Logistic Map for Different Growth Rates')
plt.show()

# Plotting bifurcation diagrams for specific ranges and zoom levels
r_values_1 = np.arange(2.8, 4.0, 0.004)
r_values_2 = np.arange(3.7, 3.9, 0.004)
r_values_3 = np.arange(3.84, 3.856, 0.004)

fig, axes = plt.subplots(3, 1, figsize=(10, 18))

for ax, r_values, zoom in zip(axes, [r_values_1, r_values_2, r_values_3], [None, (100, 200), (100, 200)]):
    plot_bifurcation_diagram(ax, r_values, zoom=zoom)

plt.tight_layout()
plt.show()
