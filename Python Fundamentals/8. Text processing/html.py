title = input()
title_html = '<h1>\n    ' + title + '\n' + '</h1>'
print(title_html)
content = input()
content_html = '<article>\n    ' + content + '\n' + '</article>'
print(content_html)
while True:
    a = input()
    if a == 'end of comments':
        break
    comment_html = '<div>\n    ' + a + '\n' + '</div>'
    print(comment_html)
