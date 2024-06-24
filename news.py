import streamlit as st
from newspaper import Article
from transformers import pipeline

# Load the summarization pipeline
summarizer = pipeline("summarization")

# Streamlit interface
st.title("News Summarizer")
st.write("Input a news article URL or text, and get a summarized version.")

# Input fields for URL or text
url = st.text_input("Enter news article URL:")
text = st.text_area("Or paste the news article text:")

def summarize_text(text):
    # Summarize the text using the pipeline
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

def get_article_text(url):
    # Extract article text from the URL
    article = Article(url)
    article.download()
    article.parse()
    return article.text

if st.button("Summarize"):
    if url:
        try:
            article_text = get_article_text(url)
            summary = summarize_text(article_text)
            st.subheader("Summary")
            st.write(summary)
        except Exception as e:
            st.error(f"Error fetching the article: {e}")
    elif text:
        summary = summarize_text(text)
        st.subheader("Summary")
        st.write(summary)
    else:
        st.error("Please provide a URL or text to summarize.")
