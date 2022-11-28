import wikipedia as wiki

articles = [
    '/Bat', '/Beaver', '/Cougar', '/Elephant', '/Elk',
    '/Giraffe', '/Impala', '/Jaguar', '/Koala', '/Lemur'
]

for i, x in enumerate(articles):
    with open(f'input/input{ i // 5 + 1}/{x.lower()}.txt', 'w') as f:
        f.write(wiki.page(x).content)