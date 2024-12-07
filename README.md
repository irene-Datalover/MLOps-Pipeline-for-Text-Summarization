# MLOps-Pipeline-for-Text-Summarization
MLOps Pipeline for Text Summarization using Hugging Face Transformers with CI/CD and Docker Integration


This version emphasizes the MLOps workflow, text summarization, and the integration of CI/CD and Docker for deployment. It covers the key technologies you are working with. Let me know if you'd like any further adjustments!

conda activate venv/

"
git add .

git commit -m "Append changes"

git push -u origin main
"

OUTPUT

Enter the text you want to summarize: Enter the text you want to summarize: Text summarization is an important task in NLP that involves shortening a text to extract key points.
No model was supplied, defaulted to sshleifer/distilbart-cnn-12-6 and revision a4f8f3e (https://huggingface.co/sshleifer/distilbart-cnn-12-6).
Using a pipeline without specifying a model name and revision in production is not recommended.
Device set to use cpu
Your max_length is set to 150, but your input_length is only 31. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=15)
Summary:
 Text summarization is an important task in NLP that involves shortening a text to extract key points .
