title = input()
content = input()
comment_list = list()
while True:
    comment = input()
    if comment == "end of comments":
        break
    else:
        comment_list.append(comment)
print(f"""<h1>
    {title}
</h1>""")
print(f"""<article>
    {content}
</article>""")
for current_comment in comment_list:
    print(f"""<div>
    {current_comment}
</div>""")


# def title_func(some_title: str):
#     return f"<h1>\n    {title}\n</h1>"
#
#
# def content_func(some_content: str):
#     return f"<article>\n    {content}\n</article>"
#
#
# def comment_func(some_comments_list: list):
#     for some_comment in some_comments_list:
#         print(some_comment)
#
#
# title = input()
# content = input()
# comment_list = list()
# while True:
#     comment = input()
#     if comment == "end of comments":
#         break
#     else:
#         comment_list.append(f"<div>\n    {comment}\n</div>")
# print(title_func(title))
# print(content_func(content))
# comment_func(comment_list)
