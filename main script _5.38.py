# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# %%
%pip install pyarrow

# %%
products=pd.read_pickle("cleaned data/products_001.pkl")
orders=pd.read_pickle("cleaned data/orders_001.pkl")
customers=pd.read_pickle("cleaned data/customers_001.pkl")


# %%
customers.head(5)

# %%
customers.info()


# %%
products.head(5)
orders.head(5)


# %%
# This prevents the 'ValueError: columns overlap' we saw earlier
cols_to_fix = ['customer_name', 'email', 'country']
orders = orders.drop(columns=cols_to_fix, errors='ignore')

# 3. Perform the Left Merge
# This matches every order to its customer details in one shot
orders = pd.merge(orders, customers[['customer_id', 'customer_name', 'email', 'country']], 
                  on='customer_id', 
                  how='left')

# %%
orders.head(5)

# %%
products.head(5)

# %%
# 3. Perform the Left Merge
# This matches every order to its product details in one shot
orders = pd.merge(orders, products[['product_id', 'coffee_type', 'roast_type', 'size', 'unit_price','profit']], 
                  on='product_id', 
                  how='left')

# %%
orders.head(5)

# %%
# Delete columns ending with "_y" and rename columns ending with "_x" (remove "_x")
orders = orders.loc[:, ~orders.columns.str.endswith('_y')]
orders.columns = orders.columns.str.replace('_x', '', regex=False)

# %%
# Merge loyalty from customers with orders
orders = pd.merge(orders, customers[['customer_id', 'loyalty_card']], 
                  on='customer_id', 
                  how='left')

# %%
# Clean up duplicate loyalty columns
orders = orders.drop(columns=['loyalty_card_y'], errors='ignore')
orders = orders.rename(columns={'loyalty_card_x': 'loyalty_card'})

# %%
# Merge city from customers with orders
orders = pd.merge(orders, customers[['customer_id', 'city']], 
                  on='customer_id', 
                  how='left')

# %%
# Sort columns with logical order: Order Info → Customer Info → Product Info → Transaction Details
column_order = [
    'order_id', 'order_date',                    # Order identifiers
    'customer_id', 'customer_name', 'email', 'city', 'country', 'loyalty_card',  # Customer info
    'product_id', 'coffee_type', 'roast_type', 'size',  # Product info
    'quantity', 'unit_price', 'sales', 'profit_per_item', 'net_profit'  # Transaction details
]
orders = orders[column_order]

# %%
orders.info()

# %%
orders.rename(columns={'profit': 'profit_per_item'}, inplace=True)

# %%
orders['sales'] = orders['quantity'] * orders['unit_price']
orders['net_profit'] = orders['quantity'] * orders['profit_per_item']

# %%
orders.info()

# %%




