from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from api.models import Book, Author
from django.contrib.auth.models import User


class BookAPITests(APITestCase):
    
    def setUp(self):
        # Create a temporal test user for authenticated requests
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpass')

        # Create an author
        self.author = Author.objects.create(name='Author One')

        # Create a book
        self.book = Book.objects.create(
            title='Test Book',
            publication_year=2020,
            author=self.author
        )
    def test_create_book(self):
        url = reverse('book-list')
        data = {
            'title': 'New Book',
            'publication_year': 2022,
            'author': self.author.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.latest('id').title, 'New Book')
        
    def test_update_book(self):
        url = reverse('book-detail', args=[self.book.id])
        data = {
            'title': 'Updated Book',
            'publication_year': 2021,
            'author': self.author.id
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')
          
    def test_delete_book(self):
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)      