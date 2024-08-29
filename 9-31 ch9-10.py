abc= 'abcdefghijklmnopqrstuvwxyz'
ABC= abc.upper()

front3= abc[:3]
end3= abc[3:]
subText= end3+ ' '+ ABC+ front3
newText= abc+ ' '+ ABC
encry_dict= dict(zip(subText, newText))
print("列印編碼字典\n", encry_dict)

msgTest= 'I like python'
cipher= []
for i in msgTest:
    v= encry_dict[i]
    cipher.append(v)
ciphertext= ''.join(cipher)

print("原始字串", msgTest)
print("加密字串", ciphertext)
abc= 'abcdefghijklmnopqrstuvwxyz'
ABC= abc.upper()

front3= abc[:3]
end3= abc[3:]
subText= end3+ ' '+ ABC+ front3
newText= abc+ ' '+ ABC
encry_dict= dict(zip(subText, newText))
print("列印編碼字典\n", encry_dict)

msgTest= 'I like python'
cipher= []
for i in msgTest:
    v= encry_dict[i]
    cipher.append(v)
ciphertext= ''.join(cipher)

print("原始字串", msgTest)
print("加密字串", ciphertext)
