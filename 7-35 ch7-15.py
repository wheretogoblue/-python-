buyers= [['James', 1030],
    ['Curry', 893],
    ['Durant', 2050],
    ['Jordan', 990],
    ['David', 2110],
             ['Kevin', 15000],
             ['Mary', 10050],
             ['Tom', 8800],
    ]
Infinite= []
VIP= []
Gold= []

for buyer in buyers:
    name, amount = buyer
    if amount >=10000:
        Infinite.append(buyer)
    elif amount >=1000:
        VIP.append(buyer)
    else:
        Gold.append(buyer)
print("Infinite買家資料", Infinite)
print("VIP買家資料", VIP)
print("Gold買家資料", Gold)

