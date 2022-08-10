import smogn
import pandas

housing = pandas.read_csv("https://raw.githubusercontent.com/nickkunz/smogn/master/data/housing.csv")

housing_smogn = smogn.smoter(data = housing, y = "SalePrice")

print(housing_smogn)