# News_Summarizer
Get quick and accurate article summaries with the Newspaper Article Summarizer. Enter the article URL, set the desired summary length, and let the tool extract the key information using advanced NLP techniques. Save time and stay informed effortlessly with this user-friendly news summarization tool

# Newspaper Article Summarizer

The Newspaper Article Summarizer is a Python application that utilizes the Sumy library to summarize news articles from given URLs. It provides a simple user interface using the Streamlit framework.

## Features

- Summarize news articles by providing the URL of the article.
- Adjust the length of the summary by specifying the number of sentences.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/newspaper-article-summarizer.git

   
1. Change to the project directory:
   cd newspaper-article-summarizer

2. Install the required dependencies:
   pip install -r requirements.txt


Usage
1. Run the application:
   streamlit run main.py
2. Access the application in your web browser at http://localhost:8501.
3. Enter the URL of the news article you want to summarize.
4. Adjust the summary length by specifying the number of sentences.
5. Click the "Generate Summary" button to generate the summary.

Examples
Once you provide the URL and specify the summary length, the application retrieves the article, preprocesses the text, and uses the Sumy library for summarization. The generated summary, along with the article's title, authors, and publication date, is displayed in the user interface.

Contributing
Contributions are welcome! If you would like to contribute to this project, please follow the guidelines outlined in CONTRIBUTING.md.
