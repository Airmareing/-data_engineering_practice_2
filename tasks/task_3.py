import json
import msgpack
import numpy as np

with open('data/products_42.json', 'r') as json_file:
    products = json.load(json_file)

aggregated_data = []

for product in products:
    prices = [item['price'] for item in products if 'price' in item]

    if prices:
        avg_price = np.mean(prices)
        max_price = np.max(prices)
        min_price = np.min(prices)
    else:
        avg_price = max_price = min_price = None

    aggregated_data.append({
        'name': product.get('name', ''),
        'avg_price': avg_price,
        'max_price': max_price,
        'min_price': min_price
    })

with open('result/output_data_3.json', 'w') as json_output:
    json.dump(aggregated_data, json_output, indent=2)

with open('result/output_data_3.msgpack', 'wb') as msgpack_output:
    packed_data = msgpack.packb(aggregated_data, use_bin_type=True)
    msgpack_output.write(packed_data)

size_json = len(json.dumps(aggregated_data).encode('utf-8'))
size_msgpack = len(packed_data)

print(f"Размер файла JSON: {size_json} байт")
print(f"Размер файла msgpack: {size_msgpack} байт")