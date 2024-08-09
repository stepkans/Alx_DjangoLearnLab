### Delete Operation
```python Django

from bookshelf.models import Book
# Delete Operation
book.delete()
print(Book.objects.all())  # Output: <QuerySet []>