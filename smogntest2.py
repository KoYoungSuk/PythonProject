import smogn
import pandas
import seaborn
import matplotlib.pyplot as plt

product = pandas.read_csv('productexample.csv')

product_smogn = smogn.smoter(
    data = product,
    y = "BUY_DATE"
)

print("PRODUCT_SHAPE: ", product.shape)

print("PRODUCT_SMOGN.SHAPE: " ,product_smogn.shape)


print(smogn.box_plot_stats(product['BUY_DATE'])['stats'])

print(smogn.box_plot_stats(product_smogn['BUY_DATE'])['stats'])

seaborn.kdeplot(product['BUY_DATE'], label="ORIGINAL")
seaborn.kdeplot(product_smogn['BUY_DATE'], label="MODIFIED")
plt.show()