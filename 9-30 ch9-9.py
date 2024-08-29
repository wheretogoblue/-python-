from collections import Counter
import string

# The Zen of Python 文字
zen_text = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

# 將文本轉為小寫並移除標點符號
zen_text = zen_text.lower()
zen_text = zen_text.translate(str.maketrans('', '', string.punctuation))

# 分詞
words = zen_text.split()

# 計算單字出現次數
word_count = Counter(words)

# 將單字按字母排序
sorted_words = sorted(word_count.items())

# 輸出結果
for word, count in sorted_words:
    print(f"{word}: {count}")
