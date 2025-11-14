import unittest
from app import app

class FlaskTest(unittest.TestCase):
    """
    Test suite for the main Flask application endpoints.
    """

    def setUp(self):
        """Set up the test client before each test."""
        # Sets the app to testing mode
        app.testing = True
        self.client = app.test_client()

    def test_main_page_status_code(self):
        """Test that the main '/' route returns a 200 OK status."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_main_page_content(self):
        """Test that the main '/' route returns the expected greeting."""
        response = self.client.get('/')
        expected_content = 'Hello from the Flask App, managed by CI/CD!'
        # response.data is a byte string, so we decode it for comparison
        self.assertIn(expected_content.encode('utf-8'), response.data)

if __name__ == '__main__':
    unittest.main()