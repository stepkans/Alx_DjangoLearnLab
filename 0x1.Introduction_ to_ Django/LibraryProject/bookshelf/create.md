### Create Operation
```python Django

# Create a new book instance
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)  # Output: 1984 by George Orwell published in 1949