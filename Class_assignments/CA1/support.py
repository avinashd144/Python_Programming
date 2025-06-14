# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 23:24:32 2024

@author: LENOVO
"""

# Function to fetch and add data from API
def add_from_api(df, offset, query="shoes"):
    url = f'https://www.asos.com/api/product/search/v2/?offset={offset}&includeNonPurchasableTypes=restocking&q={query}&store=ROW&lang=en-GB&currency=EUR&rowlength=3&channel=desktop-web&country=IE&keyStoreDataversion=mhabj1f-41&limit=72'
    headers = {
        'accept': 'application/json, text/plain, */*',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        new_data = json.loads(response.content)
        new_df = pd.json_normalize(new_data['products'])
        # Select the same key features
        new_key_features = new_df[['id', 'name', 'colourWayId', 'brandName', 'productCode', 'isSellingFast',
                                   'price.current.value', 'price.previous.value', 'price.lowestPriceInLast30Days.value',
                                   'price.isMarkedDown', 'price.currency']]
        new_key_features.rename(columns={
            'isSellingFast': 'sellingIsFast',
            'price.current.value': 'currentPrice',
            'price.previous.value': 'previousPrice',
            'price.lowestPriceInLast30Days.value': 'lowestPriceInLast30Days',
            'price.isMarkedDown': 'priceIsMarkedDown',
            'price.currency': 'currency'
        }, inplace=True)
        return pd.concat([df, new_key_features], ignore_index=True)
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return df

# Example usage
key_features = add_from_api(key_features, offset=144)
print(key_features.tail())
