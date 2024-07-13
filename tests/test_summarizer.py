import unittest
from unittest.mock import patch
from src.summarizer import summarize_url

class TestSummarizer(unittest.TestCase):
    @patch('src.summarizer.load_document')
    @patch('src.summarizer.setup_summarization_chain')
    def test_summarize_url(self, mock_setup_chain, mock_load_document):
        mock_load_document.return_value = "Sample document content"
        mock_chain = mock_setup_chain.return_value
        mock_chain.run.return_value = "Summarized content"

        result = summarize_url("https://example.com")
        self.assertEqual(result, "Summarized content")

        mock_load_document.assert_called_once_with("https://example.com")
        mock_setup_chain.assert_called_once()
        mock_chain.run.assert_called_once_with("Sample document content")

if __name__ == '__main__':
    unittest.main()