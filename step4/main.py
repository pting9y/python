"""
"""

import book
import author

first_author = author.Author("Allison", "A.", "allison@world.com")
book = book.Book("All about Python", first_author)

book.borrowed_by("Allison")