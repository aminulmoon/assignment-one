mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'}
    ],
    'exchange_rate': 103.25
}

#  Your Code Starts from here

import random
mobile_dict = mobile_data.get('data')
rate = mobile_data.get('exchange_rate')

for mobile in mobile_dict:
    # access the variables from the dictionary of list.
    mobile_name = mobile.get('name')
    price = mobile.get('price')
    usd = float(price.strip(' USD'))
        # [The USD price was in string formate with extra letters. First delete the extra letters and keep only digits. Then convert to float. So we can multiply USD with Exchange Rate.]
    bdt = round(usd * rate)
    country = mobile.get('made')

    # 5 variations of template.
    template_text =[
        f'The price of {mobile_name} is {usd} USD or {bdt} BDT in Bangladesh. It is one of the popular phone which is made in {country}.',

        f'{mobile_name} price in Bangladesh is {bdt} BDT or {usd} USD in global. It is manufactured in {country}.',

        f'{mobile_name} is one of the best premium phones which is made in {country}. This phone is also available in Bangaldesh. The price is {usd} USD which is almost {bdt} BDT.',

        f'The {mobile_name} is a beautiful phone made in {country}. The price is {usd} USD which is almost equal to {bdt} BDT.',

        f'{country} made this {mobile_name} takes you to the next level with its outstanding features. The price is {usd} USD in Global Market which is {bdt} BDT in Bangladesh.'
    ]

    print(random.choice(template_text))
