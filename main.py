import pandas as pd 
from matplotlib import pyplot as plt
import numpy as np
import scipy.stats as stats
import seaborn as sns

data = pd.read_csv("data/Plant.csv", sep = ",")

# ################################################
# Histogram
groups = data.groupby("Species")

for name, group in groups:
    # Leaf Length 
    plt.figure(figsize=(10, 6))
    plt.subplot(1, 2, 1)
    sns.histplot(group['LeafLengthCm'], kde=True, bins=10, color='skyblue')
    plt.title(f"Histogram of Leaf Length - {name}")
    plt.xlabel("Leaf Length (cm)")
    plt.ylabel("Frequency")
    # Leaf Width
    plt.subplot(1, 2, 2)
    sns.histplot(group['LeafWidthCm'], kde=True, bins=10, color='salmon')
    plt.title(f"Histogram of Leaf Width - {name}")
    plt.xlabel("Leaf Width (cm)")
    plt.ylabel("Frequency")
    
    plt.tight_layout()
    plt.show()

# ################################################
# Boxplot
plt.figure(figsize=(12, 6))
# Leaf Length
sns.boxplot(data=data, y='LeafLengthCm', color='lightblue')
plt.text(0, data['LeafWidthCm'].min()+2.5, 'All', horizontalalignment='center', fontsize=12)
sns.boxplot(data=data, x='Species', y='LeafLengthCm', color='lightcoral')
plt.title("Boxplot - Leaf Length (cm)")
plt.ylabel("Leaf Length (cm)")
plt.xlabel("Species")
# Leaf Width
sns.boxplot(data=data, y='LeafWidthCm', color='lightblue')
plt.text(0, data['LeafWidthCm'].min() - 0.17, 'All', horizontalalignment='center', fontsize=12)
sns.boxplot(data=data, x='Species', y='LeafWidthCm', color='lightcoral')
plt.title("Boxplot - Leaf Width (cm)")
plt.ylabel("Leaf Width (cm)")
plt.xlabel("Species")

plt.tight_layout()
plt.show()

# ################################################
# Scatter Plot
x = data["LeafLengthCm"]
y = data["LeafWidthCm"]
sns.scatterplot(data=data, x=x, y=y, hue="Species")
plt.title("Scatter Plot - Leaf Length vs Leaf Width")
plt.xlabel("Leaf Length (cm)")
plt.ylabel("Leaf Width (cm)")

plt.show()

# Calculate PearsonRResult
groups = data.groupby("Species")
for name, group in groups:
    x = group.LeafLengthCm
    y = group.LeafWidthCm
    print(name)
    pearson = stats.pearsonr(x,y)
    print(pearson)
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
    print(slope, intercept, r_value, p_value, std_err)
    plt.plot(x,intercept + slope*x, 'r')
    plt.show()
# Output:
# Dumb-cane
# PearsonRResult(statistic=np.float64(0.13511635000956917), pvalue=np.float64(0.5700580883451103))
# slope = 0.08359522313010684, intercept = 4.604651162790698, r_value = 0.1351163500095691
# p_value = 0.5700580883451105, std_err = 0.14448951627367315
# Snake-plant
# PearsonRResult(statistic=np.float64(0.09300726537145249), pvalue=np.float64(0.6965320110390785))
# slope = 0.06518904823989581, intercept = 5.152698826597131, r_value = 0.0930072653714525
# p_value = 0.696532011039078, std_err = 0.16448827305809685
# Zz-plant
# PearsonRResult(statistic=np.float64(-0.03334784771056223), pvalue=np.float64(0.8889985821186672))
# slope = -0.02133544053733718, intercept = 6.613512445673647, r_value = -0.03334784771056224
# p_value = 0.8889985821186673, std_err = 0.1507148110198336

# ################################################
# Calculate the mean, median, and variance for each species
result = data.groupby('Species').agg({
    'LeafLengthCm': ['mean', 'median', 'var'],
    'LeafWidthCm': ['mean', 'median', 'var']
})

# Output
#             LeafLengthCm                  LeafWidthCm
#                     mean median       var        mean median       var
# Species
# Dumb-cane          14.06   13.7  0.669895        5.78    5.9  0.256421
# Snake-plant        10.85   11.0  0.403684        5.86    5.8  0.198316
# Zz-plant            9.07    9.1  0.266421        6.42    6.4  0.109053