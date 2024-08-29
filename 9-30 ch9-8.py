song= """Are you sleeping, are you sleeping, Brother John, Brother John?
Morning bells are ringing, morning bells are ringing.
Ding ding dong, Ding ding dong. """

mydict= {}
songLower= song.lower()
for ch in sonLower:
    if ch in ".,?":
        songLower= songLower.replace(ch,'')

songList= songLower.split()
for wd in songList:
    if wd in mydict:
        mydict[wd] += 1
    else:
        mydict[wd] = 1
print(f"字串 {max(mydict)[wd]} 出現最多次共出現{max(mydict)[wd]次}")
