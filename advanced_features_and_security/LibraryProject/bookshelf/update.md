### Update Operation
```python Django

from bookshelf.models import Book
# Update Operation
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)  # Output: Nineteen Eighty-Four