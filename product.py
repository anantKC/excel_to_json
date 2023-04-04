# sourcery skip: convert-to-enumerate
import pandas as pd
import json

# Read CSV data into a Pandas DataFrame
df = pd.read_csv('NCH_Catalogue.csv')

product_list = []
product_id = 1

# Iterate over the rows of the DataFrame
for index, row in df.iterrows():
    product_dict = {
        'id': product_id,
        'Category': row['Category'],
        'Sub-Category': row['Sub-Category'],
        'Brand': row['Brand'],
        'Suvidhaa SKU': row['Suvidhaa SKU'],
        'Product Title': row['Product Title'],
        'Product Description': row['Product Description'],
        'Product Image Link': row['Product Image Link'],
        'Points': row['Points']
    }
    
    product_id += 1
    
    # Add the product dictionary to the product list
    product_list.append(product_dict)

# Convert the list of product dictionaries to JSON and save it to a file
with open('products.json', 'w') as outfile:
    json.dump(product_list, outfile, indent=2)
