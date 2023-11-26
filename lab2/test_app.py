import unittest
import json
from app import app

class LibraryAppTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_get_books(self):
        response = self.app.get('/books')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertIsInstance(data, list)

    def test_get_nonexistent_book(self):
        response = self.app.get('/books/999')
        self.assertEqual(response.status_code, 404)

    def test_create_and_delete_book(self):
        # Create a new book
        new_book_data = {"title": "Test Book", "author": "Test Author"}
        response = self.app.post('/books', json=new_book_data)
        self.assertEqual(response.status_code, 201)
        created_book = json.loads(response.get_data(as_text=True))

        # Retrieve the created book
        response = self.app.get(f'/books/{created_book["id"]}')
        self.assertEqual(response.status_code, 200)

        # Delete the created book
        response = self.app.delete(f'/books/{created_book["id"]}')
        self.assertEqual(response.status_code, 204)

        # Verify that the book is deleted
        response = self.app.get(f'/books/{created_book["id"]}')
        self.assertEqual(response.status_code, 404)

    def test_get_members(self):
        response = self.app.get('/members')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertIsInstance(data, list)

    def test_get_nonexistent_member(self):
        response = self.app.get('/members/999')
        self.assertEqual(response.status_code, 404)

    def test_create_and_delete_member(self):
        # Create a new member
        new_member_data = {"name": "Test member", "email": "test123@test.com"}
        response = self.app.post('/members', json=new_member_data)
        self.assertEqual(response.status_code, 201)
        created_member = json.loads(response.get_data(as_text=True))

        # Retrieve the created member
        response = self.app.get(f'/members/{created_member["id"]}')
        self.assertEqual(response.status_code, 200)

        # Delete the created member
        response = self.app.delete(f'/members/{created_member["id"]}')
        self.assertEqual(response.status_code, 204)

        # Verify that the member is deleted
        response = self.app.get(f'/members/{created_member["id"]}')
        self.assertEqual(response.status_code, 404)
        
    def test_get_loans(self):
        response = self.app.get('/loans')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertIsInstance(data, list)

    def test_get_nonexistent_loan(self):
        response = self.app.get('/loans/999')
        self.assertEqual(response.status_code, 404)

    def test_create_and_delete_loan(self):
        # Create a new loan
        new_loan_data = {"book_id": 1, "member_id": 123, "date": "2020-01-01", "r_date": "2020-01-01"}
        response = self.app.post('/loans', json=new_loan_data)
        self.assertEqual(response.status_code, 201)
        created_loan = json.loads(response.get_data(as_text=True))

        # Retrieve the created loan
        response = self.app.get(f'/loans/{created_loan["id"]}')
        self.assertEqual(response.status_code, 200)

        # Delete the created loan
        response = self.app.delete(f'/loans/{created_loan["id"]}')
        self.assertEqual(response.status_code, 204)

        # Verify that the loan is deleted
        response = self.app.get(f'/loans/{created_loan["id"]}')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
