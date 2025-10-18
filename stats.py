def get_book_text(path):
    with open(path) as book:
        content = book.read()
    return content

def count(book):
    count=len(book.split())
    return count

def count_character(book):
    book=str(book)
    string=book.lower()
    elements = {}
    for item in string:
        elements[item]=elements.get(item,0)+1
    return elements

def sort_on(items):
    return items["num"]

def sort_dictionary(dict):
    list=[]
    for key,value in dict.items():
        list.append({"char": key,"num": value})
    list.sort(reverse=True, key=sort_on)
    return list 
