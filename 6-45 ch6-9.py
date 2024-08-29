import re
#原始內容
a="""Are you sleeping, are you sleeping, Brother John, Brother John?
Morning bells are ringing, morning bells are ringing.
Ding ding dong, Ding ding dong
"""
#逐行處理：去除標點符號、改小寫
lines=a.splitlines()
processed_lines= [re.sub(r'[^\w\s]','',line) for line in lines]
print("歌曲字串內容")
for line in processed_lines:
    print(line)

#將所有行合併轉為列表
alist=" ".join(processed_lines).lower().split()
print("歌曲串列內容")
print(alist)
print("歌曲的字數：",len(alist))
b=input("請輸入字串：").lower()
c=alist.count(b)
print(f"{b}出現{c}次")



