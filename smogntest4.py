import smogn
import pandas
import seaborn
import matplotlib.pyplot as plt


product = pandas.read_csv('housing.csv')

product_smogn = smogn.smoter(
    data = product,
    y = "YearBuilt"
)

print("PRODUCT_SHAPE: ", product.shape)

print("PRODUCT_SMOGN.SHAPE: " ,product_smogn.shape)


print(smogn.box_plot_stats(product['YearBuilt'])['stats'])

print(smogn.box_plot_stats(product_smogn['YearBuilt'])['stats'])

seaborn.kdeplot(product['YearBuilt'], label="ORIGINAL")
seaborn.kdeplot(product_smogn['YearBuilt'], label="MODIFIED")
plt.show()