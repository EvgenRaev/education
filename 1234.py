stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
total_price = dict()
for key, vol1 in stock.items():
        for vol2 in prices.values():
            total_price [vol1 * vol2] = key
print (total_price)