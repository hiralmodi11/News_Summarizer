from newspaper import Article
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import nltk
import streamlit as st

def preprocess_text(text):
    # Add additional preprocessing steps here
    return text

def summarize_article(url, summary_length):
    try:
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()

        # Preprocess text
        preprocessed_text = preprocess_text(article.text)

        # Use Sumy library for summarization
        parser = PlaintextParser.from_string(preprocessed_text, Tokenizer("english"))
        summarizer = LexRankSummarizer(Stemmer("english"))
        summarizer.stop_words = get_stop_words("english")

        summary = summarizer(parser.document, summary_length)

        return {
            "title": article.title,
            "authors": article.authors,
            "publish_date": article.publish_date,
            "summary": summary,
        }
    except Exception as e:
        st.error(str(e))

def main():
    st.title("Newspaper Article Summarizer")

    url = st.text_input("Enter URL")
    summary_length = st.number_input("Summary Length (Number of Sentences)", step=1)

    if st.button("Generate Summary"):
        result = summarize_article(url, summary_length)

        if result:
            st.subheader(result["title"])
            st.write(f"Authors: {result['authors']}")
            st.write(f"Publication Date: {result['publish_date']}")
            st.subheader("Summary")
            for sentence in result["summary"]:
                st.write(f"- {sentence}")

if __name__ == "__main__":
    nltk.download("punkt")
    main()


#    cd C:\Users\Hiral\PycharmProjects\news_summarizer
#streamlit run main.py
