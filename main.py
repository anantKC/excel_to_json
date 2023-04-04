# sourcery skip: collection-builtin-to-comprehension
import pandas as pd
import json

# Read CSV data into a Pandas DataFrame
df = pd.read_csv('reward_product_list.csv')

# Create an empty list to hold the categories
categories = []



# Iterate over the rows of the DataFrame
print(len(df))
for index, row in df.iterrows():

    category_name = row['Category']
    subcategory_name = row['Sub-Category']
    product_dict = {
        'Brand': row['Brand'],
        'Suvidhaa SKU': row['Suvidhaa SKU'],
        'Product Title': row['Product Title'],
        'Product Description': row['Product Description'],
        'Product Image Link': row['Product Image Link'],
        'Points': row['Points']
    }
    
    # Check if the category already exists
    category_index = next((index for (index, d) in enumerate(categories) if d['name'].strip().lower() == category_name.strip().lower()), None)
    if category_index is not None:
        
        # Check if the subcategory already exists
        subcategory_index = next((index for (index, d) in enumerate(categories[category_index]['subcategories']) if d['name'] == subcategory_name), None)
        if subcategory_index is not None:
            categories[category_index]['subcategories'][subcategory_index]['products'].append(product_dict)
        else:
            subcategory_dict = {
                'name': subcategory_name,
                'products': [product_dict]
            }
            categories[category_index]['subcategories'].append(subcategory_dict)
    
    # If the category doesn't exist, add it along with the subcategory and product
    else:
        subcategory_dict = {
            'name': subcategory_name,
            'products': [product_dict]
        }
        category_dict = {
            'name': category_name,
            'subcategories': [subcategory_dict]
        }
        categories.append(category_dict)

# Create a dictionary with the categories list
# data_dict = {'categories': categories}
print(len(categories))
print(sorted(list(c['name'] for c in categories)))
# Convert the dictionary to JSON and save it to a file
with open('reward_list.json', 'w') as outfile:
    json.dump(categories, outfile)
