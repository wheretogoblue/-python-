A= {n for n in range(1,100,2)}
B= {n for n in range(0,101,5)}
a1= A | B
a2= A & B
a3= A- B 
a4= B- A
print("聯集：",a1)
print("交集：",a2)
print("A-B差集：",a3)
print("B-A差集：",a4)



