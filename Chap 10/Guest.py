filename = 'programming.txt'
with open(filename, 'w') as file_object:
    bookname=input("What's your favorite book?")
    file_object.write(bookname)