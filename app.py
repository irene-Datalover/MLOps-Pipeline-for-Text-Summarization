from transformers import pipeline

def summarize_text(text):
    # Initialize the Hugging Face summarizer
    summarizer = pipeline("summarization")

    try:
        # Summarize the input text
        summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
        print("Summary:")
        print(summary[0]['summary_text'])
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    # Example text (you can modify or input your own)
    text = input("Enter the text you want to summarize: ")
    
    summarize_text(text)
