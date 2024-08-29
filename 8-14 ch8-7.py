ps= (1100,652,946,821,955,1024,1155)
mean= sum(ps)/len(ps)
print("平均值：",mean)

var=0
for p in ps:
    var += ((p -mean)**2)
var = var/ (len(ps)-1)
print("變異數：",var)

dev= 0
for p in ps:
    dev += ((p-mean)**2)
dev = (dev/(len(ps)-1))**0.5
print("標準差：",dev)
