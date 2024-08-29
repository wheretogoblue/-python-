photos=['da1.jpg','da2.png','da3.gif','da4.gif','da5.jpg','da6.jpg','da7.gif']
jpg=[]
png=[]
gif=[]

for photo in photos:
    if photo.endswith('.jpg'):
        jpg.append(photo)
    if photo.endswith('.png'):
        png.append(photo)
    if photo.endswith('.gif'):
        gif.append(photo)
print("jpg檔案串列",jpg)
print("png檔案串列",png)
print("gif檔案串列",gif)
