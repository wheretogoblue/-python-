noodles= {
    '牛肉麵':'100',
    '肉絲麵':'80',
    '陽春麵':'60',
    '大滷麵':'90',
    '麻醬麵':'70'
    }
print(noodles)
sorted_noodles= sorted(noodles.items(), key= lambda item: int(item[1]))

for noodle, price in sorted_noodles:
    print(f"{noodle}：{price}")
