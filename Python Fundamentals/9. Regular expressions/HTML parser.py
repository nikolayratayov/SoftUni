import re


a = input()
news = re.search(r'<title>(.*)</title>', a)
content = re.search(r'<body>(.+)</body>', a)
news = re.sub(r'([<]{1}.*?[>]{1})', '', news.group())
content = re.sub(r'([<]{1}.*?[>]{1})', '', content.group())
news = news.replace(r'\n', '')
content = content.replace(r'\n', '')
print(f'Title: {news}')
print(f'Content: {content}')
