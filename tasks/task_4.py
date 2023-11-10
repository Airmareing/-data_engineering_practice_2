import pickle
import json

with open('../data/products_42.pkl', 'rb') as pkl_file:
    products_data = pickle.load(pkl_file)

with open('../data/price_info_42.json', 'r') as json_file:
    new_prices_data = json.load(json_file)

for update_data in new_prices_data:
    product_name = update_data.get('name', '')
    method = update_data.get('method', '')
    param = update_data.get('param', 0)

    product = next((item for item in products_data if item['name'] == product_name), None)

    if product:
        if method == 'add':
            product['price'] += param
        elif method == 'sub':
            product['price'] -= param
        elif method == 'percent+':
            product['price'] *= (1 + param)
        elif method == 'percent-':
            product['price'] *= (1 - param)

with open('../result/output_data_4.pkl', 'wb') as modified_pkl_file:
    pickle.dump(products_data, modified_pkl_file)