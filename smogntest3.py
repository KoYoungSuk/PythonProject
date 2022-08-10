import smogn
import pandas
import seaborn
import matplotlib.pyplot as plt

product = pandas.read_csv('housing.csv')

product_smogn = smogn.smoter(
    data = product,
    y = "SalePrice"
)

print("PRODUCT_SHAPE: ", product.shape)

print("PRODUCT_SMOGN.SHAPE: " ,product_smogn.shape)


print(smogn.box_plot_stats(product['SalePrice'])['stats'])

print(smogn.box_plot_stats(product_smogn['SalePrice'])['stats'])

seaborn.kdeplot(product['SalePrice'], label="ORIGINAL")
seaborn.kdeplot(product_smogn['SalePrice'], label="MODIFIED")
plt.show()