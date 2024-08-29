noodles= {
    '牛肉麵':'100',
    '肉絲麵':'80',
    '陽春麵':'60',
    '大滷麵':'90',
    '麻醬麵':'70'
    }
print(noodles)
max_price= max(noodles.values(), key=int)
max_noodle= max(noodles, key=lambda x:int(noodles[x]))
print(f"最貴的是   {max_noodle} 金額是 {max_price}元")
min_price= min(noodles.values(), key=int)
min_noodle= min(noodles, key=lambda x:int(noodles[x]))
print(f"最便宜的是 {min_noodle} 金額是 {min_price}元")

