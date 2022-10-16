# """
# Task One
# 1. Open mobile.py.
# 2. You will get a variable named mobile_data. You don't need to edit it.
# 3. At the end of the page you will get a comment where you can start code
# 4. Make a template using the dictionary data.
# 5. Your Template must have at least two sentences.
# 6. USD must be converted to BDT
# example Output:
# Xiaomi Note 5 is made in China. The price is 300 USD which is almost equal to 30975 BDT
#
# For bonus:
# 1. make the slug limited to 3 words
# 2. Make variation of the templates of mobile data
#
# Take Care of:
# 1. Variable name must be meaningfull
# 2. Commit at least 2 times in github
# """
#
# # template_variations = """
# # The price of Xiaomi Note 5 is 300 USD or 30000 BDT in Bangladesh. It is one of the popular phone which is made in China.
# #
# # Xiaomi Note 5 price in Bangladesh is 30000 BDT or 300 USD in global. It is manufactured in China.
# #
# # The Xiaomi Mi 11 is one of the best premium phones which is made in China. This phone is also available in Bangaldesh. The price is 300 USD which is almost 30000 BDT.
# #
# # The Samsung Galaxy Note20 is a beautiful phone made in china. The price is 300 USD which is almost equal to 30975 BDT.
# #
# # China made this The Galaxy Note20 takes you to the next level with its outstanding features. The price is 300 USD in Global Market which is 30000 BDT in Bangladesh.
# # """
#
#
# mobile_data = {
#     'status': True,
#     'data': [
#         {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
#         {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
#         {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
#         {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
#         {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
#         {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'}
#     ],
#     'exchange_rate': 103.25
# }
#
#
# #  Your Code Starts from here
#
# import random
# mobile_dict = mobile_data.get('data')
# rate = mobile_data.get('exchange_rate')
#
# for mobile in mobile_dict:
#
#     mobile_name = mobile.get('name')
#     price = mobile.get('price')
#     usd = float(price.strip(' USD'))
#     bdt = round(usd * rate)
#     country = mobile.get('made')
#
#     template_text =[
#         f'The price of {mobile_name} is {usd} USD or {bdt} BDT in Bangladesh. It is one of the popular phone which is made in {country}.',
#
#         f'{mobile_name} price in Bangladesh is {bdt} BDT or {usd} USD in global. It is manufactured in {country}.',
#
#         f'{mobile_name} is one of the best premium phones which is made in {country}. This phone is also available in Bangaldesh. The price is {usd} USD which is almost {bdt} BDT.',
#
#         f'The {mobile_name} is a beautiful phone made in {country}. The price is {usd} USD which is almost equal to {bdt} BDT.',
#
#         f'{country} made this {mobile_name} takes you to the next level with its outstanding features. The price is {usd} USD in Global Market which is {bdt} BDT in Bangladesh.'
#     ]
#
#     print(random.choice(template_text))


"""
Task Two:
1. Open post data.py.
2. You will get a list of dictionaries. You don't need to edit it.
3. At the end of the page you will get a comment where you can start code
4. Add slug field to all the post

We will test it by calling with random number e.g post_data[4]

Expected Output:
{
    'userId': 'Alex Gates',
     'id': 5,
     'title': ' nesciunt quas odio',
     'body': 'repudiandae veniam quaerat sunt sed.....',
     'slug': 'nesciunt-quas-odio'
}

"""

post_data = [
    {
        "userId":  "Alex Gates",
        "id": 1,
        "title": "sunt aut facere repellat provident",
        "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
    },
    {
        "userId":  "Alex Gates",
        "id": 2,
        "title": "qui est esse ",
        "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
    },
    {
        "userId":  "Alex Gates",
        "id": 3,
        "title": "ea molestias quasi exercitationem ",
        "body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut"
    },
    {
        "userId":  "Alex Gates",
        "id": 4,
        "title": "eum et est occaecati ",
        "body": "ullam et saepe reiciendis voluptatem adipisci\nsit amet autem assumenda provident rerum culpa\nquis hic commodi nesciunt rem tenetur doloremque ipsam iure\nquis sunt voluptatem rerum illo velit"
    },
    {
        "userId":  "Alex Gates",
        "id": 5,
        "title": " nesciunt quas odio",
        "body": "repudiandae veniam quaerat sunt sed\nalias aut fugiat sit autem sed est\nvoluptatem omnis possimus esse voluptatibus quis\nest aut tenetur dolor neque"
    },
    {
        "userId":  "Alex Gates",
        "id": 6,
        "title": "dolorem eum magni eos aperiam quia ",
        "body": "ut aspernatur corporis harum nihil quis provident sequi\nmollitia nobis aliquid molestiae\nperspiciatis et ea nemo ab reprehenderit accusantium quas\nvoluptate dolores velit et doloremque molestiae"
    }, ]

# Your Code Start from here

for post_title in post_data:
    title = post_title.get('title')
    stripped_title = title.strip()
    url = stripped_title.replace(' ','-')
    post_title.update({"slug": url})

#Your code ends here

print(post_data[2])

