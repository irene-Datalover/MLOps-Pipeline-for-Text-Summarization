import unittest
from transformers import pipeline

# Function to summarize text
def summarize_text(text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    try:
        summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        return str(e)

class TestTextSummarization(unittest.TestCase):
    
    def test_summarization(self):
        # Sample input text
        input_text = """
        Text summarization is an important task in Natural Language Processing (NLP). 
        It involves condensing a large body of text into a shorter version, while retaining the key information.
        There are two main types of summarization: extractive and abstractive.
        Extractive summarization selects important sentences or phrases directly from the text.
        Abstractive summarization generates new sentences to summarize the text more effectively.
        """
        
        # Expected summary
        expected_summary = "Text summarization is an important task in Natural Language Processing (NLP). It involves condensing a large body of text into a shorter version, while retaining the key information."
        
        # Get the summary using the summarize_text function
        summary = summarize_text(input_text)
        
        # Assert that the summary is correct (this can be adjusted for your needs)
        self.assertTrue(summary.startswith("Text summarization"))
        self.assertTrue(len(summary) > 0)

    def test_empty_input(self):
        # Test with empty input
        input_text = ""
        summary = summarize_text(input_text)
        self.assertEqual(summary, "Error: text length is too short to summarize")  # Adjust this based on error handling

    def test_invalid_input(self):
        # Test with invalid input (non-text data)
        input_text = 12345  # Invalid input (numeric data)
        summary = summarize_text(input_text)
        self.assertEqual(summary, "Error: text input should be a string")  # Adjust error message as needed

if __name__ == "__main__":
    unittest.main()
