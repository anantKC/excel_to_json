# sourcery skip: collection-builtin-to-comprehension
import pandas as pd
import json

# Read CSV data into a Pandas DataFrame
df = pd.read_csv('reward_product_list.csv')


categories = []
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
    for category in categories:
        if category['category'].strip().lower() == category_name.strip().lower():
            
            # Check if the subcategory already exists
            for subcategory in category['subcategory']:
                if subcategory['name'] == subcategory_name:
                    subcategory['products'].append(product_dict)
                    break
            
            # If the subcategory doesn't exist, add it
            else:
                subcategory_dict = {
                    'name': subcategory_name,
                    'products': [product_dict]
                }
                category['subcategory'].append(subcategory_dict)
                break
        
            break
    
    # If the category doesn't exist, add it along with the subcategory and product
    else:
        subcategory_dict = {
            'name': subcategory_name,
            'products': [product_dict]
        }
        category_dict = {
            'category': category_name,
            'subcategory': [subcategory_dict]
        }
        categories.append(category_dict)

# Create a dictionary with the categories list

print(sorted(list(c['category'] for c in categories)))

# Convert the dictionary to JSON and save it to a file
with open('reward_list.json', 'w') as outfile:
    json.dump(categories, outfile)
