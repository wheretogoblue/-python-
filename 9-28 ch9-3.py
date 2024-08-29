fruits= {
    'Watermelon':'15',
    'Banana':'20',
    'Pineapple':'25',
    'Orange':'12',
    'Apple':'18'
    }
print(fruits)
for fruit in sorted(fruits):
    print(f"{fruit}：{fruits[fruit]}")
