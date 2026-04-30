class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def apply_discount(self, percent_off):
        discount = (percent_off / 100) * self.price
        self.price -= discount
#2
import pandas as pd
data = {
    'Product_Id': [101,102,103],
    'Category': ['Electronics','Clothing','Electronics'],
    'Price': [1000,500,2000]
}
df_initial = pd.DataFrame(data)
df_initial.to_csv("products.csv")
df = pd.read_csv("products.csv")
select_row = df[df['Category'] == 'Electronic']
#3
new_price = []
for index, row in select_row.iterrows():
    item = Product(row['Product_Id'], row['Price'])
    item.apply_discount(20)
    new_price.append(item.price)
#4
select_row['Price'] = new_price
select_row['Promo_Active'] = 'Yes'
#5
select_row.to_excel("holiday_promo.xlsx", index=False)
print("holiday_promo.xlsx has been created")