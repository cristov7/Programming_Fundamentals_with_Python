shelf_with_books = input().split("&")
while True:
    command = input()
    if command == "Done":
        break
    else:
        command_list = command.split(" | ")
        info = command_list[0]
        if info == "Add Book":
            book_name = command_list[1]
            if book_name in shelf_with_books:
                continue
            else:
                shelf_with_books.insert(0, book_name)
        elif info == "Take Book":
            book_name = command_list[1]
            if book_name in shelf_with_books:
                shelf_with_books.remove(book_name)
            else:
                continue
        elif info == "Swap Books":
            book1 = command_list[1]
            book2 = command_list[2]
            if book1 in shelf_with_books and book2 in shelf_with_books:
                index_per_book1 = shelf_with_books.index(book1)
                index_per_book2 = shelf_with_books.index(book2)
                shelf_with_books[index_per_book1], shelf_with_books[index_per_book2] = \
                    shelf_with_books[index_per_book2], shelf_with_books[index_per_book1]
            else:
                continue
        elif info == "Insert Book":
            book_name = command_list[1]
            if book_name in shelf_with_books:
                continue
            else:
                shelf_with_books.append(book_name)
        elif info == "Check Book":
            index = int(command_list[1])
            if 0 <= index <= (len(shelf_with_books) - 1):
                name_book = shelf_with_books[index]
                print(name_book)
            else:
                continue
print(", ".join(shelf_with_books))


# def school_library(books: str):
#     shelf_with_books = books.split("&")
#     while True:
#         command = input()
#         if command == "Done":
#             break
#         else:
#             command_list = command.split(" | ")
#             info = command_list[0]
#             if info == "Add Book":
#                 book_name = command_list[1]
#                 if book_name in shelf_with_books:
#                     continue
#                 else:
#                     shelf_with_books.insert(0, book_name)
#             elif info == "Take Book":
#                 book_name = command_list[1]
#                 if book_name in shelf_with_books:
#                     shelf_with_books.remove(book_name)
#                 else:
#                     continue
#             elif info == "Swap Books":
#                 book1 = command_list[1]
#                 book2 = command_list[2]
#                 if book1 in shelf_with_books and book2 in shelf_with_books:
#                     index_per_book1 = shelf_with_books.index(book1)
#                     index_per_book2 = shelf_with_books.index(book2)
#                     shelf_with_books[index_per_book1], shelf_with_books[index_per_book2] = \
#                         shelf_with_books[index_per_book2], shelf_with_books[index_per_book1]
#                 else:
#                     continue
#             elif info == "Insert Book":
#                 book_name = command_list[1]
#                 if book_name in shelf_with_books:
#                     continue
#                 else:
#                     shelf_with_books.append(book_name)
#             elif info == "Check Book":
#                 index = int(command_list[1])
#                 if 0 <= index <= (len(shelf_with_books) - 1):
#                     name_book = shelf_with_books[index]
#                     print(name_book)
#                 else:
#                     continue
#     return ", ".join(shelf_with_books)
#
#
# books_on_shelves = input()
# print(school_library(books_on_shelves))
