import unittest
from unittest.mock import patch
from app.main import app, load_data

class TestChatbot(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_load_data(self):
        data = load_data()
        self.assertTrue(len(data) > 0, "Data should not be empty")

    @patch('openai.Completion.create')
    def test_query(self, mock_openai):
        mock_openai.return_value = {
            'choices': [{'text': 'This is a mock response.'}]
        }
        response = self.app.post('/api/query', json={'query': 'What is your business about?'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('answer', response.json, "Response should contain an answer")

if __name__ == '__main__':
    unittest.main() 