"""
book.py
"""

class Book:
    def __init__(self, title, authors):
        self.title = title
        self.authors = authors

    def borrowed_by(self, user_name):
        print("{} borrowed by {}".format(self.title, user_name))

    