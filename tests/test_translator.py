import unittest
from unittest.mock import patch
from src.translator import translate_text

class TestTranslator(unittest.TestCase):
    @patch('src.translator.setup_translator_chain')
    def test_translate_text(self, mock_setup_chain):
        mock_chain = mock_setup_chain.return_value
        mock_chain.run.return_value = "Translated text"

        result = translate_text("Original text", "Turkish")
        self.assertEqual(result, "Translated text")

        mock_setup_chain.assert_called_once_with("Turkish")
        mock_chain.run.assert_called_once_with({"text": "Original text", "language": "Turkish"})

if __name__ == '__main__':
    unittest.main()