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
        data = {
            'title': 'New Book',
            'publication_year': 2022,
            'author': self.author.id
        }
        response = self.client.post(reverse('book-list'), data, format='json')
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(response.data['title'], 'New Book')
        
    def test_update_book(self):
        # Prepare data to update the book
        update_data = {
            'title': 'Updated Book Title',
            'publication_year': 2021,
            'author': self.author.id  
        response = self.client.put(reverse('book-detail', args=[self.book.id]), update_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Ensure the response contains updated data
        self.assertEqual(response.data['title'], 'Updated Book Title')
        self.assertEqual(response.data['publication_year'], 2021)
        
        # Ensure the book in the database has been updated
        self.book.refresh_from_db()  # Refresh the book instance from the database
        self.assertEqual(self.book.title, 'Updated Book Title')
        self.assertEqual(self.book.publication_year, 2021)
        
    def test_delete_book(self):
        book_id = self.book.id
        response = self.client.delete(reverse('book-detail', args=[book_id]))
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
    
    def test_for_unauthenticated_user(self):
        self.client.logout()
        response = self.client.post(reverse('book-list'), {})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)          