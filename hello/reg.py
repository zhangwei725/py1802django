import re

content = 'abc12131abfdsfs'
"""
. 匹配除了\n以为的所有字符
^ 以什么开头的
$  结尾

\d 等同于[0-9]
\D 非数字
\w [A-Za-z0-9]
\W 非单词字符

* 0次到多次
+
?  0次或者一次


"""

# li = re.findall('^ac', content)
li = re.findall('^a[a-z]{1,3}', content)

()  # 分组
# (?P < 名称 > 正则表达式)

print(li)
