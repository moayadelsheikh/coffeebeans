import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def load_data():
    # Load data from pickle files
    products = pd.read_pickle("cleaned data/products_001.pkl")
    orders = pd.read_pickle("cleaned data/orders_001.pkl")
    customers = pd.read_pickle("cleaned data/customers_001.pkl")
    
    # Display customer info
    print("Customers DataFrame:")
    print(customers.head(5))
    print("\nCustomer Info:")
    print(customers.info())
    
    # Display products and orders info
    print("\nProducts DataFrame:")
    print(products.head(5))
    print("\nOrders DataFrame:")
    print(orders.head(5))
    
    # Drop duplicate columns before merge to prevent 'ValueError: columns overlap'
    cols_to_fix = ['customer_name', 'email', 'country']
    orders = orders.drop(columns=cols_to_fix, errors='ignore')
    
    # Merge orders with customer details
    orders = pd.merge(orders, customers[['customer_id', 'customer_name', 'email', 'country']], 
                     on='customer_id', 
                     how='left')
    
    print("\nOrders after customer merge:")
    print(orders.head(5))
    
    print("\nProducts DataFrame:")
    print(products.head(5))
    
    # Merge orders with product details
    orders = pd.merge(orders, products[['product_id', 'coffee_type', 'roast_type', 'size', 'unit_price', 'profit']], 
                     on='product_id', 
                     how='left')
    
    print("\nOrders after product merge:")
    print(orders.head(5))
    
    # Delete columns ending with "_x" (the empty original columns) and rename columns ending with "_y" (the merged data)
    orders = orders.loc[:, ~orders.columns.str.endswith('_x')]
    orders.columns = orders.columns.str.replace('_y', '', regex=False)
    
    # Merge loyalty from customers with orders
    orders = pd.merge(orders, customers[['customer_id', 'loyalty_card']], 
                     on='customer_id', 
                     how='left')
    
    # Clean up duplicate loyalty columns
    orders = orders.drop(columns=['loyalty_card_y'], errors='ignore')
    orders = orders.rename(columns={'loyalty_card_x': 'loyalty_card'})
    
    # Merge city from customers with orders
    orders = pd.merge(orders, customers[['customer_id', 'city']], 
                     on='customer_id', 
                     how='left')
    
    # Calculate sales and net_profit
    orders['sales'] = orders['quantity'] * orders['unit_price']
    orders['net_profit'] = orders['quantity'] * orders['profit']
    
    # Sort columns with logical order: Order Info → Customer Info → Product Info → Transaction Details
    column_order = [
        'order_id', 'order_date',                    # Order identifiers
        'customer_id', 'customer_name', 'email', 'city', 'country', 'loyalty_card',  # Customer info
        'product_id', 'coffee_type', 'roast_type', 'size',  # Product info
        'quantity', 'unit_price', 'sales', 'profit', 'net_profit'  # Transaction details
    ]
    orders = orders[column_order]
    
    print("\nFinal Orders Info:")
    print(orders.info())
    
    return orders


if __name__ == "__main__":
    orders = load_data()




