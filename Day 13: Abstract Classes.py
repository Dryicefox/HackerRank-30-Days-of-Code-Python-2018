### Name: Verneri Kalviainen (dryicefox)
### Date: 12/26/2018
### Title: Day 13: Abstract Classes

from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

#Write MyBook class
class MyBook(Book):
    ##Set book to inherit the information in book and add a price to it
    def __init__(self, title, author, price):
        Book.__init__(self, title, author)
        self.price = price

    ##Print out the information requested by the challenge
    def display(self):
        print('Title: ' + self.title)
        print('Author: ' + self.author)
        print('Price: ' + str(self.price))
    

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()
