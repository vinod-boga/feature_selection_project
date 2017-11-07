# Default imports
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your solution here:
def plot_corr(data,size=11):
    plt.figure(figsize=(15,12))
    cmap = sns.diverging_palette(220, 20, as_cmap=True)
    sns.heatmap(data.corr(),cmap=cmap)
    plt.show()
plot_corr(data)
