import string
msg='''
Sillicon Stone Education is an unbiased organization,
concentrated on bridging the gap between academic
and the working world in order to benefit society as a
whole. We have carefully crafted our online certifacation system
and test content databases. The content for each topic is
created by experts and is all carefully designed with a
comphrehensive knowledge to greatly benefit all candidates who
participate.'''

msg= msg.translate(str.maketrans('','',string.punctuation)).lower()
msg_list= sorted(list(set(msg.split())))
print("最後串列 ＝ ",msg_list)
