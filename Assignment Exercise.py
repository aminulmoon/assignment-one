"""
Task One
1. Open mobile.py.
2. You will get a variable named mobile_data. You don't need to edit it.
3. At the end of the page you will get a comment where you can start code
4. Make a template using the dictionary data.
5. Your Template must have at least two sentences.
6. USD must be converted to BDT
example Output:
Xiaomi Note 5 is made in China. The price is 300 USD which is almost equal to 30975 BDT

For bonus:
1. make the slug limited to 3 words
2. Make variation of the templates of mobile data

Take Care of:
1. Variable name must be meaningfull
2. Commit at least 2 times in github
"""

# template_variations = """
# The price of Xiaomi Note 5 is 300 USD or 30000 BDT in Bangladesh. It is one of the popular phone which is made in China.
#
# Xiaomi Note 5 price in Bangladesh is 30000 BDT or 300 USD in global. It is manufactured in China.
#
# The Xiaomi Mi 11 is one of the best premium phones which is made in China. This phone is also available in Bangaldesh. The price is 300 USD which is almost 30000 BDT.
#
# The Samsung Galaxy Note20 is a beautiful phone made in china. The price is 300 USD which is almost equal to 30975 BDT.
#
# China made this The Galaxy Note20 takes you to the next level with its outstanding features. The price is 300 USD in Global Market which is 30000 BDT in Bangladesh.
# """


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

for mobile in mobile_dict:

    mobile_name = mobile.get('name')
    price = mobile.get('price')
    country = mobile.get('made')
    print(price)

    template_text =[
        f'The price of {mobile_name} is {price} or 30000 BDT in Bangladesh. It is one of the popular phone which is made in {country}.',

        f'{mobile_name} price in Bangladesh is 30000 BDT or {price} in global. It is manufactured in {country}.',

        f'{mobile_name} is one of the best premium phones which is made in {country}. This phone is also available in Bangaldesh. The price is {price} which is almost 30000 BDT.',

        f'The {mobile_name} is a beautiful phone made in {country}. The price is {price} which is almost equal to 30975 BDT.',

        f'{country} made this {mobile_name} takes you to the next level with its outstanding features. The price is {price} in Global Market which is 30000 BDT in Bangladesh.'
    ]

    print(random.choice(template_text))




