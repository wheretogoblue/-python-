names=['Mary','Josh','Tracy']
print("目前宴會名單",names)
print("1：增加名單")
print("2：刪除名單")
func=input(" = ")
if func==   "1":
    name=input("請輸入名字：")
    names.append(name)
    print("新的宴會名單：",names)
elif func=="2":
    name=input("請輸入名字：")
    if name in names:
        names.remove(name)
        print("新的宴會名單：",names)
else:
        print("名單輸入錯誤")
